import graphene
from graphene_django import DjangoObjectType
from .models import Metal
from .models import ElementTraceAssay


class MetalObjects(DjangoObjectType):
    class Meta:
        model = Metal

class ElementTraceAssayObjects(DjangoObjectType):
    class Meta:
        model = ElementTraceAssay

class Query(graphene.ObjectType):
    all_metal = graphene.List(MetalObjects)
    all_elements = graphene.List(ElementTraceAssayObjects)
    
    def resolve_all_metal(self, info):
        return Metal.objects.all()
    
    def resolve_all_elements(self, info):
        return ElementTraceAssay.objects.all()

schema = graphene.Schema(query=Query)
