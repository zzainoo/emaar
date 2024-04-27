from django.db import models
from core.models import Menu, Category, CustomPage
from utils.files import content_file_name

# section - header - footer - blogshort - projectsshort - spacer - Masonry Layout(متدرج) - counter
ANIMATIONS = (
    ("fade-up", "fade-up"),
    ("fade-down", "fade-down"),
    ("flip-left", "flip-left"),
    ("flip-right", "flip-right"),
    ("flip-up", "flip-up"),
    ("flip-down", "flip-down"),
    ("zoom-in", "zoom-in"),
    ("zoom-out", "zoom-out"),
)


class ShortCode(models.Model):
    short_code = models.CharField(max_length=20, unique=True)


class Section(ShortCode):
    title = models.CharField(max_length=200)
    title_e = models.CharField(max_length=200)
    desc = models.TextField()
    desc_e = models.TextField()
    image = models.FileField(upload_to=content_file_name)
    image_e = models.FileField(upload_to=content_file_name)
    is_reflected = models.BooleanField(default=False)
    is_background = models.BooleanField(default=False)
    button_link = models.URLField()
    button_text = models.CharField(max_length=200)
    button_text_e = models.CharField(max_length=200)
    effect = models.CharField(max_length=200, choices=ANIMATIONS, default="fade-up")
    effect_duration = models.IntegerField(default=1000)


class Header(ShortCode):
    logo = models.ImageField(upload_to=content_file_name)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    work_time = models.CharField(max_length=200)

    is_button = models.BooleanField(default=False)
    button_link = models.URLField()
    button_text = models.CharField(max_length=200)
    button_text_e = models.CharField(max_length=200)
    effect = models.CharField(max_length=200, choices=ANIMATIONS, default="fade-up")
    effect_duration = models.IntegerField(default=1000)
    is_default = models.BooleanField(default=True)



class Footer(ShortCode):
    logo = models.ImageField()
    logo_e = models.ImageField()
    title1 = models.CharField(max_length=200)
    title_e1 = models.CharField(max_length=200)
    menu1 = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu1')
    title2 = models.CharField(max_length=200)
    title_e2 = models.CharField(max_length=200)
    menu2 = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu2')
    title3 = models.CharField(max_length=200)
    title_e3 = models.CharField(max_length=200)
    menu3 = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu3')
    desc = models.TextField()
    desc_e = models.TextField()
    effect = models.CharField(max_length=200, choices=ANIMATIONS, default="fade-up")
    effect_duration = models.IntegerField(default=1000)
    is_default = models.BooleanField(default=True)



class BlogComp(ShortCode):
    title = models.CharField(max_length=200)
    title_e = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_simple = models.BooleanField(default=True)
    count = models.IntegerField(default=4)
    button_link = models.URLField()
    button_text = models.CharField(max_length=200)
    button_text_e = models.CharField(max_length=200)
    effect = models.CharField(max_length=200, choices=ANIMATIONS, default="fade-up")
    effect_duration = models.IntegerField(default=1000)


class ProjectComp(ShortCode):
    title = models.CharField(max_length=200)
    title_e = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_simple = models.BooleanField(default=True)
    count = models.IntegerField(default=4)
    button_link = models.URLField()
    button_text = models.CharField(max_length=200)
    button_text_e = models.CharField(max_length=200)
    effect = models.CharField(max_length=200, choices=ANIMATIONS, default="fade-up")
    effect_duration = models.IntegerField(default=1000)


class Spacer(ShortCode):
    height = models.CharField(max_length=200)
    effect = models.CharField(max_length=200, choices=ANIMATIONS, default="fade-up")
    effect_duration = models.IntegerField(default=1000)


class Masonry(ShortCode):
    title = models.CharField(max_length=200)
    title_e = models.CharField(max_length=200)

    title1 = models.CharField(max_length=200)
    image1 = models.ImageField()
    description1 = models.TextField()
    icon1 = models.CharField(max_length=200)

    title2 = models.CharField(max_length=200)
    image2 = models.ImageField()
    description2 = models.TextField()
    icon2 = models.CharField(max_length=200)

    title3 = models.CharField(max_length=200)
    image3 = models.ImageField()
    description3 = models.TextField()
    icon3 = models.CharField(max_length=200)

    effect = models.CharField(max_length=200, choices=ANIMATIONS, default="fade-up")
    effect_duration = models.IntegerField(default=1000)


class Counter(ShortCode):
    title1 = models.CharField(max_length=200)
    title1_e = models.CharField(max_length=200)
    number1 = models.CharField(max_length=200)

    title2 = models.CharField(max_length=200)
    title2_e = models.CharField(max_length=200)
    number2 = models.CharField(max_length=200)

    title3 = models.CharField(max_length=200)
    title3_e = models.CharField(max_length=200)
    number3 = models.CharField(max_length=200)

    title4 = models.CharField(max_length=200)
    title4_e = models.CharField(max_length=200)
    number4 = models.CharField(max_length=200)
    effect = models.CharField(max_length=200, choices=ANIMATIONS, default="fade-up")
    effect_duration = models.IntegerField(default=1000)


class Contact(ShortCode):
    phone1 = models.CharField(max_length=200)
    phone2 = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    location_e = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    whatsapp = models.CharField(max_length=200)
    telegram = models.CharField(max_length=200)

    dest_email = models.CharField(max_length=200)
    effect = models.CharField(max_length=200, choices=ANIMATIONS, default="fade-up")
    effect_duration = models.IntegerField(default=1000)