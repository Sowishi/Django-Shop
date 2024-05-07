from django.contrib import admin
from .models import Products, WomenProducts, KidsProducts, MensProducts, Cart
# Register your models here.


admin.site.register(Products)
admin.site.register(WomenProducts)
admin.site.register(KidsProducts)
admin.site.register(MensProducts)
admin.site.register(Cart)