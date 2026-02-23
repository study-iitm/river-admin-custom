from django.urls import re_path
from rest_framework.authtoken.views import ObtainAuthToken
from river_admin.views import urls

class CustomObtainAuthToken(ObtainAuthToken):
    authentication_classes = []

urlpatterns = [
                  re_path(r'^api-token-auth/', CustomObtainAuthToken.as_view()),
              ] + urls
