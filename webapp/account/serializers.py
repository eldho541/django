from rest_framework import serializers
from account.models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields =('email', 'username', 'date_joined','last_login','is_admin','is_staff')