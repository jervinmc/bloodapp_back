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


class Assestment(models.Model):
    user_id = models.IntegerField(_('user_id'),default=0.0)
    hospital_id=models.CharField(_('hospital_id'),max_length=255,blank=True,null=True)
    is_q1=models.CharField(_('is_q1'),max_length=255,blank=True,null=True)
    is_q2=models.CharField(_('is_q2'),max_length=255,blank=True,null=True)
    is_q3=models.CharField(_('is_q3'),max_length=255,blank=True,null=True)
    is_q4=models.CharField(_('is_q4'),max_length=255,blank=True,null=True)
    is_q5=models.CharField(_('is_q5'),max_length=255,blank=True,null=True)
    is_q6=models.CharField(_('is_q6'),max_length=255,blank=True,null=True)
    is_q7=models.CharField(_('is_q7'),max_length=255,blank=True,null=True)
    is_q8=models.CharField(_('is_q8'),max_length=255,blank=True,null=True)
    is_q9=models.CharField(_('is_q9'),max_length=255,blank=True,null=True)
    is_q10=models.CharField(_('is_q10'),max_length=255,blank=True,null=True)
    is_q11=models.CharField(_('is_q11'),max_length=255,blank=True,null=True)
    is_q12=models.CharField(_('is_q12'),max_length=255,blank=True,null=True)
    is_q13=models.CharField(_('is_q13'),max_length=255,blank=True,null=True)
    is_q14=models.CharField(_('is_q14'),max_length=255,blank=True,null=True)
    is_q15=models.CharField(_('is_q15'),max_length=255,blank=True,null=True)
    is_q16=models.CharField(_('is_q16'),max_length=255,blank=True,null=True)
    is_q17=models.CharField(_('is_q17'),max_length=255,blank=True,null=True)
    is_q18=models.CharField(_('is_q18'),max_length=255,blank=True,null=True)
    is_q19=models.CharField(_('is_q19'),max_length=255,blank=True,null=True)
    is_q20=models.CharField(_('is_q20'),max_length=255,blank=True,null=True)
    is_q21=models.CharField(_('is_q21'),max_length=255,blank=True,null=True)
    is_q22=models.CharField(_('is_q22'),max_length=255,blank=True,null=True)
    is_q23=models.CharField(_('is_q23'),max_length=255,blank=True,null=True)
    is_q24=models.CharField(_('is_q24'),max_length=255,blank=True,null=True)
    is_q25=models.CharField(_('is_q25'),max_length=255,blank=True,null=True)
    is_q26=models.CharField(_('is_q26'),max_length=255,blank=True,null=True)
    is_q27=models.CharField(_('is_q27'),max_length=255,blank=True,null=True)
    is_q28=models.CharField(_('is_q28'),max_length=255,blank=True,null=True)
    is_q29=models.CharField(_('is_q29'),max_length=255,blank=True,null=True)
    is_q30=models.CharField(_('is_q30'),max_length=255,blank=True,null=True)
    is_q31=models.CharField(_('is_q31'),max_length=255,blank=True,null=True)
    is_q32=models.CharField(_('is_q32'),max_length=255,blank=True,null=True)
    is_q33=models.CharField(_('is_q33'),max_length=255,blank=True,null=True)
    is_q34=models.CharField(_('is_q34'),max_length=255,blank=True,null=True)
    status=models.CharField(_('status'),max_length=255,blank=True,null=True)

    class Meta:
        ordering = ["-id"]
