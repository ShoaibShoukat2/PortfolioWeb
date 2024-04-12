from django.contrib import admin

# Register your models here.

# in admin.py

from django.contrib import admin
from .models import AdminProfile,Email,Category,Products

class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    def username(self, obj):
        return obj.user.username

    def email(self, obj):
        return obj.user.email


class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email', 'text')
    search_fields = ('subject', 'email')

admin.site.register(Email, EmailAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Products)
class ProductsModel(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'image', 'description']
    list_filter = ['category']
    search_fields = ['title', 'description']
 
    
    
    
admin.site.register(AdminProfile, AdminProfileAdmin)
