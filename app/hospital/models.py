from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Hospital(models.Model):
    hospital_name=models.CharField(_('hospital_name'),max_length=255,blank=True,null=True)
    longitude=models.CharField(_('longitude'),max_length=255,blank=True,null=True)
    latitude=models.CharField(_('latitude'),max_length=255,blank=True,null=True)
    class Meta:
        ordering = ["-id"]
