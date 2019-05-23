from django.db import models

# Create your models here.
class Cheque(models.Model):
    issuer = models.ForeignKey("users.User", 
        verbose_name=_("User that has issued the cheque"),
        on_delete=models.CASCADE)
    cheque_id = models.UUIDField(_("Check ID"))
    issue_date = models.DateField(auto_now=True,editable=False )
    amount = models.IntegerField()
    cheque = models.ImageField(_(""), 
        upload_to=cheques/,blank = True,
        max_length=1000,
        null=True,)
    
        
