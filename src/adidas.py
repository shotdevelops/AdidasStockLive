import requests

class Adidas(object):
    def __init__(self):
        self.base_url = "https://www.adidas.com"
    
    def monitorStockForDrop(self,sku,locale):
        url = "{}/hpl/content/availability/{}/{}.json".format(self.base_url,str(locale).upper(),str(sku).upper())

        headers = {'Accept'     : 'application/json, text/plain, */*',
                   'DNT'        : '1',
                   'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
        return requests.get(url,headers=headers)
