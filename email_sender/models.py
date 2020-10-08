from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):
    image = models.ImageField(upload_to='',blank=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='created',null=True)
    des = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('email:detail',args=[self.slug])



