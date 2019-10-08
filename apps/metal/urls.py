from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from django.urls import path
from . import views


urlpatterns = [
    url(r'history', views.get_data),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]