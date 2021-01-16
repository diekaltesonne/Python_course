import json
from  django.core.validators import RegexValidator
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator
from django import forms
from .models import Item, Review

#[\s\w+][\S]*
def jsonForm(req):
    return json.loads(req.body.decode('utf-8'))

class AddItemView_Form(forms.Form):
    title = forms.CharField(max_length = 64,validators=[RegexValidator(regex= r"[\s+\D+]")],required = True)
    description = forms.CharField(max_length = 1024,validators=[RegexValidator(regex= r"[\s+\D+]")],required = True)
    price = forms.IntegerField(max_value = 1000000,min_value = 1,required = True)


@method_decorator(csrf_exempt, name='dispatch')
class AddItemView(View):
    """View для создания товара."""
    def post(self, request):
        if request.method == 'POST':
            try:
                document = jsonForm(request)
            except:
                return JsonResponse(status=400, data={})
            form = AddItemView_Form(document)
            if form.is_valid():
                dic = form.cleaned_data
                i = Item(**dic)
                i.save()
                return JsonResponse(data={'id': i.id}, status=201)
        return JsonResponse(data={}, status=400)
            #try:
            #    data = json.loads(request.body)
            #except:
            #    return JsonResponse(status=400, data={})

class PostReviewView_Form(forms.Form):
    text = forms.CharField(max_length = 1024,validators=[RegexValidator(regex= r"[\s+\D+]")],required = True)
    grade = forms.IntegerField(max_value = 10,min_value = 1,required = True)
@method_decorator(csrf_exempt, name='dispatch')
class PostReviewView(View):
    """View для создания отзыва о товаре."""
    def post(self, request, item_id):
        if request.method == 'POST':
            try:
                item = Item.objects.get(id=item_id)
            except Item.DoesNotExist:
                return JsonResponse(status=404, data={})
            try:
                data = json.loads(request.body)
            except:
                return JsonResponse(status=400, data={})
            form = PostReviewView_Form(data)
            if form.is_valid():
                dic = form.cleaned_data
                rev = Review(text = dic['text'], grade = dic['grade'], item = Item.objects.get(pk=item_id))
                rev.save()
                return JsonResponse(data={'id': rev.id}, status=201)
        return JsonResponse(data = {}, status=400)

class GetItemView(View):
    def get(self, request, item_id):
        if request.method == 'GET':
            try:
                item = Item.objects.prefetch_related('review_set').get(id=item_id)
            except Item.DoesNotExist:
                return JsonResponse(status=404, data={})
            item_dict = model_to_dict(item)
            item_reviews = [model_to_dict(x) for x in item.review_set.all()]
            item_reviews = sorted(item_reviews, key=lambda review: review['id'], reverse=True)[:5]
            for review in item_reviews:
                review.pop('item', None)
            item_dict['reviews'] = item_reviews
            return JsonResponse(item_dict, status=200)
