from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100,unique=True)
    
    def save(self,*args, **kwargs ):
        if not self.id:
            self.slug = slugify(self.name)
        return super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


        

class Post(models.Model): # model for Posts
    
    title = models.CharField( max_length=250)
    content = models.TextField()
    last_update = models.DateTimeField( auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)
    image  = models.ImageField(upload_to= "image/", blank=True , null=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='post')
    view_count = models.IntegerField(null=True, blank=True) # initially new block post created it can be null and also blank while creating post we dont want user to submit counts
    

    def __str__(self):
        return self.title

class Comments(models.Model):
    name = models.CharField( max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    website = models.CharField(max_length=150, blank=True)
    email = models.EmailField( max_length=254)
    
    post = models.ForeignKey(Post,on_delete=models.CASCADE) #many to one relationships
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # null = true ,because without login anyone can comment , to keep a track oflogged in author 

    def __str__(self):
        return f'{self.name} and {self.content}'

        