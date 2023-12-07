'''
#? Serializers are used to convert complex data into python datatypes 
# that can then be easily rendered into JSON which we will be using 
# in ReactJS i.e Client-side
'''

from rest_framework import serializers
from .models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['name', 'detail']