from django.db import models


class Todo(models.Model):
    category_id = models.IntegerField()
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.text[0:10] + '...'

class Category(models.Model):
    name = models.CharField(max_length=300)
