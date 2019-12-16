import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Metal
from .models import Ore
from .models import ElementTraceAssay
from .models import IsotopeTraceAssay


class OreObjects(DjangoObjectType):
    class Meta:
        model = Ore
        filter_fields = ['country', 'site', 'museum_number', 'source', 'description']
        interfaces = (graphene.relay.Node, )


class MetalObjects(DjangoObjectType):
    class Meta:
        model = Metal
        filter_fields = ['country', 'site', 'museum_number', 'source', 'description']
        interfaces = (graphene.relay.Node, )


class ElementTraceAssayObjects(DjangoObjectType):
    class Meta:
        model = ElementTraceAssay
        filter_fields = ['analysis_method', 'id']
        interfaces = (graphene.relay.Node, )


class IsotopeTraceAssayObjects(DjangoObjectType):
    class Meta:
        model = IsotopeTraceAssay
        filter_fields = ['analysis_method', 'id']
        interfaces = (graphene.relay.Node, )


class Query(graphene.ObjectType):
    metal = graphene.relay.Node.Field(MetalObjects)
    all_metal = DjangoFilterConnectionField(MetalObjects)
    ore = graphene.relay.Node.Field(OreObjects)
    all_ore = DjangoFilterConnectionField(OreObjects)
    elements = graphene.relay.Node.Field(ElementTraceAssayObjects)
    all_elements = DjangoFilterConnectionField(ElementTraceAssayObjects)
    all_isotopes = DjangoFilterConnectionField(IsotopeTraceAssayObjects)

schema = graphene.Schema(query=Query)
