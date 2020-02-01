from .models import Node, Link
from rest_framework import viewsets
from .serializers import NodeSerializer, LinkSerializer


class NodeViewSet(viewsets.ModelViewSet):

    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class LinkViewSet(viewsets.ModelViewSet):
    
    queryset = Link.objects.all()
    serializer_class = LinkSerializer