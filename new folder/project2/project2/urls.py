"""
URL configuration for project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app2 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accnts/',include('django.contrib.auth.urls')),
    path('login_1',views.login_1,name='login_1'),
    path('signup_1',views.signup_1,name='signup_1'),
    path('home',views.home,name='home'),
    path('',views.base,name='base'),
    path('logout',views.user_logout,name='logout'),
    path('data',views.add_data,name='add_data'),
    path('view',views.view_data,name='view_data'),
    path('view_item/<int:p>',views.view_item,name='view_item'),
    path('edit_item/<int:p>',views.edit_item,name='edit_item'),
    path('delete_item/<int:p>',views.delete_item,name='delete_item'),
]
