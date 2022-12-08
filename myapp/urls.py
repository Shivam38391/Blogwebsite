from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# app_name = "my_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>', views.post_page, name='post'),
    path('tag/<slug:slug>', views.tag_page, name='tag_page'),
    path('author/<slug:slug>', views.author_page, name='author_page'),
    path('search/', views.search_post, name='search_post'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)