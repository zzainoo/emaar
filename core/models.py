from django.db import models
from utils.files import content_file_name
from django.utils.translation import gettext_lazy as _


class Site(models.Model):
    name = models.CharField(_('الاسم'), max_length=200)
    logo = models.FileField(_('اللوكو'), upload_to=content_file_name)
    font = models.FileField(_('الخط'), upload_to=content_file_name)
    p_color = models.CharField(_('اللون الاساسي'), max_length=200)
    s_color = models.CharField(_('اللون الثانوي'), max_length=200)
    subdomain = models.CharField(_('رابط'), max_length=200, unique=True)
    is_homepage = models.BooleanField(_('رئيسي؟'), default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('الموقع')
        verbose_name_plural = _('المواقع')


class LinkModel(models.Model):
    link = models.CharField(_('الرابط'), max_length=255)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, verbose_name=_('الموقع'), )

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = _('رابط مخصص')
        verbose_name_plural = _('روابط مخصصة')
        unique_together = ('link', 'site')


class Category(models.Model):
    name = models.CharField(_('الاسم'), max_length=200)

    class Meta:
        verbose_name = _('القسم')
        verbose_name_plural = _('الاقسام')

    def __str__(self):
        return self.name


class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('القسم'), )
    site = models.ForeignKey(Site, on_delete=models.CASCADE, verbose_name=_('الموقع'), )
    image = models.FileField(_('الصورة'), upload_to=content_file_name)
    name = models.CharField(_('الاسم'), max_length=200)
    name_e = models.CharField(_('الاسم $'), max_length=200)
    desc = models.TextField(_('الوصف'), )
    desc_e = models.TextField(_('الوصف $'), )

    class Meta:
        verbose_name = _('المشروع')
        verbose_name_plural = _('المشاريع')

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('القسم'), )
    site = models.ForeignKey(Site, on_delete=models.CASCADE, verbose_name=_('الموقع'), )
    image = models.FileField(_('الصورة'), upload_to=content_file_name)
    name = models.CharField(_('الاسم'), max_length=200)
    name_e = models.CharField(_('الاسم $'), max_length=200)
    desc = models.TextField(_('الوصف'), )
    desc_e = models.TextField(_('الوصف $'), )

    class Meta:
        verbose_name = _('المقال')
        verbose_name_plural = _('المقالات')

    def __str__(self):
        return self.name


class CustomPage(LinkModel):
    name = models.CharField(_('الاسم'), max_length=200)
    name_e = models.CharField(_('الاسم $'), max_length=200)
    desc = models.TextField(_('الوصف'), )
    desc_e = models.TextField(_('الوصف $'), )
    is_home = models.BooleanField(_('رئيسي'), default=False)
    short_codes = models.TextField(_('المكونات'), blank=True)

    class Meta:
        verbose_name = _('الصفحة')
        verbose_name_plural = _('الصفحات')

    def __str__(self):
        return self.name


ListPage_Type = (
    ("project", "مشروع"),
    ("post", "مدونة"),
)


class Menu(models.Model):
    name = models.CharField(_('الاسم'), max_length=200)

    class Meta:
        verbose_name = _('القائمة')
        verbose_name_plural = _('القوائم')

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name=_('القائمة'), )
    name = models.CharField(_('الاسم'), max_length=200)
    name_e = models.CharField(_('الاسم $'), max_length=200)
    external = models.BooleanField(_('خارجي؟'),default=False)
    link = models.ForeignKey(LinkModel, on_delete=models.CASCADE, verbose_name=_('الرابط'), )

    class Meta:
        verbose_name = _('عنصر القائمة')
        verbose_name_plural = _('عناصر القوائم')

    def __str__(self):
        return self.name
