from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):

    name = models.CharField(max_length=128, unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self): 
        return self.name

    # IntegerField = Store Integers
    views = models.IntegerField(default=0)

    # IntegerField = Store Integers
    likes = models.IntegerField(default=0)

    # SlugField = For URL Correction
    slug = models.SlugField(unique=True)

    # Alters URL to Remove Spaces, and Make it Readable
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) 
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Page(models.Model):
    # Foreign Key from Category above, delete associated pages if category is deleted
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    
    # URLField = Text Field for URLs
    url = models.URLField()
    # IntegerField = Store Integers
    views = models.IntegerField(default=0)

    # Good practice for debugging
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance. 
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
