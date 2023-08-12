# django-grappelli-captcha-admin


Easy added captcha to Django administration login page. inherit from a-roomana/django-multi-captcha-admin

---
## Dependency

To use this module you need to install django and one of the captcha engines, which you can install it with easy_install or pip.

---
## Installation

Install:

    pip install django-grappelli-captcha-admin

if you are using python 2 then install version 1.0.0 (*`pip install django-multi-captcha-admin==1.0.0`*)


Add `'multi_captcha_admin'` to your `INSTALLED_APPS` setting before `'django.contrib.admin'` app.

```python
INSTALLED_APPS = [
	...
	'captcha_admin',
	'django.contrib.admin',
	...
]

CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_TIMEOUT = 1
CAPTCHA_GET_FROM_POOL_TIMEOUT = 0
CAPTCHA_BACKGROUND_COLOR = '#bbaaaa'
```

### Engines

We support three famous engines to render CAPTCHA. You need to install one of them, then add it to your django project according to their documents.

 - [simple-captcha](https://github.com/mbi/django-simple-captcha)
 - [recaptcha](https://github.com/praekelt/django-recaptcha)
 - [recaptcha2](https://github.com/kbytesys/django-recaptcha2)

For more information, please go to the engine site.

Then add the following to your `settings.py` with the name of the installed engine:

```python
MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}
```

----------
## Results
[simple captcha](https://github.com/mbi/django-simple-captcha)

![captcha of recaptcha](https://github.com/xcai/django-grappelli-captcha-admin/blob/main/django-simple-captcha.png)

[recaptcha2](https://github.com/kbytesys/django-recaptcha2)

![captcha of recaptcha2](http://bayanbox.ir/view/2417903076718397977/reCaptcha2.png)


[recaptcha](https://github.com/praekelt/django-recaptcha)

![captcha of recaptcha](http://bayanbox.ir/view/2014387201108001651/reCaptcha.png)

