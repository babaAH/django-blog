from django.db import models
import uuid
class Article(models.Model):
    description = models.CharField(max_length=100)
    text = models.TextField()
    published_date = models.DateTimeField
    image = models.ImageField(upload_to='models/%Y/%m/%d')
    slug = models.SlugField(unique=True)


    def __str__(self):
        return "".join(self.description)
