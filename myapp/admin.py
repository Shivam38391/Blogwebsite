from django.contrib import admin
from .models import Post, Tag ,Comments , Profile

# Register your models here.

class ModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

# admin.site.register(Mode, ModelAdmin)





admin.site.register(Post, ModelAdmin)
admin.site.register(Tag)
admin.site.register(Comments)
admin.site.register(Profile)
