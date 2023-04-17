from django.conf.urls import url
from . import views
from .views import *

urlpatterns = [
    url("paymentschemeApi", views.PaymentschemeApi.as_view(), name="aymentschemeApi"),
    url("reciptsApi", views.ReciptsApi.as_view(), name="reciptsApi"),
    url("paymentsApi", views.paymentsApi.as_view(), name="paymentsApi"),
    url("bankApi", views.BankApi.as_view(), name="bankApi"),
    url("companyApi", views.CompanyApi.as_view(), name="companyApi"),
    url(r'^api', include('applications.finance_accounts.api.urls')),
]