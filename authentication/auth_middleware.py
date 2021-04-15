from django.shortcuts import redirect

from authentication.models import MyToken


def auth_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        # print(request.cookies)
        # if not request.path == "confirm":
        #     try:
        #         print(Cliente.objects.get(usuario_id=request.user.id))
        #     except Cliente.DoesNotExist:
        #         return redirect('confirm')
        return response
    return middleware


    #     try:
    #         token = request.cookies['MyToken']
    #     except:
    #         return redirect('login/')
    #     if token in MyToken.objects.all():
    #         pass
    #     else:
    #         return redirect ('login/')

    # response.set_cookie(
    #     "Auth",
    #     "1263516731289",
    #     365 * 24 * 60 * 60,
    # )
