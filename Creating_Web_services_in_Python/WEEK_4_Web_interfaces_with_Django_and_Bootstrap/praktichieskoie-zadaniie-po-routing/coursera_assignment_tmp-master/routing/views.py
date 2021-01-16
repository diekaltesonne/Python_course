from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'PUT', 'POST'])
def simple_route(request, something=None):
    if request.method == 'GET' and something == None:
        return HttpResponse(status=200)
    elif request.method in ['POST', 'PUT']:
        return HttpResponse(status=405)

# @require_http_methods(['GET'])
def slug_route(request, first=None, second=None):
    if second is None:
        return HttpResponse(content=first, status=200)
    else:
        return HttpResponse(status=404)

#@require_http_methods(['GET'])
def sum_route(request,number_1,number_2,third = None):
    if (third == None):
        answer = int(number_1)+int(number_2)
        return HttpResponse(content=str(answer), status=200)
    else:
        return HttpResponse(status=404)

@require_http_methods(['GET'])
def sum_get_method(request):
    first = request.GET.get('a')
    second = request.GET.get('b')
    if check(first) and check(second):
        return HttpResponse(content=str(int(first) + int(second)), status=200)
    else:
        return HttpResponse(status=400)

@require_http_methods(['POST'])
def sum_post_method(request):
    first = request.POST.get('a')
    second = request.POST.get('b')
    if check(first) and check(second):
        return HttpResponse(content=str(int(first) + int(second)), status=200)
    else:
        return HttpResponse(status=400)

def check(string):
    try:
        if string.isdigit():
           return True
        else:
            try:
                float(string)
                return True
            except ValueError:
                return False
    except:
        return False
