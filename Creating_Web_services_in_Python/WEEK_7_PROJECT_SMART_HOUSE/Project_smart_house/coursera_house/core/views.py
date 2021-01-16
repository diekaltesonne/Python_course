import requests
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import FormView

from .models import Setting
from .form import ControllerForm

TOKEN = settings.SMART_HOME_ACCESS_TOKEN
url = settings.SMART_HOME_API_URL
headers = {'Authorization': f'Bearer {TOKEN}'}

# 1. Делайте лишь один GET-запрос для получения данных из API на каждый запрос
# к вашему приложению.
# 2. Делайте не более одного POST-запроса на изменение данных в API на каждый
# запрос к вашему приложению.
# Если параметры света в форме не изменились - не надо их отправлять в API.
# Все это относится и к задаче в celery.
# 3. Обязательно отрабатывайте вариант, когда ваши запросы к API
# заканчиваются неудачно.
# 4. Помните, что запросы requests могут как бросать исключения,
# так и просто возвращать ответ с ошибочным кодом.
# 5. Пока форма невалидна в POST-запросе - не делайте каких-либо запросов к API.
# Грейдер не оценит такого внимания.

def get_or_update(controller_name, label, value):
    try:
        entry = Setting.objects.get(controller_name=controller_name)
    except Setting.DoesNotExist:
        Setting.objects.create(
            controller_name = controller_name,
            label = label,
            value = value
        )
    else:
        entry.value = value
        entry.save()

class ControllerView(FormView):

    form_class = ControllerForm
    template_name = 'core/control.html'
    success_url = reverse_lazy('form')

    def form_valid(self, form):
        get_or_update(
            'bedroom_target_temperature',
            'Bedroom target temperature',
            form.cleaned_data['bedroom_target_temperature']
        )
        get_or_update(
            'hot_water_target_temperature',
            'Hot water target temperature value',
            form.cleaned_data['hot_water_target_temperature']
        )
        controller_data = requests.get(url, headers=headers).json().get('data')
        if controller_data:
            controller_bedroom_light = list(
                filter(lambda x: 'bedroom_light' in x.values(), controller_data)
            )[0]['value']
            controller_bathroom_light = list(
                filter(lambda x: 'bathroom_light' in x.values(), controller_data)
            )[0]['value']
            smoke_detector = list(
                filter(lambda x: 'smoke_detector' in x.values(),
                       controller_data)
            )[0]['value']
            load = {'controllers': []}

            if not smoke_detector:
                if form.cleaned_data['bedroom_light'] != controller_bedroom_light:
                    load['controllers'].append(
                        {'name': 'bedroom_light', 'value'
                        : form.cleaned_data['bedroom_light']})
                if form.cleaned_data['bathroom_light'] != controller_bathroom_light:
                    load['controllers'].append(
                        {'name': 'bathroom_light', 'value'
                        : form.cleaned_data['bathroom_light']})
                requests.post(url, headers=headers, json = load)

        return super(ControllerView, self).get(form)

    def get_context_data(self, **kwargs):
        context = super(ControllerView, self).get_context_data()
        headers = {'Authorization': f'Bearer {settings.SMART_HOME_ACCESS_TOKEN}'}
        try:
            current_controller_data = requests.get(
                settings.SMART_HOME_API_URL, headers=headers
            ).json()
            context['data'] = current_controller_data
        except:
            context['data'] = {}
        return context

    def get_initial(self):
        initial = super(ControllerView, self).get_initial()
        initial['bedroom_target_temperature'] = 21
        initial['hot_water_target_temperature'] = 80
        return initial

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        if not context.get('data'):
            return self.render_to_response(context, status=502)
        return self.render_to_response(context)
