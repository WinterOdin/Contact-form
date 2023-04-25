import django_filters 
from .models import Contact


class ContactMessageFilter(django_filters.FilterSet):

    class Meta:
        model = Contact
        fields = {
            'updated':['icontains','lte','gte'],
            'created':['icontains','lte','gte'],
            'name':['iexact'],
            'email':['iexact'],
            'subject':['iexact'],
            'status':['iexact'],
        }