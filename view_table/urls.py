from django.urls import path, include
from .views import view_table
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', view_table),
                  path('download_file/', include('download_file.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
