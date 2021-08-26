from django.db import models
import string

# Create your models here.
def get_file_info():
    return ''

class Prioritization(models.Model):
    counter = models.IntegerField()
    name = models.CharField(max_length=50)
    project_name = models.CharField(max_length=50)
    issue_key = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    priority_number = models.IntegerField()
    case_title = models.CharField(max_length=250)
    status = models.CharField(max_length=50)
    progress = models.CharField(max_length=50)
    sprint = models.CharField(max_length=50)
    due_date = models.CharField(max_length=50)
    sys_fiscal_week = models.CharField(max_length=50)
    created = models.CharField(max_length=50)
    a = models.CharField(max_length=50)
    project_size = models.CharField(max_length=50)
    report_table = models.CharField(max_length=50)
    request_item = models.CharField(max_length=100)
    request_owner = models.CharField(max_length=50)
    notes = models.CharField(max_length=100)
    objective = models.IntegerField()
    rowid = models.IntegerField(default=1)

    def _str_(self):
        return self.title