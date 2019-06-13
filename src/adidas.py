import requests

class Adidas(object):
    def __init__(self):
        self.base_url = "https://www.adidas.com"
    
    def formatProxy(self,proxy):
        if ":" in str(proxy) and "127.0.0.1" not in str(proxy):
            p = proxy.split(":")
            if len(p)==4:
                return {"http":"http://{}:{}@{}:{}".format(p[2], p[3], p[0], p[1]),"https":"https://{}:{}@{}:{}".format(p[2], p[3], p[0], p[1])}
            elif len(p)==2:
                return {"http":"http://{}:{}".format(p[0], p[1]),"https":"https://{}:{}".format(p[0], p[1])}
            else:
                return None
        elif proxy is None or "127.0.0.1" in str(proxy):
            return None
        elif "https" in str(proxy) or "http" in str(proxy):
            return {"http":str(proxy),"https":str(proxy)}
        else:
            return None
    def monitorStockForDrop(self,sku,locale,proxy=None):
        url = "{}/hpl/content/availability/{}/{}.json".format(self.base_url,str(locale).upper(),str(sku).upper())

        headers = {'Accept'     : 'application/json, text/plain, */*',
                   'DNT'        : '1',
                   'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
        return requests.get(url,headers=headers,proxies=self.formatProxy(proxy))
