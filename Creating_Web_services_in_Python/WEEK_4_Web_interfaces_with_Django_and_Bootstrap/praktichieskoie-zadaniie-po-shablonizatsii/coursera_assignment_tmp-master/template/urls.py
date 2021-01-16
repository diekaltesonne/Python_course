from django.conf.urls import url
from template.views import echo, filters, extend
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^echo/$', csrf_exempt(echo)),
    url(r'^filters/$', csrf_exempt(filters)),
    url(r'^extend/$', csrf_exempt(extend))
]
