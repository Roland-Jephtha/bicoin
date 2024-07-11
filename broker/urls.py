from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .forms import CustomSetPasswordForm, CustomPasswordResetForm


urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),

    path('contact', contact, name='contact'),
    path('faq', faq, name='faq'),
    path('terms', terms, name='terms'),
    path('assets', assets, name='assets'),

    # path('forgotPassword/', forgotPassword, name="forgotPassword"),
    # path('resetpassword_validate/<uidb64>/<token>/', resetpassword_validate, name="resetpassword_validate"),
    # path('resetPassword/',resetPassword, name="resetPassword"),
    
]
