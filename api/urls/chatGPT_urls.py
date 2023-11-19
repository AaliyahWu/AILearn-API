from django.urls import path

from api.views.chatGPT_views import *

app_name = 'chatGPT'

urlpatterns = [
    path('chatbot/', chatbot),
]