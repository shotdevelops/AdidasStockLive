import json,time,sys,os,random
from src.adidas import Adidas
Adidas = Adidas()

def parseProxies():
    proxies = []
    proxy_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"proxies.txt")
    with open(proxy_path) as f:
        for i in f.read().splitlines():
            proxies.append(i)
    if proxies is []:
        proxies.append(None)
    return proxies
def parseSettings():
    settings_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"settings.json")
    try:
        with open(settings_path,encoding='utf-8') as f:
            data = json.loads(f.read())
    except:
        print("Failed to load Settings file. Check File and run again!")
        sys.exit()
    
    return data

def parseEndpoint(sku,locale,proxy):
    r = Adidas.monitorStockForDrop(sku,locale,proxy=proxy)
    if r.status_code==200:
        try:
            JSON = r.json()
            return JSON
        except:
            return []
    else:
        return []

if __name__ == "__main__":
    proxies = parseProxies()
    config = parseSettings()
    sku = config['SKU']
    locale = config['locale']
    delay = config['delay']
    print("Starting Adidas {} Monitor for SKU [{}]".format(locale,sku))
    print("-"*20)
    while True:
        proxy = random.choice(proxies)
        data = parseEndpoint(sku,locale,proxy)
        if data != []:
            print("[{}] is Live!".format(sku))
            print("-"*20)
            for i in data["variation_list"]:
                print("Size : {}".format(str(i['size'])))
                print("Status : {}".format(str(i['availability_status'])))
                print("Stock level : {}".format(str(i['availability'])))
                print("-"*20)
            break
        else:
            time.sleep(int(delay))

