from django.contrib import admin
from django.urls import path

from django.urls import include
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('get_user_info/',views.get_user_info, name='get_user_info'),
    path('confirmation_page/',views.confirmation_page, name='confirmation_page'),
    path('help/',views.help, name='help'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('thankyou/', views.thankyou_view, name='thankyou'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    
]
