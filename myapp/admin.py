from django.contrib import admin
from .models import Post, Tag ,Comments , Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comments)
admin.site.register(Profile)
