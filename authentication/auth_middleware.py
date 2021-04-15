from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from authentication.models import MyToken


class CheckTokenMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path != '/login/' and request.path != '/admin/':
            try:
                token = request.COOKIES['Auth_token']
                if MyToken.objects.filter(mytoken=token).exists():
                    pass
                else:
                    response = redirect('login/')
                    return response
            except:
                return redirect('login/')
