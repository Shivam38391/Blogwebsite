from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE) #one author hav only one profile
    profile_image  = models.ImageField(upload_to= "image/", blank=True , null=True)
    bio = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200,unique=True)
    
    def save(self,*args, **kwargs ):
        if not self.id:
            self.slug = slugify(self.user.username)
        return super(Profile, self).save(*args, **kwargs)


    def __str__(self):
        return self.user.username







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
    is_featured = models.BooleanField(default=False)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    

    def __str__(self):
        return self.title
    
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
        
        
        

class Comments(models.Model):
    name = models.CharField( max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    website = models.CharField(max_length=150, blank=True)
    email = models.EmailField( max_length=254)
    post = models.ForeignKey(Post,on_delete=models.CASCADE) #many to one relationships
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # null = true ,because without login anyone can comment , to keep a track oflogged in author 
    parent = models.ForeignKey("self", on_delete=models.DO_NOTHING, null=True,blank=True, related_name='replies')

    def __str__(self):
        return f'{self.name} and {self.content}'

        
        
class Subscribe(models.Model): 
    email = models.EmailField( max_length=254)
    date = models.DateField( auto_now=True)

    def __str__(self):
        return self.email

