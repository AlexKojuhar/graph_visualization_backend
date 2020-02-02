from .models import Node, Link
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class NodeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=225, validators=[UniqueValidator(queryset=Node.objects.all())])

    class Meta:
        model = Node
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(LinkSerializer, self).to_representation(instance)
        rep['source'] = instance.source.name
        rep['target'] = instance.target.name
        return rep
