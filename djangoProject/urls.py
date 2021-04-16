from django.contrib import admin
from django.urls import path, include

from authentication.views import logout

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('view_table.urls')),
    path('upload_file/', include('upload_file.urls')),
    path('login/', include('authentication.urls')),
    path('logout/', logout)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)