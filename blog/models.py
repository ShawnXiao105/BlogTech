# -*- coding: utf-8 -*-
from django.db import models
#from markdown import markdown
from django.utils import timezone
from django.conf import settings
import markdown

def markdown_to_html(markdowntext, images):
    #md = markdown.Markdown()
    for image in images:
        image_url = settings.MEDIA_URL + image.image.url
        image_tag = '![%s]' % image.name
        image_replace = '![%s](%s)' % (image.name, image.image.url)
        markdowntext = markdowntext.replace(image_tag, image_replace)
    html = markdown.markdown(markdowntext, extensions=['codehilite(linenums=False)'])
    return html

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='Category Name')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Slug')
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'


class Tag(models.Model):
    tag_name = models.CharField(max_length=20, blank=True, verbose_name='Tag Name')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Tag Creation Time')

    def __unicode__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

class Image(models.Model):
    name = models.CharField(max_length=100, verbose_name='Image Name')
    description = models.CharField(max_length=150, verbose_name='Image Description')
    image = models.ImageField(upload_to='images/%Y/%m/%d')

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    caption = models.CharField(max_length=50, verbose_name='Blog Caption')
    slug = models.SlugField(max_length=50, unique=True,verbose_name='Slug')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Tags Name')
    content = models.TextField(verbose_name='Blog content')
    blog_introduction = models.TextField(verbose_name='Blog Introduction')
    content_preview = models.TextField(verbose_name='Blog Preview')
    publish_time = models.DateTimeField(default=timezone.now(), verbose_name='Blog Publish Time')
    images = models.ManyToManyField(Image, blank=True, verbose_name='Images')
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='Blog Update Time')
    counts = models.IntegerField(default=0, verbose_name='Click Rate')
    category = models.ForeignKey(Category, verbose_name='Category Name')

    def __unicode__(self):
        return '%s %s' %(self.caption, self.publish_time)

    def body_html(self):
        return markdown_to_html(self.content, self.images.all())

    def preview_html(self):
        return markdown_to_html(self.content_preview, self.images.all())

    class Meta:
        get_latest_by = 'publish_time'
        ordering = ['-id']

class ClientInfo(models.Model):
    ip_address = models.CharField(max_length=50, verbose_name='IP Address')
    click_time = models.DateTimeField(auto_now=True, verbose_name='Client Click Time')

    def __unicode__(self):
        return '%s %s' %(self.ip_address, self.click_time)

    class Meta:
        get_latest_by = 'click_time'
        ordering = ['-id']
        verbose_name_plural = verbose_name = 'PV'
