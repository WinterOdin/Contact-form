from django.core.validators import validate_email
from rest_framework import serializers
from django.conf import settings
from .models import Contact
import operator
import os


"""
This just adds a classes to django serializers rendered as forms 
Basically I wanted to use some framework to serve html files so
I thought if im using Django I can use serializer rendering but I didn't
liked how they looked so I added custom template instead ¯\_(ツ)_/¯
"""

TEMPLATE_PATH = os.path.join(
                settings.TEMPLATES[0]['DIRS'][0], 'base', 'custom_input_forms.html'
            )
CHOICE_CHECK = set(map(operator.itemgetter(0), Contact.SUBJECT))

class ContactMessageSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField()
    subject = serializers.ChoiceField(choices=Contact.SUBJECT)

    name = serializers.CharField(
        style={
            'template': TEMPLATE_PATH,
            'class': 'custom_form_control',
            'input_type': 'input'
        },
        max_length=50,
        min_length=5
    )

    email = serializers.CharField(
        style={
            'template': TEMPLATE_PATH,
            'class': 'custom_form_control',
            'input_type': 'input'
        },
        max_length=55
    )

    subject = serializers.CharField(
        style={
            'template': TEMPLATE_PATH,
            'class': 'custom_form_control',
            'input_type': 'select',
            'choice': Contact.SUBJECT
        }
    )

    message = serializers.CharField(
        style={
            'template': TEMPLATE_PATH,
            'input_type': 'textarea',
            'placeholder': 'Tell us your story.'
        },
        max_length=500,
        min_length=10
    )

    def get_status(self, obj):
        return obj.status

    def validate(self, data):
        name = data['name']
        email = data['email']
        choice = data['subject']

        try:
            validate_email(email)
        except:
            raise serializers.ValidationError({'Invalid Email': 'Email is invalid, please recheck.'})

        if not (choice in CHOICE_CHECK):
            choices_printable = ', '.join(CHOICE_CHECK)
            raise serializers.ValidationError({'Invalid Choice': f'Choice field is not valid. Valid choices are: {choices_printable}'})

        return data

    class Meta:
        model = Contact
        fields = '__all__'
