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



'''
Serializers in Django REST framework serve two main purposes:

1.They handle the conversion of complex data types (like model instances) 
    into simpler, renderable formats (serialization), especially for 
    outputting data in responses.
2.They handle the conversion of incoming data (like JSON from a POST request) 
    into Python data types, validate this data, and then use it to create or 
    update model instances (deserialization).

'''