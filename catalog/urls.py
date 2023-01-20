from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import catalog


app_name = CatalogConfig.name

urlpatterns = [
    path('', catalog),
]
