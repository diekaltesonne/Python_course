## Решение задания по аутентификации и авторизации
Для реализации HTTP Basic Auth в фреймворке Django обычно используются middleware или реализуется auth backend https://docs.djangoproject.com/en/dev/topics/auth/customizing/ Но в данном случае так как весь код должен располагаться в файле views.py лучше реализовать аутентификацию на базе декоратора для view:
```Python
def basicauth(view_func):
    """Декоратор реализующий HTTP Basic AUTH."""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if 'HTTP_AUTHORIZATION' in request.META:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2:
                if auth[0].lower() == 'basic':
                    token = base64.b64decode(auth[1].encode('ascii'))
                    username, password = token.decode('utf-8').split(':')
                    user = authenticate(username=username, password=password)
                    if user is not None and user.is_active:
                        request.user = user
                        return view_func(request, *args, **kwargs)

        response = HttpResponse(status=401)
        response['WWW-Authenticate'] = 'Basic realm="Somemart staff API"'
        return response
    return _wrapped_view
```
Декоратор выполняет аутентификацию пользователя используя стандартный метод authenticate из пакета django.contrib.auth. Также в задании указано, что помимо того что пользователь должен быть аутентифицирован, у пользователя должен быть проставлен флаг is_staff. В нашем случае мог бы подойти декоратор staff_member_required, но так как у нас API и мы не хотим осуществлять редирект на страницу логина, то стоит реализовать свой декоратор.
```Python
def staff_required(view_func):
    """Декоратор проверяющший наличие флага is_staff у пользователя."""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_staff:
            return view_func(request, *args, **kwargs)
        response = HttpResponse(status=403)
        return response
    return _wrapped_view
```
Теперь остается только подключить декораторы к View.
```Python
from django.utils.decorators import method_decorator
...
@method_decorator(basicauth, name='dispatch')
@method_decorator(staff_required, name='dispatch')
class AddItemView(View):
...
```
