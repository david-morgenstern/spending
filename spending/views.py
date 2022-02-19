import json

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import otp_clean_csv
from .operations import Operations


class DashboardView(APIView):
    def get(self, request):
        csv_files = ['data/1.csv']
        result = otp_clean_csv(csv_files)
        parsed = json.loads(result.to_json(date_format='iso', orient='index'))

        ops = Operations(result)
        by_date = ops.get_by_date_group
        by_target = ops.get_by_target_group

        result_json = {'table': parsed, 'date_group': json.loads(by_date.to_json(date_format='iso')),
                       'target_group': json.loads(by_target.to_json(date_format='iso'))}
        return Response(result_json)


def home(request):
    csv_files = ['data/1.csv']
    result = otp_clean_csv(csv_files)
    parsed = json.loads(result.to_json(date_format='iso'))

    ops = Operations(result)
    by_date = ops.get_by_date_group
    by_target = ops.get_by_target_group

    result_json = {'table': parsed, 'date_group': json.loads(by_date.to_json(date_format='iso')),
                   'target_group': json.loads(by_target.to_json(date_format='iso'))}
    return HttpResponse(json.dumps(result_json, indent=4))
