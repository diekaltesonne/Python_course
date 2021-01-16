from __future__ import absolute_import, unicode_literals
import requests
from celery import task
from django.conf import settings
from django.core.mail import EmailMessage
from .models import Setting

TOKEN = settings.SMART_HOME_ACCESS_TOKEN
url = settings.SMART_HOME_API_URL
headers = {'Authorization': f'Bearer {TOKEN}'}

@task()
def smart_home_manager():
    
    cld = requests.get(url, headers=headers).json().get('data')
    cld = {x['name']: x for x in cld}
    load = {
        'controllers': []
    }

    if cld['leak_detector']['value']:
        # если датчик показывает протечку и есть гор. и/или хол. вода,
        # перекрываем гор. и/или хол. воду
        if cld['cold_water']['value']:
            load['controllers'].append({'name': 'cold_water', 'value': False})

        if cld['hot_water']['value']:
            load['controllers'].append({'name': 'hot_water', 'value': False})
        email = EmailMessage(
            'leak detector',
            'text',
            settings.EMAIL_HOST,
            [settings.EMAIL_RECEPIENT],
        )
        email.send(fail_silently=False)

    # если протечка или нет холодной воды
    if cld['leak_detector']['value'] or \
            not cld['cold_water']['value']:
        if cld['boiler']['value']:
            load['controllers'].append({'name': 'boiler', 'value': False})
        if cld['washing_machine']['value'] in ('on', 'broken'):
            load['controllers'].append({'name': 'washing_machine', 'value': "off"})

    boiler_temperature = cld['boiler_temperature']['value']
    hot_water_target_temperature = Setting.objects.get(
        controller_name='hot_water_target_temperature').value

    bedroom_temperature = cld['bedroom_temperature']['value']
    bedroom_target_temperature = Setting.objects.get(
        controller_name='bedroom_target_temperature').value

    if cld['smoke_detector']['value']:
        # если дым, выключаем кондиционер, бойлер и свет, но только если они включены
        if cld['air_conditioner']['value']:
            load['controllers'].append(
                {'name': 'air_conditioner', 'value': False}
            )
        if cld['bathroom_light']['value']:
            load['controllers'].append(
                {'name': 'bathroom_light', 'value': False}
            )
        if cld['bedroom_light']['value']:
            load['controllers'].append(
                {'name': 'bedroom_light', 'value': False}
            )
        if cld['boiler']['value']:
            load['controllers'].append({'name': 'boiler', 'value': False})
        if cld['washing_machine']['value'] in ('on', 'broken'):
            load['controllers'].append(
                {'name': 'washing_machine', 'value': 'off'}
            )

    can_turn_on = {
        'boiler': cld['cold_water']['value'] and \
                  not cld['leak_detector']['value'] and \
                  not cld['smoke_detector']['value'] and \
                  not cld['boiler']
        ,
        'air_conditioner': not cld['smoke_detector']['value']
    }

    if (boiler_temperature < hot_water_target_temperature * 0.9) and \
            can_turn_on['boiler']:
        load['controllers'].append({'name': 'boiler', 'value': True})

    if boiler_temperature > hot_water_target_temperature * 1.1:
        load['controllers'].append({'name': 'boiler', 'value': False})

    if (bedroom_temperature < bedroom_target_temperature * 0.9) and \
            can_turn_on['air_conditioner']:
        load['controllers'].append({'name': 'air_conditioner', 'value': False})

    if bedroom_temperature > bedroom_target_temperature * 1.1:
        load['controllers'].append({'name': 'air_conditioner', 'value': True})



    outdoor_light = cld['outdoor_light']['value']
    bedroom_light = cld['bedroom_light']['value']
    if cld['curtains']['value'] == 'slightly_open':
        pass
    else:
        if outdoor_light < 50 and not bedroom_light:
            load['controllers'].append({'name': 'curtains', 'value': 'open'})
        elif outdoor_light > 50 or bedroom_light:
            load['controllers'].append({'name': 'curtains', 'value': 'close'})

    if load['controllers']:
        unique = []
        for item in load['controllers']:
            if item not in unique:
                unique.append(item)
        load['controllers'] = unique
        requests.post(url, headers=headers, json=load)
