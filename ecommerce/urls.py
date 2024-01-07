from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),  # Include URLs users app
    path("products/", include("products.urls")),  # Include URLs products app
    path("orders/", include("orders.urls")),  # Include URLs orders app
]
