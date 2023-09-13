from django.urls import path
from .views import SimpleUploadView

urlpatterns = [
    path('', SimpleUploadView.as_view(), name='upload_view'),
    # Other URL patterns
]