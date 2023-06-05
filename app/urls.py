from django.urls import path, include

from app.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('ielts/', IELTSViews.as_view(), name='ielts'),
    path('', MainViews.as_view(), name='ielts'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)