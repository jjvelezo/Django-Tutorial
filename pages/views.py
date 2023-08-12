from django.shortcuts import render # here by default
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ValidationError



class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV", "price": 599},
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price": 999},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price": 29},
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price": 49}
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] =  "List of products"
        viewData["products"] = Product.products

        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        try:
            product_id = int(id)
            if 1 <= product_id <= len(Product.products):
                viewData = {}
                product = Product.products[product_id - 1]
                viewData["title"] = product["name"] + " - Online Store"
                viewData["subtitle"] = product["name"] + " - Product information"
                viewData["product"] = product
                return render(request, self.template_name, viewData)
            else:
                return HttpResponseRedirect(reverse('home'))  # Redirect to the home page
        except ValueError:
            return HttpResponseRedirect(reverse('home'))  # Redirect to the home page



# Create your views here.


class HomePageView(TemplateView):
 template_name = 'pages/home.html'


class Contact(TemplateView):
 template_name = 'pages/contact.html'



class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Juan Jose Velez Orozco",
        })

        return context


    

class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise ValidationError("Precio debe ser mayor a Cero (0).")
        return price


class ProductCreateView(View):
    template_name = 'products/create.html'
    success_template_name = 'products/product_created.html'  # New template

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            # Save the product or perform any necessary actions
            return render(request, self.success_template_name)  # Render success template
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)
