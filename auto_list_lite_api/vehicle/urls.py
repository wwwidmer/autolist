from django.urls import path

from .views import VehicleListView, VehiclePageView


urlpatterns = [
    path('', VehicleListView.as_view()),
    path('<str:vin>',VehiclePageView.as_view())
]