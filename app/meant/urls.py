from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import index, login, contact_form, MessageViewSet



router = DefaultRouter()
router.register('api/message', MessageViewSet, basename="message")

urlpatterns = [
	path('', index, name='home'),
	path('login/', login, name='login'),
    path('contact/', contact_form, name='contact'),
] + router.urls