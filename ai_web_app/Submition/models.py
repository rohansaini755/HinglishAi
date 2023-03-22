from django.db import models
from Auth.models import User
from Text.models import Text

# Create your models here.
class submition(models.Model):
    submition_id       = models.AutoField(primary_key=True)
    # username         = models.ForeignKey(User, on_delete=models.CASCADE)
    id                 = models.ForeignKey(User,on_delete=models.CASCADE)
    username           = models.CharField(max_length=50)
    text_id            = models.ForeignKey(Text,on_delete=models.CASCADE)
    answer             = models.CharField(max_length=2000,null=False)
    date               = models.DateTimeField(auto_now_add=True)
    suggestions        = models.CharField(max_length=1000,null=True,default="")
    accuracy           = models.IntegerField()
    answer_status      = models.CharField(max_length=20,blank = True,null=True)
    flag               = models.BooleanField(default=True)
    
    class Meta:
        db_table='submitions'

    def __str__(self):
        return self.submition_id
