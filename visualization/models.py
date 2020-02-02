from django.db import models

class Node(models.Model):
    name = models.CharField(unique=True, max_length=225)

    def __str__(self):
        return self.name

class Link(models.Model):
    source = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='source')
    target = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='target')
