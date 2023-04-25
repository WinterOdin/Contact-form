from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from django.db import models
import uuid


# Create your models here.
class Contact(models.Model):

    """
    There is many ways to do this I've just chosen two diffrent ones.
    Alternatives are

        - Enums
        - django-model-utils
        
    """
    
    APP = 'app'
    PAY = 'payment'
    HR = 'hr'
    OTHER = 'other'
    SUBJECT = [
        (APP, _('App Support')),
        (PAY, _('Payment Support')),
        (HR, _('HR & Jobs')),
        (OTHER, _('Non related (Other)'))
    ]

    STATUS = (
       ('new', _('New')),
       ('progres', _('In Progres - someone is taking an action')),
       ('resolved', _('Resolved - action was made')),
   )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, max_length=50)
    email = models.EmailField(max_length=55, blank=False, db_index=True)
    subject = models.CharField(choices=SUBJECT, max_length=15, blank=False)
    message = models.TextField(max_length=500, blank=False)
    status = models.CharField(choices=STATUS, max_length=15, default=STATUS[0][0])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return str(f'{self.subject} is {self.status}')
