from django.shortcuts import render, redirect

from rest_framework.response import Response
from rest_framework import status, viewsets

from .models import Contact
from .permissions import AdminOnly
from .filters import ContactMessageFilter
from .pagination import ContactMessagePaginator
from .serializers import ContactMessageSerializer

"""
Just to be cohesive we can render it like that like that or in classic CBV
"""
# class LandingAPIView(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'meant/index.html'  

#     def get(self, request):

#         serializer = ContactSerializer()
#         return Response(template_name = 'meant/index.html')

def index(request):

    return render(request, 'meant/index.html')


def login(request):

   return render(request, 'meant/login.html')


"""
I've used serializers with inputs overrides as forms here 
We can do this in other ways.

First.
    Django forms with attrs={'class':'class_name'}
Second.
    Custom forms in some frontend framework. 
    This is the most typically solution, where you only posting data to
    an endpoint. This works here two I just have rendering form done by Django
    If you wanna test this out just go into postman or /swagger/

"""

def contact_form(request):

    serializer = ContactMessageSerializer()
    context = {
        'serializer': serializer
    }

    return render(request, 'meant/contact.html', context)


"""
In other situation I would create separate file/app for api functions
just to keep api endpoints separate
and if you want partial update just use patch request
"""

class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = (AdminOnly,)
    queryset = Contact.objects.all()
    pagination_class = ContactMessagePaginator
    serializer_class = ContactMessageSerializer
    filterset_class  = ContactMessageFilter

    def create(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)