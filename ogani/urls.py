from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/', BlogView.as_view() , name='blog'),
    path('blog-details/', BlogDetailsView.as_view() , name='blog_details'),
    path('checkout/', CheckoutView.as_view() , name='checkout'),
    path('contact/', ContactView.as_view() , name='contact'),
    path('main/', MainView.as_view() , name='shop_details'),
    path('shop-grid/', ShopDetailsView.as_view() , name='shop_grid'),
    path('shoping-cart/', ShopingCartView.as_view() , name='shoping_cart'),

    #path('blog/', blog , name='blog'),
    #path('blog-details/', blog_details, name='blog_details'),
    #path('checkout/', checkout, name='checkout'),
    #path('checkout/', contact, name='contact'),
    #path('contact/', main, name='main'),
    #path('main/', shop_details, name='shop_details'),
    #path('shop-grid/', shop_grid, name='shop_grid'),
    #path('shoping-cart/', shoping_cart, name='shoping_cart'),

]
