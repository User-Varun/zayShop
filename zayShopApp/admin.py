
from django.contrib import admin
from zayShopApp.models import Customer , ImageUploader , Product
from zayShopApp.models import ProductImage

class CustomerAdmin(admin.ModelAdmin):list_display=['cname' , 'cadd' , 'email' , 'phone' , 'unm' , 'pw']

admin.site.register(Customer , CustomerAdmin)

class ImgUploaderAdmin(admin.ModelAdmin):list_display=['photo' , 'date']

admin.site.register(ImageUploader , ImgUploaderAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'stock', 'created_at')
    prepopulated_fields = {'slug': ('title',)}



# @admin.register(ImageUploader)
# class ImageUploaderModelAdmin(admin.ModelAdmin): list_display =['photo' , 'date']