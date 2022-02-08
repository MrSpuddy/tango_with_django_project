from django.db import models

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
