import requests

url_front = "http://api.vworld.kr/req/address?"
url_params = "service=address&request=getcoord&version=2.0&crs=epsg:4326&refine=true&simple=false&format=json&type=road"
url_address = "&address="
url_key = "&key="
address = "경기도 수원시 영통구 광교산로 154-42 1" 
auth_key = "E51C295D-8B20-3B3C-94B0-99A30A7B20DE"
# url 완성
url = url_front + url_params + url_address + address + url_key + auth_key
print(url)
result = requests.get(url)
json_data = result.json()
print(json_data)

if json_data['response']['status'] == 'OK':
    x = json_data['response']['result']['point']['x']
    y = json_data['response']['result']['point']['y']
    print("\n경도: ", x, "\n위도: ", y)