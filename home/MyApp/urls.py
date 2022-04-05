from django.urls import path
from MyApp import views


app_name = 'MyApp'
urlpatterns = [
    path('',views.home,name = 'home'),
    path('shop/',views.shop,name = 'shop'),
    path('about/',views.about,name = 'about'),
    path('contact/',views.contact,name = 'contact'),
    path('blog/',views.blog,name = 'blog'),
    path('blog/blog-details/',views.blog_details,name = 'blog-details'),
    path('checkout/',views.checkout,name = 'checkout'),
    path('shop/shopping-cart/',views.shopping_cart,name = 'shopping-cart'),
    path('shop/single-product/',views.single_product,name = 'single-product'),
    path('wishlist/',views.wishlist,name = 'wishlist'),
    path('my-account/',views.my_account,name = 'my-account'),
   

]
