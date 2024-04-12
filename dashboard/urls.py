
from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name="index-page"),
    path('login/',login,name="login-page"),
    path('logout/',logout,name="logout-page"),
    path('contact/',contact,name="contact-page"),
    path('user/',users,name="user-page"),
    path('user/<int:email_id>/',delete_user,name="delete-function"),
    path('Add-Products/',AddProducts,name="Products-Page"),
    path('delete-product/<int:product_id>/',DeleteProduct,name="delete-product"),
    path('Add-Category/',AddCategory,name="Add-Category"),
    path('delete-category/<int:category_id>/',delete_category,name="Delete-Category")
]





