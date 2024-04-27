from django.contrib import admin
from django.urls import path,include
from core.views import main,list_projects,list_posts
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:page>', main),
    path('', main),
    path('projects/<int:pk>', list_projects),
    path('posts/<int:pk>', list_posts),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)