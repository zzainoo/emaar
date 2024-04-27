from django.contrib import admin
from .models import *
from comps.models import ShortCode


# class ShortCodeInline(admin.TabularInline):
#     model = ShortCode
#
#
# class CustomPageAdmin(admin.ModelAdmin):
#     inlines = [ShortCodeInline]


admin.site.register(Site)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Post)
admin.site.register(CustomPage)
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(LinkModel)
admin.site.register(ShortCode)
