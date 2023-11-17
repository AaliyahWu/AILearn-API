import requests
from django.http import JsonResponse
import openai
import configparser
def generate_image(request):
    config = configparser.ConfigParser()
    config.read('apikey.ini')
    api_key = config['API_KEYS']['api_key']
    url = "https://api.openai.com/v1/images/generations"

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        'model':'dall-e-3',
        "prompt": "students are in the class, Flat Style",
        "n": 1,
        "size": "1024x1024"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        image_url = response.json()["data"][0]
        return JsonResponse({"image_url": image_url})
    else:
        return JsonResponse({"error": response.json()["error"]["message"]}, status=500)
