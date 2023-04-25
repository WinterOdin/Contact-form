# we can use this or do it in pytest
from django.urls import reverse
from rest_framework.test import APITestCase
from django.test.client import Client
from django.contrib.auth.models import User
from .serializers import ContactMessageSerializer

class MessageViewSetTest(APITestCase):
    def setUp(self) -> None:

        self.admin_user = Client()
        self.base_user = Client()

        self.user = User.objects.create_superuser(
            username='foobar',
            email='foo@bar.com',
            password='hatefoobarpeople')

        self.admin_user.force_login(user=self.user)

        self.message_dummy = {
            'name': 'Marcel Czuryszkiewicz',
            'email': 'czuryszkiewicz@domain.com',
            'subject': 'app',
            'message': 'one test please'
        }


    def test_get_messages_admin(self):

        response = self.admin_user.get(reverse('message-list'))
        self.assertEqual(response.status_code, 200)
    
    def test_get_messages_all(self):

        response = self.base_user.get(reverse('message-list'))
        self.assertEqual(response.status_code, 403)

    def test_post_correct_payload(self):

        response_base = self.base_user.post(reverse('message-list'), self.message_dummy)
        response_admin = self.admin_user.post(reverse('message-list'), self.message_dummy)
  
        self.assertEqual(response_base.status_code, 201)
        self.assertEqual(response_admin.status_code, 201)
        self.assertEqual(response_admin.data['name'], self.message_dummy['name'])

    def test_post_incorrect_payload(self):

        self.message_dummy['subject'] = "this cant work"

        response_base = self.base_user.post(reverse('message-list'), self.message_dummy)
        response_admin = self.admin_user.post(reverse('message-list'), self.message_dummy)

        self.assertEqual(response_base.status_code, 400)
        self.assertEqual(response_admin.status_code, 400)
        

    """
    We can test serializers to but in this case I don't think that's necessary
    because we are doing full request-response cycle
    Regardles of that here is one for fun
    """

    def test_email_valid(self):
        
        self.message_dummy['email'] = 'emaildomain.com'
        serializer = ContactMessageSerializer(data=self.message_dummy)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), set(['Invalid Email']))