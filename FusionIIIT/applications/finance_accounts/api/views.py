from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.shortcuts import get_object_or_404
from applications.finance_accounts.models import *
from django.contrib.auth.models import User
from applications.globals.models import ExtraInfo, HoldsDesignation, Designation



class PaymentschemeApi(APIView):
    def get(self, request):
        Paymentscheme_obj = Paymentscheme.objects.all();
        Paymentscheme_obj = PaymentschemeSerializer(Paymentscheme_obj, many=True)
        return Response({'status':200, 'payload':serialized_obj.data})

    def post(self, request):
        data = request.data
    month = data['month']
    year = data['year']
    pf = data['pf']
    name = data['name']
    designation =data['designation']
    pay = data['pay']
    gr_pay = data['gr_pay']
    da = data['da']
    ta = data['ta']
    hra = data['hra']
    fpa = data['fpa']
    special_allow = data['special_allow']
    nps = data['nps']
    gpf = data['gpf']
    income_tax = data['income_tax']
    p_tax = data['p_tax']
    gslis = data['gslis']
    gis = data['gis']
    license_fee = data['license_fee']
    electricity_charges = data['electricity_charges']
    others = data['others']
    gr_reduction = data['gr_reduction']
    net_payment = data['net_payment']
    senior_verify = data['senior_verify']
    ass_registrar_verify = data['ass_registrar_verify']
    ass_registrar_aud_verify = data['ass_registrar_aud_verify']
    registrar_director_verify = data['registrar_director_verify']
    runpayroll = data['runpayroll']
    view = data['view']
        obj = Payments(
    month = month, 
    year = year,
    pf = pf,
    name = name, 
    designation = designation,
    pay = pay,
    gr_pay = gr_pay,
    da = da,
    ta = ta,
    hra = hra,
    fpa = fpa,
    special_allow = special_allow,
    nps = nps,
    gpf = gpf,
    income_tax = income_tax,
    p_tax = p_tax,
    gslis = gslis,
    gis = gis,
    license_fee = license_fee,
    electricity_charges = electricity_charges, 
    others = others,
    gr_reduction = gr_reduction, 
    net_payment = net_payment,
    senior_verify = senior_verify,
    ass_registrar_verify = ass_registrar_verify,
    ass_registrar_aud_verify = ass_registrar_aud_verify,
    registrar_director_verify = registrar_director_verify,
    runpayroll = runpayroll,
    view = view,
        )
        obj.save()
        return Response({'status':200})


class ReceiptsApi(APIView):
    def get(self, request):
        receipts_obj = Receipts.objects.all();
        serialized_obj = ReceiptsSerializer(receipts_obj, many=True)
        return Response({'status':200, 'payload':serialized_obj.data})
    def post(self, request):
        data = request.data
        receipt_id = data['receipt_id']
        TransactionId = data['TransactionId']
        ToWhom = data['ToWhom']
        FromWhom = data['FromWhom']
        Purpose = data['Purpose']
        Date = data['Date']
        obj = Receipts(
            receipt_id = receipt_id,
            TransactionId =TransactionId,
            ToWhom=ToWhom,
            FromWhom=FromWhom,
            Purpose=Purpose,
            Date=Date
        )
        obj.save()
        return Response({'status':200})


class PaymentsApi(APIView):
    def get(self, request):
        Payments_obj = Payments.objects.all();
        serialized_obj = PaymentsSerializer(Payments_obj, many=True)
        return Response({'status':200, 'payload':serialized_obj.data})

    def post(self, request):
        data = request.data
        payment_id= data['payment_id']
        TransactionId = data['TransactionId']
        ToWhom = data['ToWhom']
        FromWhom = data['FromWhom']
        Purpose = data['Purpose']
        Date = data['Date']
        obj = Payments(
            payment_id = payment_id,
            TransactionId =TransactionId,
            ToWhom=ToWhom,
            FromWhom=FromWhom,
            Purpose=Purpose,
            Date=Date
        )
        obj.save()
        return Response({'status':200})


class BankApi(APIView):
    def get(self, request):
        Bank_obj = Bank.objects.all();
        Bank_obj = BankSerializer(Bank_obj, many=True)
        return Response({'status':200, 'payload':serialized_obj.data})

    def post(self, request):
        data = request.data
        bank_id= data['bank_id']
        Account_no = data['Account_no']
        Bank_Name = data['Bank_Name']
        IFSC_Code = data['IFSC_Code']
        Branch_Name = data['Branch_Name']
        obj = Bank(
            bank_id = bank_id,
            Account_no =Account_no,
            Bank_Name=Bank_Name,
            IFSC_Code=IFSC_Code,
            Branch_Name=Branch_Name,
        )
        obj.save()
        return Response({'status':200})


class CompanyApi(APIView):
    def get(self, request):
        Company_obj = Company.objects.all();
        Company_obj = CompanySerializer(Company_obj, many=True)
        return Response({'status':200, 'payload':serialized_obj.data})

    def post(self, request):
        data = request.data
        company_id= data['company_id']
        Company_Name = data['Company_Name']
        Start_Date = data['Start_Date']
        End_Date = data['End_Date']
        Description = data['Description']
        Status = data['Status']
        obj = Company(
            company_id = company_id,
            Company_Name =Company_Name,
            Start_Date=Start_Date,
            End_Date=End_Date,
            Branch_Name=Branch_Name,
            Status=Status,
        )
        obj.save()
        return Response({'status':200})

