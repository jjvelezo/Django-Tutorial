from django.urls import path
from .views import HomePageView, AboutPageView, ProductIndexView, ProductShowView,  ProductCreateView, Contact
	
	
urlpatterns = [
	path("", HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('templates/products/<str:id>', ProductShowView.as_view(), name='show'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('contact/', Contact.as_view(), name='contact')
 

	]
