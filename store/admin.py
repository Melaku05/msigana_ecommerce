from django.contrib import admin
from store.models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {'product_slug': ('product_name',)}
    list_display = ('product_name', 'product_stock', 'category',
                    'product_created_date', 'product_modified_date', 'product_is_available',)


admin.site.register(Product, ProductAdmin)