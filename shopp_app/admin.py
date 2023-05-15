from itertools import product
from unicodedata import name
from django.contrib import admin
from .models import Brand, Catagory, Catagory_Type, Catagory_Type2,Product, Productgallery, units
import admin_thumbnails

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Catagory,CategoryAdmin)

# Register your models here.
@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model=Productgallery
    extra=1




class ServiceAdmin(admin.ModelAdmin):
    exclude = ('percentage',)
    list_display=['name','stock','selling_price']
    inlines=[ProductGalleryInline]
     
    def save_model(self, request, obj, form, change):
        percentage =obj.percentage
        percentage=100-((obj.selling_price/obj.original_price)*100)
        
        obj.percentage=percentage
        super().save_model(request, obj, form, change)
admin.site.register(Product,ServiceAdmin)




class ProductAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Catagory_Type,ProductAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Catagory_Type2,ProductAdmin)

admin.site.register(Brand)
admin.site.register(units)


