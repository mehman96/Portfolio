from itertools import count
from django.db import models
from ckeditor.fields import RichTextField




class Counter(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="media/")
    count=models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=225,null=True, blank=True)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="media/")
    job=models.CharField(max_length=128,blank=True,null=True)
    name=models.CharField(max_length=128,null=True,blank=True)
    desc= RichTextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    header=models.CharField(max_length=225, null=True, blank=True)
    date=models.DateField(null=True, blank=True)
    desc= RichTextField(null=True, blank=True)
    link=models.CharField(max_length=128,null=True,blank=True)

    def __str__(self):
        return self.desc
