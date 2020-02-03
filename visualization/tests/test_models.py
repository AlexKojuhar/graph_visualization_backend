from django.test import TestCase
from visualization.models import Node, Link

class NodeTest(TestCase):

    def test_model_fields(self):
        self.assertTrue(hasattr(Node, 'id'))
        self.assertTrue(hasattr(Node, 'name'))

    def test_type_model_fields(self):
        self.assertTrue(
            Node._meta.get_field('id').get_internal_type(),
            'IntegerField'
        )
        self.assertTrue(
            Node._meta.get_field('name').get_internal_type(),
            'CharField'
        )


    def test_string_representation(self):
        node = Node.objects.create(name='Node')
        self.assertEqual(str(node), node.name)

class LinkTest(TestCase):

    def test_model_fields(self):
        self.assertTrue(hasattr(Link, 'id'))
        self.assertTrue(hasattr(Link, 'source'))
        self.assertTrue(hasattr(Link, 'target'))

    def test_type_model_fields(self):
        self.assertTrue(
            Link._meta.get_field('id').get_internal_type(),
            'IntegerField'
        )
        self.assertTrue(
            Link._meta.get_field('source').get_internal_type(),
            'ForeignKey'
        )
        self.assertTrue(
            Link._meta.get_field('target').get_internal_type(),
            'ForeignKey'
        )
