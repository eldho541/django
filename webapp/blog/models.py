from django.db import models

# Create your models here.
from django.db.models.signals import pre_save,post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver


def upload_location(instance,filename):
    file_path = 'blog/{author_id}/{title}--{filename}'.format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename)

    return file_path

class BlogPost(models.Model):
    titel = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(max_length=500,null= False, blank=False)
    image=models.ImageField(upload_location=upload_location, null=False, blank=False)
    date_published =models.DateField(auto_now_add=True, verbose_name='date published')
    date_updated =models.DateField(auto_now=True, verbose_name="date updated")
    author =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    slug =models.SlugField(blank=True, unique= True)

@reciver(post_delete,sender=BlogPost)