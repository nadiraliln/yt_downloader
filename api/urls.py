from django.urls import path
from .views import stream_download

urlpatterns = [
    path('stream-download/', stream_download),
]