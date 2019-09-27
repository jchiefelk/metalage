from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'history', views.get_data)
]