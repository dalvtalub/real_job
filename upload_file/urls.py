from django.urls import path
from .views import upload_file
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', upload_file),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
