from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Transaction


class UserSerializer(serializers.HyperlinkedModelSerializer):
    transactions = serializers.ReadOnlyField(source='get_transactions')
    user = serializers.HyperlinkedIdentityField(view_name="customuser-detail")

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'user', 'transactions']


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedRelatedField(lookup_field='slug', view_name="transaction-detail", read_only=True)
    slug = serializers.HyperlinkedIdentityField(lookup_field='slug', view_name="transaction-detail", read_only=True)

    class Meta:
        model = Transaction
        fields = '__all__'

