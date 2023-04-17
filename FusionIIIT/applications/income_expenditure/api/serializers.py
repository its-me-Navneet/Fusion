from rest_framework import serializers
from applications.income_expenditure.models import *

class ExpenditureTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model=ExpenditureType
        fields=('__all__')

# class ExpenditureSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Expenditure
#         fields=('__all__')

# class IncomeSourceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = IncomeSource
#         fields=('__all__')

# class IncomeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Income
#         fields=('__all__')

# class FixedAttributesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=FixedAttributes
#         fields=('__all__')

# class BalanceSheetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=BalanceSheet
#         fields=('__all__')

# class otherExpenseSerializer(serializers.ModelSerializer):

#     class Meta:
#         model=otherExpense
#         fields=('__all__')
