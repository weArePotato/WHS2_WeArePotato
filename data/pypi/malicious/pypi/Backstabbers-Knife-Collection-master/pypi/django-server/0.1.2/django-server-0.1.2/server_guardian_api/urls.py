"""URLs for the server_guardian_api app."""
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$',
        views.ServerGuardianAPIView.as_view(),
        name='server_guardian_api'),
]
