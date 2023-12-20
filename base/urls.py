from django.urls import path
from . import views     

urlpatterns = [
    path('home/',views.home, name="home"), 
    path('room/<str:pk>/',views.room, name="room"),
    path('add_new/',views.Add_new, name="add_new"),
    path('tyre_new/',views.Tyre_new, name="tyre_new"),
    path('order/',views.Order_new, name="order"),
    path('tyre_edit/<str:q>/',views.Tyre_Edit, name="tyre_edit"),
    path('tyre_status/',views.Tyre_status, name="tyre_status"),
    path('order_status/',views.Order_status, name="order_status"),
    path('customer_edit/<str:a>/',views.Customer_Edit, name="customer_edit"),
    path('customer_new/',views.Customer_new, name="customer_new"),
    path('customer_profile/',views.Customer_profile, name="customer_profile"),
    path('customer_profile_page/<str:q>/',views.Customer_profile_page, name="customer_profile_page"),
    path('company_new/',views.Company_new, name="company_new"),
    path('update/',views.Update, name="update"),
    path('check_status/',views.CheckStatus, name="check_status"),
    path('tyre_update/',views.Tyre_update, name="tyre_update"),
    path('customer_update/',views.Customer_update, name="customer_update"),
    path('',views.loginPage, name="login"),
]