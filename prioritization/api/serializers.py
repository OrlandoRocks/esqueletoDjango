from rest_framework import serializers

from .models import Prioritization


class PrioritizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prioritization
        fields = ('counter','name','project_name','issue_key','priority','priority_number',
                  'case_title','status','progress','sprint','due_date','sys_fiscal_week',
                  'created','a','project_size','report_table','request_item','request_owner'
                  ,'notes','objective','rowid')
