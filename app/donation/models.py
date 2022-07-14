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


class Donation(models.Model):
    hospital_name=models.CharField(_('hospital_name'),max_length=255,blank=True,null=True)
    location=models.CharField(_('location'),max_length=255,blank=True,null=True)
    donor_id=models.CharField(_('donor_id'),max_length=255,blank=True,null=True)
    blood_type=models.CharField(_('blood_type'),max_length=255,blank=True,null=True)
    # gender=models.CharField(_('gender'),max_length=255,blank=True,null=True)
    # blood_type=models.CharField(_('blood_type'),max_length=255,blank=True,null=True)
    # password=models.CharField(_('password'),max_length=255,blank=True,null=True)
    # marital_status=models.CharField(_('marital_status'),max_length=255,blank=True,null=True)
    # mobile_number=models.CharField(_('mobile_number'),max_length=255,blank=True,null=True)
    # permanent_address=models.CharField(_('permanent_address'),max_length=255,blank=True,null=True)
    
    # image = models.ImageField(
    #     _('image'), upload_to=nameFile, default="uploads/Cases.png")
    class Meta:
        ordering = ["-id"]
