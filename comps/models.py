from django.db import models
from core.models import Menu, Category, CustomPage
from utils.files import content_file_name
from django.utils.translation import gettext_lazy as _

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
    short_code = models.CharField(_('الكود المختصر'), max_length=20, unique=True)
    hash = models.CharField(_('id'),max_length=200,null=True,blank=True)

    class Meta:
        verbose_name = _('كود مختصر')
        verbose_name_plural = _('الكودات المختصرة')

    def __str__(self):
        return self.short_code


class Section(ShortCode):
    title = models.CharField(_('العنوان'), max_length=200)
    title_e = models.CharField(_('العنوان $'), max_length=200)
    desc = models.TextField(_('الوصف'), )
    desc_e = models.TextField(_('الوصف $'), )
    image = models.FileField(_('الصورة'), upload_to=content_file_name)
    image_e = models.FileField(_('الصورة $'), upload_to=content_file_name)
    is_reflected = models.BooleanField(_('مقلوب؟'), default=False)
    is_background = models.BooleanField(_('بخلفية؟'), default=False)
    button_link = models.URLField(_('رابط الزر'), )
    button_text = models.CharField(_('نص الزر'), max_length=200)
    button_text_e = models.CharField(_('نص الزر $'), max_length=200)
    effect = models.CharField(_('التآثير'), max_length=200, choices=ANIMATIONS, default="fade-up")
    effect_duration = models.IntegerField(_('مدة التآثير'), default=1000)

    class Meta:
        verbose_name = _('قسم')
        verbose_name_plural = _('الاقسام')

    def __str__(self):
        return self.title


class Header(ShortCode):
    logo = models.ImageField(_('اللوكو'), upload_to=content_file_name)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name=_('القائمة'), )

    email = models.CharField(_('البريد الالكتروني'), max_length=200)
    phone = models.CharField(_('الهاتف'), max_length=200)
    work_time = models.CharField(_('ساعات الهمل'), max_length=200)

    is_button = models.BooleanField(_('يحتوي زر؟'), default=False)
    button_link = models.URLField(_('رابط الزر'), )
    button_text = models.CharField(_('نص الزر'), max_length=200)
    button_text_e = models.CharField(_('نص الزر $'), max_length=200)
    effect = models.CharField(_('التآثير'), max_length=200, choices=ANIMATIONS, default="fade-up")
    effect_duration = models.IntegerField(_('مدة التآثير'), default=1000)
    is_default = models.BooleanField(_('افتراضي'), default=True)

    class Meta:
        verbose_name = _('رآس الصفحة')
        verbose_name_plural = _('رؤوس الصفحات')

    def __str__(self):
        return self.short_code


class Footer(ShortCode):
    logo = models.ImageField(_('اللوكو'), upload_to=content_file_name)
    logo_e = models.ImageField(_('اللوكو $'), upload_to=content_file_name)
    title1 = models.CharField(_('العنوان ١'), max_length=200)
    title_e1 = models.CharField(_('العنوان ١ $'), max_length=200)

    menu1 = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu1', verbose_name=_('القائمة ١'), )
    title2 = models.CharField(_('العنوان ٢'), max_length=200)
    title_e2 = models.CharField(_('العنوان ٢ $'), max_length=200)
    email = models.CharField(_('البريد الالكتروني'), max_length=200)
    phone = models.CharField(_('الهاتف'), max_length=200)
    work_time = models.CharField(_('ساعات الهمل'), max_length=200)

    desc = models.TextField(_('الوصف'), )
    desc_e = models.TextField(_('الوصف $'), )
    effect = models.CharField(_('التآثير'), max_length=200, choices=ANIMATIONS, default="fade-up")
    effect_duration = models.IntegerField(_('مدة التآثير'), default=1000)
    is_default = models.BooleanField(_('افتراضي ؟'), default=True)

    class Meta:
        verbose_name = _('ذيل الصفحة')
        verbose_name_plural = _('اذيال الصفحات')

    def __str__(self):
        return self.short_code


class BlogComp(ShortCode):
    title = models.CharField(_('العنوان'), max_length=200)
    title_e = models.CharField(_('العنوان ١'), max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('القسم'), )
    is_simple = models.BooleanField(_('بسيط؟'), default=True)
    count = models.IntegerField(_('العدد'), default=4)
    button_link = models.URLField(_('رابط الزر'), )
    button_text = models.CharField(_('نص الزر'), max_length=200)
    button_text_e = models.CharField(_('نص الزر $'), max_length=200)
    effect = models.CharField(_('التآثير'), max_length=200, choices=ANIMATIONS, default="fade-up")
    effect_duration = models.IntegerField(_('مدة التآثير'), default=1000)

    class Meta:
        verbose_name = _('مدونة')
        verbose_name_plural = _('المدونات')

    def __str__(self):
        return self.title


