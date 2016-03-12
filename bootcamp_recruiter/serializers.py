from .models import Company
from rest_framework import serializers

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('industry_type','company_name'
                  ,'company_url','bootcamp_grad_hired'
                  , 'contact', 'notes','twitter_handle')
