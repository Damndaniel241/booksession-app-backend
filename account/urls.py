from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.Signup, name='Signup'),
    path('login/', views.Login, name='Login'),
    path('update/<int:id>', views.updateAccount, name='updateAccount'),
    path('delete/<int:id>',views.deleteAccount,name='deleteAccount'),
 ]
