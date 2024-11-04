from django.db import models

class StickerDesign(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploads/image/')

    def __str__(self):
        return self.title


# Create your models here.
class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/stickers/')
    
    def __str__(self):
        return self.title