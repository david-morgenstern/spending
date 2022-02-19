from rest_framework import generics, viewsets

from .models import Transaction, CustomUser
from .serializers import TransactionSerializer, UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class TransactionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TransactionSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user)


class Home(generics.ListAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

# def home(request):
#     csv_files = ['data/1.csv']
#     result = otp_clean_csv(csv_files)
#     parsed = json.loads(result.to_json(date_format='iso'))
#
#     ops = Operations(result)
#     by_date = ops.get_by_date_group
#     by_target = ops.get_by_target_group
#
#     result_json = {'table': parsed, 'date_group': json.loads(by_date.to_json(date_format='iso')),
#                    'target_group': json.loads(by_target.to_json(date_format='iso'))}
#     return HttpResponse(json.dumps(result_json, indent=4))
