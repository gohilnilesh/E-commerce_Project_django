from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


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

def sign_up(request):

    if request.method == "POST":
        fm = UserCreationForm(request.POST)
    if fm.is_valid():
        fm.save()
       
    else:
      fm = UserCreationForm()
    return render(request,'signup.html',{'form':fm})

