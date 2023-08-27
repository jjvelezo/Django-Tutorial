from django.urls import path
from .views import HomePageView, AboutPageView, ProductIndexView, ProductShowView,  ProductCreateView, Contact, CartView, CartRemoveAllView, ImageViewFactory, signupaccount, logoutaccount, loginaccount, ImageViewNoDI
from .utils import ImageLocalStorage
	
    
urlpatterns = [
	path("", HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('templates/products/<str:id>', ProductShowView.as_view(), name='show'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('contact/', Contact.as_view(), name='contact'),
    path('product-created/', ProductCreateView.as_view(), name='product-created'),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
    path('image/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'),
    path('image/save', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'),
    path('signupaccount/', signupaccount, name='signupaccount'),
    path('logout/', logoutaccount, name='logoutaccount'),
    path('login/', loginaccount, name='loginaccount'),
    path('imagenotdi/', ImageViewNoDI.as_view(), name='imagenodi_index'),
    path('image/save', ImageViewNoDI.as_view(), name='imagenodi_save'),




	]
