import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .dataframe_cleaner import csv_to_dataframe
from .dataframe_operations import Operations


@login_required
def home(request):
    csv_files = ['data/1.csv']
    result = csv_to_dataframe(csv_files)
    parsed = json.loads(result.to_json(date_format='iso'))

    ops = Operations(result)
    by_date = ops.get_by_date_group
    by_target = ops.get_by_target_group

    result_json = {'table': parsed, 'date_group': json.loads(by_date.to_json(date_format='iso')),
                   'target_group': json.loads(by_target.to_json(date_format='iso'))}
    return HttpResponse(json.dumps(result_json, indent=4))

