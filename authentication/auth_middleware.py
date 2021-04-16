from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from authentication.models import MyToken


class CheckTokenMiddleware(MiddlewareMixin):

    def process_request(self, request):

        if not request.path.startswith('/login/') and not request.path.startswith('/admin/'):
            if 'Auth_token' not in request.COOKIES:
                return redirect('/login/')
            token = request.COOKIES['Auth_token']

            if not MyToken.objects.filter(mytoken=token).exists():
                response = redirect('/login/')
                return response

