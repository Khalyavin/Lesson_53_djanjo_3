from django.contrib import admin

from catalog.models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category_id', )
    search_fields = ('name', 'description', )
    list_filter = ('category_id', )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', )
    list_filter = ('name', )
