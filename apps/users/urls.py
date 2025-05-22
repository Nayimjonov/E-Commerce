from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    AuthorizeAPIView,
    ForgotPasswordAPIView,
    LoginAPIView,
    LogoutAPIView,
    ResetPasswordAPIView,
    VerifyAPIView,
)

urlpatterns = [
    path("auth/authorize/", AuthorizeAPIView.as_view(), name="authorize"),
    path("auth/verify/", VerifyAPIView.as_view(), name="verify"),
    path("auth/login/", LoginAPIView.as_view(), name="login"),
    path("auth/logout/", LogoutAPIView.as_view(), name="logout"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "auth/forgot-password/",
        ForgotPasswordAPIView.as_view(),
        name="forgot_password",
    ),
    path(
        "auth/reset-password/",
        ResetPasswordAPIView.as_view(),
        name="reset_password",
    ),
]