class ProjectComp(ShortCode):
    title = models.CharField(_('العنوان'), max_length=200)
    title_e = models.CharField(_('العنوان $'), max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('القسم'), )
    is_simple = models.BooleanField(_('بسيط'), default=True)
    count = models.IntegerField(_('العدد'), default=4)
    button_link = models.URLField(_('رابط الزر'), )
    button_text = models.CharField(_('نص الزر'), max_length=200)
    button_text_e = models.CharField(_('نص الزر $'), max_length=200)
    effect = models.CharField(_('التآثير'), max_length=200, choices=ANIMATIONS, default="fade-up")
    effect_duration = models.IntegerField(_('مدة التآثير'), default=1000)

    class Meta:
        verbose_name = _('المشروع')
        verbose_name_plural = _('المشاريع')

    def __str__(self):
        return self.title


class Spacer(ShortCode):
    height = models.CharField(_('الارتفاع'), max_length=200)
    effect = models.CharField(_('التآثير'), max_length=200, choices=ANIMATIONS, default="fade-up")
    effect_duration = models.IntegerField(_('مدة التآثير'), default=1000)

    class Meta:
        verbose_name = _('مسافة')
        verbose_name_plural = _('المسافات')

    def __str__(self):
        return self.height


class Masonry(ShortCode):
    title = models.CharField(_('العنوان'), max_length=200)
    title_e = models.CharField(_('العنوان $'), max_length=200)

    title1 = models.CharField(_('العنوان ١'), max_length=200)
    title1_e = models.CharField(_('العنوان ١ $'), max_length=200)
    image1 = models.ImageField(_('الصورة ١'), upload_to=content_file_name)
    description1 = models.TextField(_('الوصف ١'), max_length=220)
    description1_e = models.TextField(_('الوصف ١ $'), max_length=220)
    icon1 = models.CharField(_('الايقونة ١'), max_length=200)

    title2 = models.CharField(_('العنوان ٢'), max_length=200)
    title2_e = models.CharField(_('العنوان ٢ $'), max_length=200)
    image2 = models.ImageField(_('الصورة ٢'), upload_to=content_file_name)
    description2 = models.TextField(_('الوصف ٢'), max_length=220 )
    description2_e = models.TextField(_('الوصف ٢ $'),  max_length=220)
    icon2 = models.CharField(_('الايقونة ٢'), max_length=200)

    title3 = models.CharField(_('العنوان ٣'), max_length=200)
    title3_e = models.CharField(_('العنوان ٣ $'), max_length=200)
    image3 = models.ImageField(_('الصورة ٣'), upload_to=content_file_name)
    description3 = models.TextField(_('الوصف ٣'), max_length=220 )
    description3_e = models.TextField(_('الوصف ٣ $'), max_length=220 )
    icon3 = models.CharField(_('الايقونة ٣'), max_length=200)

    effect = models.CharField(_('التآثير'), max_length=200, choices=ANIMATIONS, default="fade-up")
    effect_duration = models.IntegerField(_('مدة التآثير'), default=1000)

    class Meta:
        verbose_name = _('متدرج')
        verbose_name_plural = _('المتدرجات')

    def __str__(self):
        return self.title


class Counter(ShortCode):
    title1 = models.CharField(_('العنوان ١'), max_length=200)
    title1_e = models.CharField(_('العنوان ١ $'), max_length=200)
    number1 = models.CharField(_('رقم ١'), max_length=200)

    title2 = models.CharField(_('العنوان ٢'), max_length=200)
    title2_e = models.CharField(_('العنوان ٢ $'), max_length=200)
    number2 = models.CharField(_('رقم ٢'), max_length=200)

    title3 = models.CharField(_('العنوان ٣'), max_length=200)
    title3_e = models.CharField(_('العنوان ٣ $'), max_length=200)
    number3 = models.CharField(_('رقم ٣'), max_length=200)

    title4 = models.CharField(_('العنوان ٤'), max_length=200)
    title4_e = models.CharField(_('العنوان ٤ $'), max_length=200)
    number4 = models.CharField(_('رقم ٤'), max_length=200)
    effect = models.CharField(_('التآثير'), max_length=200, choices=ANIMATIONS, default="fade-up")
    effect_duration = models.IntegerField(_('مدة التآثير'), default=1000)

    class Meta:
        verbose_name = _('عداد')
        verbose_name_plural = _('العدادات')

    def __str__(self):
        return self.short_code


class Contact(ShortCode):
    phone1 = models.CharField(_('هاتف ١'), max_length=200)
    phone2 = models.CharField(_('هاتف ٢'), max_length=200)
    email = models.CharField(_('بريد'), max_length=200)
    location = models.CharField(_('العنوان'), max_length=200)
    location_e = models.CharField(_('عنوان $'), max_length=200)
    facebook = models.CharField(_('فيسبوك'), max_length=200)
    instagram = models.CharField(_('انستا'), max_length=200)
    whatsapp = models.CharField(_('واتس اب'), max_length=200)
    telegram = models.CharField(_('تليغرام'), max_length=200)

    dest_email = models.CharField(_('البريد المراد الارسال اليه'), max_length=200)
    effect = models.CharField(_('التآثير'), max_length=200, choices=ANIMATIONS, default="fade-up")
    effect_duration = models.IntegerField(_('مدة التآثير'), default=1000)

    class Meta:
        verbose_name = _('تواصل')
        verbose_name_plural = _('فورمات التواصل')

    def __str__(self):
        return self.short_code
