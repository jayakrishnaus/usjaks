from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    #description = RichTextField(blank=True, null= True)
    description2 = RichTextUploadingField(blank=True, null= True,
     config_name='special',
     external_plugin_resources=[(
         'youtube',
         '/assets/ckeditor/ckeditor/vendor/ckeditor_plugins/youtube/youtube/',
         'plugin.js',
         )],
         )
    description = RichTextUploadingField(blank=True, null= True)
    body = models.TextField(blank=True, null= True)
    order = models.IntegerField(blank= True, null= True)
    slug= models.SlugField(default='', blank=True)
    

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return '%s' % self.title
