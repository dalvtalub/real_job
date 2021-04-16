from django.contrib import admin
from django.urls import path, include
from authentication.views import logout

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('view_table.urls')),
    path('upload_file/', include('upload_file.urls')),
    path('login/', include('authentication.urls')),
    path('logout/', logout)
]
