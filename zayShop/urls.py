"""
URL configuration for zayShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from zayShopApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('' , views.index, name='index'),
    path('index/' , views.index, name='index'),
    # path('index/' , views.index ),
    path('about/' , views.about , name='about'),

    path('contact/' , views.contact , name='contact'),
    path('shopSingle/', views.shopSingle, name='shopSingle'),
    path('shop/', views.shop, name='shop'),
    path('login/' , views.login , name='login'),
    path('regis/' , views.regis , name='regis'),
    path('images/' , views.upload_image, name='upload_image'),
    path('cart/add/', views.add_to_cart, name='cart_add'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='cart_add_product'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    # path(route="delete/<int:image_id>" , view=views.delete_image , name='delete_data'  )
    path('delete/<int:image_id>', views.delete_image, name='delete_data')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
