from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'id']


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedRelatedField(view_name="user-detail", read_only=True)
    user_id = serializers.SerializerMethodField('custom_user_id')

    @staticmethod
    def custom_user_id(transaction):
        return transaction.user.id

    class Meta:
        model = Transaction
        fields = '__all__'
