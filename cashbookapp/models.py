from email.mime import image
from pyexpat import model
from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
from django.contrib.auth.models import User

class Cashbook(models.Model):
    title = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('data published')
    content = models.TextField()
    email = models.EmailField(max_length=254, blank=True)
    url = models.URLField(max_length=200, blank= True)
    created_at = models.DateTimeField(default= datetime.now, blank=True)
    image = models.ImageField(upload_to = 'image/', blank = True)


    def __str__(self):
        return self.title

    def clean(self):
        title = self.title
        if title =="":
            raise ValidationError("글을 작성해주세요")
        return super(Cashbook,self).clean()
    
def clean_content(self):
    instance = getattr(self, 'instance', None)
    if instance and instance.pk:
        return instance.content
    else:
        return self.cleaned_data['email']



