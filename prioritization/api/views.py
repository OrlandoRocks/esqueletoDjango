from django.shortcuts import render
import csv, io
from django.shortcuts import render
from django.contrib import messages
from rest_framework import generics, status
from rest_framework.views import APIView

from .models import Prioritization
from .serializers import PrioritizationSerializer

# Create your views here.

class PrioritizationView(generics.ListAPIView):
    queryset = Prioritization.objects.all()
    serializer_class = PrioritizationSerializer


# one parameter named request
def PrioritizationGetFile(request):
    # declaring template
    template = "prioritization_upload.html"
    data = Prioritization.objects.all()
    serializer_class = PrioritizationSerializer
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'El orden del CSV debe ser: counter, name, project_name, issue_key, priority, priority_number, case_title, status, progress, sprint, due_date, sys_fiscal_week, created, a, project_size, report_table, request_item, request_owner, notes, objective, rowid',
        'prioritization_info': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Este no es un CSV :(')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Prioritization.objects.update_or_create(
            counter = column[0],
            name = column[1],
            project_name = column[2],
            issue_key = column[3],
            priority = column[4],
            priority_number = column[5] or 0,
            case_title = column[6],
            status = column[7],
            progress = column[8],
            sprint = column[9],
            due_date = column[10],
            sys_fiscal_week = column[11],
            created = column[12],
            a = column[13],
            project_size = column[14],
            report_table = column[15],
            request_item = column[16],
            request_owner = column[17],
            notes = column[18],
            objective = column[19],
            rowid = column[20]
        )
    context = {}
    return render(request, template, context)
