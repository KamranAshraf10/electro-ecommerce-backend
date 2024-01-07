from django.urls import path, include
from users.views import UserViewSet, UserRegistrationAPIView, AdminRegistrationAPIView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r"users", UserViewSet)


urlpatterns = [
    # DRF viewset
    path(
        "api/", include(router.urls)
    ),  # Note: This will prepend 'api/' to all router URLs
    # JWT Token Endpoints
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # User and Admin Registration
    path(
        "api/register/user/",
        UserRegistrationAPIView.as_view(),
        name="user_registration",
    ),
    path(
        "api/register/admin/",
        AdminRegistrationAPIView.as_view(),
        name="admin_registration",
    ),
]
