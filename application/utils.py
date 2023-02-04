import requests

def get_lost():
    url="http://localhost:1337/api/lost-items"
    lost_items=requests.get(url).json()
    return lost_items.get("data")

def get_found():
    url="http://localhost:1337/api/found-items"
    found_items=requests.get(url).json()
    print (found_items.get("data"))


if __name__=="__main__":
    get_found()