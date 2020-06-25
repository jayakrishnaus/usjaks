from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    First_Name = models.CharField(max_length=255, blank=True, null=True)
    Last_Name= models.CharField(max_length=255, blank=True, null=True)
    Email= models.EmailField(max_length=255, blank=True, null=True)

    title = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(upload_to='pics')
    Subject = models.CharField(max_length=20,  blank=True, null=True) 
    #description = RichTextField(blank=True, null= True)
    description = RichTextUploadingField(blank=True, null= True)
    
    
    

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return '%s' % self.title


class questions(models.Model):
    First_Name = models.CharField(max_length=255, blank=True, null=True)
    Last_Name= models.CharField(max_length=255, blank=True, null=True)
    Email= models.EmailField(max_length=255, blank=True, null=True)
    Subject = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null= True)

    def save(self):
        self.slug = slugify(self.First_Name)
        super(questions, self).save()

    def __str__(self):
        return '%s' % self.First_Name



class answers(models.Model):
    First_Name = models.CharField(max_length=255, blank=True, null=True)
    Last_Name= models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(upload_to='pics')
    Email= models.EmailField(max_length=255, blank=True, null=True)
    Subject = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null= True)
    


    def save(self):
        self.slug = slugify(self.First_Name)
        super(answers, self).save()

    def __str__(self):
        return '%s' % self.First_Name


