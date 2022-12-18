from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class User(models.Model):
    email=models.CharField(_('email'),max_length=255,blank=True,null=True)
    fullname=models.CharField(_('fullname'),max_length=255,blank=True,null=True)
    user_type=models.CharField(_('user_type'),max_length=255,blank=True,null=True)
    birthdate=models.CharField(_('birthdate'),max_length=255,blank=True,null=True)
    gender=models.CharField(_('gender'),max_length=255,blank=True,null=True)
    no_donate = models.IntegerField(_('no_donate'),default=0.0)
    blood_type=models.CharField(_('blood_type'),max_length=255,blank=True,null=True)
    password=models.CharField(_('password'),max_length=255,blank=True,null=True)
    marital_status=models.CharField(_('marital_status'),max_length=255,blank=True,null=True)
    mobile_number=models.CharField(_('mobile_number'),max_length=255,blank=True,null=True)
    longitude=models.CharField(_('longitude'),max_length=255,blank=True,null=True)
    latitude=models.CharField(_('latitude'),max_length=255,blank=True,null=True)
    permanent_address=models.CharField(_('permanent_address'),max_length=255,blank=True,null=True)
    is_active=models.BooleanField(_('is_active'),default=True)
    is_assessed=models.BooleanField(_('is_assessed'),default=True)
    is_notification=models.BooleanField(_('is_notification'),default=True)

    
    # image = models.ImageField(
    #     _('image'), upload_to=nameFile, default="uploads/Cases.png")
    class Meta:
        ordering = ["-id"]
