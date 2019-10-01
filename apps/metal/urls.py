from django.conf.urls import url
from graphene_django.views import GraphQLView
from django.urls import path
from . import views


urlpatterns = [
    url(r'history', views.get_data),
    path('graphql', GraphQLView.as_view(graphiql=True)),
]