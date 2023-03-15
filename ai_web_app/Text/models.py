from django.db import models

class Text(models.Model):
    text_id      = models.AutoField(primary_key= True)
    name         = models.CharField(max_length=50,null=False)
    level        = models.CharField(max_length=20,blank=True,null=True)
    subLevel     = models.IntegerField(default=0)
    hindiText    = models.CharField(max_length=2000,null=False)
    englishText  = models.CharField(max_length=2000,null=False)
    flag1        = models.BooleanField(default=True)
    hintString  = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        db_table = 'text_content'

    def __str__(self):
        return self.name