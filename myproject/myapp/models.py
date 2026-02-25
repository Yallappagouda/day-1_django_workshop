from django.db import models

class Addition(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    result = models.IntegerField()

    def __str__(self):
        return f"{self.num1} + {self.num2} = {self.result}"