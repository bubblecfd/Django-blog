from django.contrib import admin
from blogging.models import Post, Category

# and a new admin registration

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]

class CategoryAdmin(admin.ModelAdmin):
    #inlines = [
    #    CategoryInline,
    #]
    exclude = ('posts',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
