import json,time,sys,os
from src.adidas import Adidas
Adidas = Adidas()

def parseSettings():
    settings_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"settings.json")
    try:
        with open(settings_path,encoding='utf-8') as f:
            data = json.loads(f.read())
    except:
        print("Failed to load Settings file. Check File and run again!")
        sys.exit()
    
    return data

def parseEndpoint(sku,locale):
    r = Adidas.monitorStockForDrop("EG5293","AU")
    if r.status_code==200:
        try:
            JSON = r.json()
            return JSON
        except:
            return []
    else:
        return []

if __name__ == "__main__":
    config = parseSettings()
    sku = config['SKU']
    locale = config['locale']
    delay = config['delay']
    print("Starting Adidas {} Monitor for SKU [{}]".format(locale,sku))
    print("-"*20)
    while True:
        data = parseEndpoint(sku,locale)
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

