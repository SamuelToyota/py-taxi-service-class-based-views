from django.urls import path
from . import views

from django.urls import path
from . import views  # ← duplicado

app_name = "taxi"

urlpatterns = [
    path("manufacturers/", views.ManufacturerListView.as_view(), name="manufacturer-list"),
    ...
]

urlpatterns = [  # ← duplicado
    ...
]
