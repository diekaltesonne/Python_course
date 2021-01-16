from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
import re
# Create your views here.

@require_http_methods(['GET', 'POST'])
def echo_0(request):
    if request.method == 'GET' and something == None:
        return render(request,'templates/echo.html',context)
    elif request.method in ['POST', 'PUT']:
        return HtppBadResponse(status=405)

def parser(string):
    result = re.match(r'[aA-zZ]+',string)
    return result.group(0)


# def echo(request):
#     try:
#         if (request.method == 'GET'):
#             meta = parser(request.META['QUERY_STRING'])
#             return render(request, 'echo.html', context={
#                 'get_letters': meta,
#                 'get_value': request.GET.get(meta),
#                 'get_tag': request.META.get('HTTP_X_PRINT_STATEMENT'),
#                 'request_method': request.META['REQUEST_METHOD'].lower()
#                 })
#         elif request.method == 'POST':
#             meta = parser(request.META['QUERY_STRING'])
#             return render(request, 'echo.html', context={
#                 'get_letters': meta,
#                 'get_value': request.POST.get(meta),
#                 'get_tag': request.META.get('HTTP_X_PRINT_STATEMENT'),
#                 'request_method': request.META['REQUEST_METHOD'].lower()
#                 })
#     except:
#         return HttpResponse(status=404)

# def echo(request):
#     if (request.method == 'GET'):
#         meta = parser(request.META['QUERY_STRING'])
#         return render(request, 'echo.html', context={
#             'get_letters': meta,
#             'get_value': request.GET.get(meta),
#             'get_tag': request.META.get('HTTP_X_PRINT_STATEMENT'),
#             'request_method': request.META['REQUEST_METHOD'].lower()
#             })
#     elif request.method == 'POST':
#         #print(request.META['QUERY_STRING'])
#         print(request.POST)
#         return render(request, 'echo.html', context={
#              'get_letters':'a',
#              'get_value': 1,
#              'get_tag': request.META.get('HTTP_X_PRINT_STATEMENT'),
#              'request_method': request.META['REQUEST_METHOD'].lower()
#              })

def echo(request):
    context = {
        'get' : request.GET,
        'post' : request.POST,
        'meta' : request.META
    }
    return render(request,"echo.html",context = context)


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })

# <!-- {% extends base.html%} -->
#

def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
#
# <!--DOCTYPE html -->
# <html>
# <body>
# {% if 'QUERY_STRING' in request.META %}
#     <h1> {{ request_method }} {{ get_letter }}: {{ get_value }} statement is empty </h1>
# {% elif 'HTTP_X_PRINT_STATEMENT' in request.META %}
#     <h2> statement is {{get_tag}} </h2>
# {% endif %}
# </body>
# </html>
