from django.shortcuts import render

#for forms
from .models import Contact
from .forms import ContactForm



# Create your views here.
#for Form
# def create_view(request):
#     context = {}

#     form = ContactForm(request.POST or None)
#     if form.is_valid():
#         form.save()

#         context['form'] = form

#         return render(request, 'new_contact.html',context)





#path
def home(request):
    return render(request, 'index.html')

def shop(request):
    return render(request, 'shop.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def checkout(request):
    return render(request, 'checkout.html')

def shopping_cart(request):
    return render(request, 'shopping-cart.html')

def single_product(request):
    return render(request,'single-product.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def my_account(request):
    return render(request, 'my-account.html')

def new_contact(request):
    return render(request,'new_contact.html')