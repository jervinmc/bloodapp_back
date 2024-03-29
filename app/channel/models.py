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


class Channel(models.Model):
    channel=models.CharField(_('channel'),max_length=255,blank=True,null=True)
    finder_id=models.CharField(_('finder_id'),max_length=255,blank=True,null=True)
    hospital_id=models.CharField(_('hospital_id'),max_length=255,blank=True,null=True)
    class Meta:
        ordering = ["-id"]
