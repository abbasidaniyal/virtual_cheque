from django.db import models
# from users.models import Users
from users.models import Users


class Cheque(models.Model):
    # drawer = models.ForeignKey(Users, 
    #     verbose_name=("User that has issued the cheque"),
    #     on_delete=models.CASCADE)
    bearer= models.CharField(max_length=20,null=True)
    issue_date = models.DateField(auto_now_add=False)
    amount = models.FloatField()
    cheque = models.ImageField(upload_to="cheques/",blank = True,max_length=1000,null=True,)
    
        
