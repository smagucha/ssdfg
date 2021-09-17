from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('Bioinfo', views.userbio, name='userdetails'),
    path('listuser', views.listclients, name='list_user'),
    path('updatedetails/<int:id>', views.updateuser, name='update_details'),
    path('reoveclient/<int:id>', views.deletelient, name='delete_client'),

    path('businessdetails', views.businessdetails, name='client_business'),
    path('bizclient', views.clientsbusiness, name='client_biz'),
    path('updatebiz/<int:id>', views. updatebiz, name='update_biz'),
    path('removebiz/<int:id>', views.deletebiz, name='delete_business'),

    path('empform', views.employmentdetails, name='emp_form'),
    path('empdetails', views.showemploymentdetails, name='empldetails'),
    path('updateemp/<int:id>', views.updateemployment, name='update_biz'),
    path('removeemp/<int:id>', views.deleteemp, name='delete_emp'),
                                                                         
    path('bankform', views.BankDetails, name='bank_form'),
    path('bankdetails', views.bankclient, name='bank_details'),
    path('updateabank/<int:id>', views.updateBank, name='update biz'),
    path('removebank/<int:id>', views.deletebank, name='delete emp'),


    path('loanform', views.Loanform, name='loan_form'),
    path('loandetails', views.loantypedetails, name='loan_details'),
    path('updateloan/<int:id>', views.updateloan, name='update_loan'),
    path('removeloan/<int:id>', views.deletebank, name='delete_loan'),
    path('moredetails', views.moredetails, name='moredetails'),
  

    path('otherform', views.otherform, name='other_form'),
    path('otherdetails', views.otherdetails, name='other_details'),
    path('updateother/<int:id>', views.updateother, name='update_other'),
    path('deleteother/<int:id>', views.deleteother, name='delete_other'),

]