from django.shortcuts import render
from twilio.rest import Client
from .forms import ContactForm
from home import settings


# msg = 'MESSAGE HERE'
# account_sid = '*'
# auth_token = '*',
# client = Client(account_sid,auth_token)
# message = client.messages.create(
#     body = msg
#     # from = 'number',
#     # to = '+ 91 je ma moklavu 6 ema',
# )

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            contact_name = form.cleaned_data['name']
            contact_email = form.cleaned_data['email']
            sub = form.cleaned_data['subject']
            content = form.cleaned_data['message']
            # print(contact_name)
            form.save()
            subject = 'Hello ' + contact_name + ' from apparel!'
            message = 'Stay Connected. We would love to hear you!'
            email_from = settings.EMAIL_HOST_1USER
            email_to = [contact_email, ]
            send_mail(subject, message, email_from, email_to)
            messages.success(request, 'Form submitted successfully.')
            return redirect('Home:Home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ContactForm()
    template = 'contact.html'
    return render(request, template, {'form': form})



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

