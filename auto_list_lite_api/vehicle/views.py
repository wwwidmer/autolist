from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.views import View

from .models import Vehicle

from .api import AutoListAPI  

class VehicleListView(View):
    def get(self, request):
        '''
        Call the API and fill in recorded pageviews
        '''
        auto_list_api = AutoListAPI()
        vehicles = []
        for vehicle in auto_list_api.getList():
            try:
                vehicle['page_views'] = Vehicle.objects.get(
                    vin=vehicle['vin'].lower()
                ).page_views
            except ObjectDoesNotExist:
                print('vehicle', vehicle['vin'])
                pass


            vehicles.append(vehicle)

        return HttpResponse(vehicles)


class VehiclePageView(View):

    def post(self, request, vin):
        vehicle, _ = Vehicle.objects.get_or_create(vin=vin.lower())
        vehicle.page_views += 1
        vehicle.save()

        return HttpResponse()