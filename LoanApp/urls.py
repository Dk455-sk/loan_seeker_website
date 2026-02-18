"""
URL configuration for LoanApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from Home import views as hviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loan_application/',hviews.loan_application,name="loan_application"),
    path('',hviews.home,name="home"),
    path('home_loan',hviews.home_loan,name="home_loan"),
    path('bussinsess_loan',hviews.bussiness_loan,name="bussiness_loan"),
    path('personal_loan',hviews.personal_loan,name="personal_loan"),
    path('poperty_loan',hviews.poperty_loan,name="poperty_loan"),
    path('term',hviews.term,name="term"),
    path('bill_discount',hviews.bill_discount,name="bill_discount"),
    path('credit',hviews.credit,name="credit"),
    path('gureenty',hviews.gureenty,name="gureenty"),
    path('contactus',hviews.contactus,name="contactus"),
    path('emi_calculator',hviews.emi_calculator,name="emi_calculator"),
]
