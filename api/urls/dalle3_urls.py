from django.urls import path

from api.views.dalle3_views import *


app_name = 'dalle3'

urlpatterns = [
    path('pic/', generate_image),
]