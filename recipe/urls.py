from django.contrib import admin
from django.urls import path,include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('food.urls')),
    path('register/', user_views.register, name='register'),
    path('logout/', user_views.logout_user, name='logout'),
]
