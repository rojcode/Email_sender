from django.contrib import admin

# Register your models here.
from email_sender.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','des','created')
    list_filter = ['created']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title','des')
    date_hierarchy = 'created'
    ordering = ['created']
