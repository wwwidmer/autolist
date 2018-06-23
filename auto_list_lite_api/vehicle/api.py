from django.conf import settings

import requests

HEADERS = {
    'x-api-key': settings.AUTOLIST_API_KEY
}

class AutoListAPI(object):
    def __init__(self):
        self.session = requests.session()
        self.base_url = 'https://qa878qmgjk.execute-api.us-east-1.amazonaws.com/'

        self.session.headers.update(HEADERS)

    def getList(self, price_min=None, price_max=None, page=1):
        url = '{}dev?page={}'.format(self.base_url, page)

        if price_min:
            url = '{}&price_min={}'.format(url, price_min)
        if price_max:
            url = '{}&price_min={}'.format(url, price_max)
        try:
            response = self.session.get(url)
        except ConnectionError:
            raise Exception('TODO')
        if response.status_code != 200:
            raise Exception('TODO')
        json = response.json()
        return json['records']