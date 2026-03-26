from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('get_user_info/',views.get_user_info, name='get_user_info'),
    path('confirmation_page/',views.confirmation_page, name='confirmation_page'),
    path('help/',views.help, name='help'),
    path('feedback/', views.feedback_view, name='feedback')
]