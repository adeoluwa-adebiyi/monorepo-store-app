from django.contrib import admin
from .models import Product, ProductBrand, ProductCategory, ParentCategory, ProductProductListing, ProductListing, ParentCategoryProductListing

# Register your models here.


admin.site.register(Product)
admin.site.register(ProductBrand)
admin.site.register(ProductCategory)
admin.site.register(ParentCategory)
admin.site.register(ProductProductListing)
admin.site.register(ProductListing)
admin.site.register(ParentCategoryProductListing)
