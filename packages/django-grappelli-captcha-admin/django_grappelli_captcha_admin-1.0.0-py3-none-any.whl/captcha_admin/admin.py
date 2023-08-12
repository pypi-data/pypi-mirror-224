from django.contrib import admin
from captcha_admin.forms import MultiCaptchaAdminAuthenticationForm

admin.AdminSite.login_form = MultiCaptchaAdminAuthenticationForm
