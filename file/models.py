from django.db import models
import uuid
# Create your models here.
class Employee(models.Model):
    uid=models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    ename=models.CharField(max_length=100)
    age=models.IntegerField()
    salary=models.IntegerField()
    location=models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.ename
