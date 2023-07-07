from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from . import api

urlpatterns = [
    path('me/', api.me, name='me'),
    path('signup/', api.signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('update-me/', api.updateDetails, name='update-me')
]
