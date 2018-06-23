from django.urls import path, include

from django.views.generic.base import RedirectView
    
urlpatterns = [
    path('', RedirectView.as_view(url='/vehicle')),
    path('vehicle/', include('vehicle.urls'))
]
