from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('post/<slug:slug>', views.post_page, name='post'),
    path('tag/<slug:slug>', views.tag_page, name='tag_page'),
    
    path('', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)