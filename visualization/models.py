from django.db import models

class Node(models.Model):
    name = models.CharField(max_length=225)

class Link(models.Model):
    source = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='source')
    target = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='target')
