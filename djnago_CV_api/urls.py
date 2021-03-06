from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('face-detection/', include('face_detection.urls')),
    path('image-processing/', include('image_processing.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
