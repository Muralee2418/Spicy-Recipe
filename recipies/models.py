from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save  
from django.dispatch import receiver
from .utils import get_link_data

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=60)
    skills=models.TextField()
    profilepic=models.ImageField(upload_to="authorpics")
class Recipie(models.Model):
    title=models.CharField(max_length=60)
    ingredients=models.CharField(max_length=20)
    isveg=models.BooleanField()
    description=models.TextField()
    image=models.ImageField(upload_to="pics")
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
class ScrapRecipie(models.Model):
    recipieurl=models.URLField(max_length=500)
    title=models.CharField(max_length=100,blank=True)
    description=models.TextField(blank=True)
    imageurl=models.URLField(max_length=500,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=('title','description')
    
    def save(self,*args,**kwargs):
        action=kwargs.get('action')
        if action!="update":
            title,des,imagelink=get_link_data(self.recipieurl)
            print(title)
            self.title=title
            self.description=des
            self.imageurl=imagelink
            print("self Data")
            print(self.title+" "+self.description+" "+self.imageurl)       
        super().save(*args,**kwargs) 
    def __str__(self):
        return self.title

class comments(models.Model):
    comment_info=models.TextField()
    comment_date=models.DateField(auto_now_add=True)
    recipie=models.ForeignKey(ScrapRecipie,on_delete=models.CASCADE,null=True,blank=True)
    
class profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    likedrecipies=models.ManyToManyField(ScrapRecipie)
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile.objects.create(user=instance)        

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    def __str__(self):
        return self.user.username
