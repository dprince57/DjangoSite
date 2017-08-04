from django.db import models

# Create your models here.


class UserReg(models.Model):

    fName = models.CharField(max_length=25)
    lName = models.CharField(max_length=25)
    uName = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    area = models.IntegerField()
    lNum = models.IntegerField()

    class Meta:
        db_table = "user_data"
