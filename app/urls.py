from django.urls import path

from app import views

urlpatterns=[

    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('login_view',views.login_view,name='login_view'),
    path('view_Book',views.view_Book,name='view_Book'),
    path('add_Customer',views.add_Customer,name='add_Customer'),
    path('view_Customer',views.view_Customer,name='view_Customer'),
    path('edit_customer/<int:id>', views.edit_customer, name='edit_customer'),
    path('delete_customer/<int:id>', views.delete_customer, name='delete_customer'),
    path('add_district',views.add_district,name='add_district'),
    path('view_district', views.view_district, name='view_district'),
    path('delete_district/<int:id>', views.delete_district, name='delete_district'),
    path('add_Area', views.add_Area, name='add_Area'),
    path('view_Area', views.view_Area, name='view_Area'),
    path('delete_Area/<int:id>', views.delete_Area, name='delete_Area'),
    path('adminview_Book', views.adminview_Book, name='adminview_Book'),
    path('add_BookCatogeory', views.add_BookCatogeory, name='add_BookCatogeory'),
    path('view_BookCatogeory', views.view_BookCatogeory, name='view_BookCatogeory'),
    path('delete_BookCatogery/<int:id>', views.delete_BookCatogery, name='delete_BookCatogery'),
    path('add_Dealer', views.add_Dealer, name='add_Dealer'),
    path('view_Dealer', views.view_Dealer, name='view_Dealer'),
    path('edit_Dealer/<int:id>', views.edit_Dealer, name='edit_Dealer'),
    path('delete_Dealer/<int:id>', views.delete_Dealer, name='delete_Dealer'),

    #################################DEALER PAGES############################
    path('dealer_home', views.dealer_home, name='dealer_home'),
    path('view_Book',views.view_Book,name='view_Book'),
    path('create_Book',views.create_Book,name='create_Book'),
    path('edit_Book/<int:id>', views.edit_Book, name='edit_Book'),
    path('admin_view_BookCatogeory', views.admin_view_BookCatogeory, name='admin_view_BookCatogeory'),
    path('delete/<int:id>', views.delete, name='delete'),


    path('Customer_Home', views.Customer_Home, name='Customer_Home'),
    path('customer_view_Book', views.customer_view_Book, name='customer_view_Book'),
    path('', views.Home, name='Home'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('customer_view_Dealer', views.customer_view_Dealer, name='customer_view_Dealer'),
    path('view_Customer_profile', views.view_Customer_profile, name='view_Customer_profile'),


    path('Customer_feedback', views.Customer_feedback, name='Customer_feedback'),
    path('view_customer_feedback', views.view_customer_feedback, name='view_customer_feedback'),
    path('edit_customer_feedback/<int:id>', views.edit_customer_feedback, name='edit_customer_feedback'),
    path('delete_customer_feedback/<int:id>', views.delete_customer_feedback, name='delete_customer_feedback'),
    path('admin_view_customer_feedback', views.admin_view_customer_feedback, name='admin_view_customer_feedback'),
    path('admin_reply/<int:id>', views.admin_reply, name='admin_reply'),
    path('Home', views.Home, name='Home'),

    path('bill_payment/<int:name_id>', views.bill_payment, name='bill_payment'),
    path('buy_now/<int:id>', views.buy_now, name='buy_now'),
    path('bill_history', views.bill_history, name='bill_history'),

]