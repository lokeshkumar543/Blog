from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=255,blank=True)
    description=models.CharField(max_length=255,blank=True)
    image=models.ImageField(upload_to='images/',default=None,blank=True,null=True)
    author_name=models.CharField(max_length=255,blank=True)
    author_email=models.EmailField()
    author_phone=models.CharField(max_length=15,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=True)

    def __str__(self):
        return self.author_name
