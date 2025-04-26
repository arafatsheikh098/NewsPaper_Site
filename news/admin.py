from django.contrib import admin
from .models import Article, Category,Comment

admin.site.register(Article)
admin.site.register(Category)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'text', 'created_at')
    readonly_fields = ('article', 'user', 'text', 'created_at')  # Make fields read-only

    def has_change_permission(self, request, obj=None):
        return False 