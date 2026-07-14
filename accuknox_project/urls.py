"""
URL configuration for accuknox_project project.

Each assessment app gets its own URL namespace.
We use include() so each app manages its own URL patterns.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin panel — available at /admin/
    path('admin/', admin.site.urls),

    # signals_app handles Questions 1, 2, and 3 (Django Signals)
    # All its URLs will be under /signals/
    path('signals/', include('signals_app.urls')),

    # custom_classes handles Question 4 (Rectangle class)
    # All its URLs will be under /classes/
    path('classes/', include('custom_classes.urls')),
]
