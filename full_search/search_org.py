import requests
from distance import lonlat_distance

API_KEY = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"


def search_organization(ll=None, text="Аптека", lang="ru_RU", org_type="biz"):
    search_params = {
        "apikey": API_KEY,
        "text": text,
        "lang": lang,
        "ll": ll,
        "type": org_type
    }
    search_api_server = "https://search-maps.yandex.ru/v1/"
    response = requests.get(search_api_server, params=search_params)

    json_response = response.json()
    organization = json_response["features"][0]

    org_name = organization["properties"]["CompanyMetaData"]["name"]
    # Адрес организации.
    org_address = organization["properties"]["CompanyMetaData"]["address"]

    org_work_time = organization["properties"]["CompanyMetaData"]["Hours"]["text"]

    org_pos = organization["geometry"]["coordinates"]
    distance = round(lonlat_distance(org_pos, list(map(float, ll.split(",")))))

    print(f"Название: {org_name}\nАдресс: {org_address}\nВремя работы: {org_work_time}\nДо него: {distance} метров")
