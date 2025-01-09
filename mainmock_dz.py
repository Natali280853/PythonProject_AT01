# **Функция `get_random_cat_image`**:
#    - Выполняет GET-запрос к TheCatAPI.
#    - Если статус-код ответа равен 200, функция извлекает URL изображения из полученного JSON и возвращает его.
#    - Если статус-код не равен 200 или данные пустые, функция возвращает `None`.
import requests

def get_random_cat_image():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    if response.status_code == 200:
        data = response.json()
        return data[0]['url'] if data else None
    return None
