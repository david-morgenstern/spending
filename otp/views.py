import json
import os

from django.http import HttpResponse

from .dataframe_cleaner import csv_to_dataframe
from .dataframe_operations import get_by_date_group, get_by_target_group

def home(request):
    csv_files = ['data/1.csv']
    result = csv_to_dataframe(csv_files)
    parsed = json.loads(result.to_json())
    result_json = {'table': parsed, 'date_group': json.loads(get_by_date_group(result).to_json()), 'target_group': json.loads(get_by_target_group(result).to_json())}
    return HttpResponse(json.dumps(result_json, indent=4))

