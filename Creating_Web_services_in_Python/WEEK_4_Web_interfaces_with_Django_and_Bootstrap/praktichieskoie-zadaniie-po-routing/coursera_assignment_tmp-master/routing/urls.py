from django.conf.urls import url
from routing.views import *
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
url(r'^simple_route/$',csrf_exempt(simple_route)),
url(r'^slug_route/([0-9a-z-_]{0,16})/$',slug_route),
url(r'^sum_route/(?P<number_1>(-[0-9]+)|([0-9]+))/(?P<number_2>(-[0-9]+)|([0-9]+))/$',sum_route),
url(r'^sum_get_method/$',sum_get_method),
url(r'^sum_post_method/$',csrf_exempt(sum_post_method))
]
# csrf_exempt(views.ObjectView.as_view())
