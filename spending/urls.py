from django.urls import path

from . import views
from .views import UserViewSet, TransactionViewSet

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

transaction_list = TransactionViewSet.as_view({
    'get': 'list'
})

transaction_detail = TransactionViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path("", views.Home.as_view(), name="home"),

    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='customuser-detail'),

    path("transactions/", transaction_list, name='transaction-list'),
    path("transactions/<int:pk>/", transaction_detail, name='transaction-detail'),
]
