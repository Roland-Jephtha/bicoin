from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth import authenticate, login as log, logout
from django.contrib import messages
from .forms import *
from django.shortcuts import get_object_or_404

# from django.contrib.sites.models import Site

from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.views import PasswordResetView








def home(request):
    base_url = request.build_absolute_uri('/')

    context = {
      
        'url': base_url,


    }  
    return render(request, 'index.html', context)


def about(request):
    base_url = request.build_absolute_uri('/')

    context = {
      
        'url': base_url,
    }  
    return render(request, 'About.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        contacts = Contact(
            name = name,
            email = email,
            message = message,
            number = subject,
        )
        contacts.save()
        messages.success(request, 'We received your Message we will get back to you soon!!!')
    contact = Contact.objects.all() 
 
        
    return render(request, 'Contact.html')



def faq(request):
    return render(request, 'faq.html')


def sitemap(request):
    return render(request, 'sitemap.xml')



def terms(request):
    return render(request, 'Terms.html')

def assets(request):
    return render(request, 'Assets.html')

 

