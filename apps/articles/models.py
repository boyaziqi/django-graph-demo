from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

class Article(models.Model):
    """
    文章 model
    """
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='articles')
