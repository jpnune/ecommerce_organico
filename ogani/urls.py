from django.urls import path

from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('artigos/', ArtigosView.as_view() , name='artigos'),
    path('blog-details/', BlogDetailsView.as_view() , name='blog_details'),
    path('checkout/', CheckoutView.as_view() , name='checkout'),
    path('contact/', ContactView.as_view() , name='contact'),
    path('main/', MainView.as_view() , name='shop_details'),
    path('produtos/', ProdutosView.as_view() , name='produtos'),
    path('shoping-cart/', ShopingCartView.as_view() , name='shoping_cart'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

