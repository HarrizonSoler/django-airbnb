from django.urls.conf import path
from . import views


app_name = 'products'
urlpatterns = [
    path('', views.list, name="list"),
]