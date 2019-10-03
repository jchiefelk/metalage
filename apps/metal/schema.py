import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Metal
from .models import ElementTraceAssay


class MetalObjects(DjangoObjectType):
    class Meta:
        model = Metal
        filter_fields = ['country']
        interfaces = (graphene.relay.Node, )


class ElementTraceAssayObjects(DjangoObjectType):
    class Meta:
        model = ElementTraceAssay
        filter_fields = ['analysis_method', 'id']
        interfaces = (graphene.relay.Node, )


class Query(graphene.ObjectType):
    metal = graphene.relay.Node.Field(MetalObjects)
    all_metal = DjangoFilterConnectionField(MetalObjects)
    elements = graphene.relay.Node.Field(ElementTraceAssayObjects)
    all_elements = DjangoFilterConnectionField(ElementTraceAssayObjects) 


schema = graphene.Schema(query=Query)
