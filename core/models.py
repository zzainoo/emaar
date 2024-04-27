from django.db import models
from utils.files import content_file_name


class Site(models.Model):
    name = models.CharField(max_length=200)
    logo = models.FileField(upload_to=content_file_name)
    font = models.FileField(upload_to=content_file_name)
    p_color = models.CharField(max_length=200)
    s_color = models.CharField(max_length=200)
    subdomain = models.CharField(max_length=200, unique=True)
    is_homepage = models.BooleanField(default=False)


class LinkModel(models.Model):
    link = models.CharField(max_length=255)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('link', 'site')


class Category(models.Model):
    name = models.CharField(max_length=200)


class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    image = models.FileField(upload_to=content_file_name)
    name = models.CharField(max_length=200)
    name_e = models.CharField(max_length=200)
    desc = models.TextField()
    desc_e = models.TextField()


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    image = models.FileField(upload_to=content_file_name)
    name = models.CharField(max_length=200)
    name_e = models.CharField(max_length=200)
    desc = models.TextField()
    desc_e = models.TextField()


class CustomPage(LinkModel):
    name = models.CharField(max_length=200)
    name_e = models.CharField(max_length=200)
    desc = models.TextField()
    desc_e = models.TextField()
    is_home = models.BooleanField(default=False)
    short_codes = models.TextField(blank=True)


ListPage_Type = (
    ("project", "مشروع"),
    ("post", "مدونة"),
)


class Menu(models.Model):
    name = models.CharField(max_length=200)


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    name_e = models.CharField(max_length=200)
    link = models.ForeignKey(LinkModel, on_delete=models.CASCADE)
