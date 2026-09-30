from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "short_body",
        "author",
    ]

    @admin.display(description="Body")
    def short_body(self, obj):
        return obj.body[:50]


admin.site.register(Article, ArticleAdmin)
