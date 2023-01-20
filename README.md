# recipe-django
This Repository contain recipe app project built using Django


# Project Structure 

```
├── recipe/              
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
|
├── food/                  
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── templates/food
|       ├── base.html
|       ├── item-detail.html
|       ├── item-form.html
|       ├── items.html
│   ├── static/
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
|
├── users/                
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── templates/user/
|       ├── register.html
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── manage.py
└── requirements.txt
└── Dockerfile
└── docker-compose.yaml
```