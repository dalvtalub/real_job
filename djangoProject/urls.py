from django.contrib import admin
from django.urls import path, include
from view_table.views import view_table

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),

    path('', include('view_table.urls')),
    path('upload_file/', include('upload_file.urls')),
]

