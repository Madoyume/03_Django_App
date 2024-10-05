from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

class Friend(models.Model):
    name = models.CharField(max_length=100, \
        validators=[MinLengthValidator(10)])
    mail = models.EmailField(max_length=200, \
        validators=[MinLengthValidator(10)])
    gender = models.BooleanField()
    age = models.IntegerField(validators=[ \
        MinValueValidator(0),
        MaxValueValidator(150)]
    )
    birthday = models.DateField()
    
    def __str__(self):
        return f'<Friend:id={str(self.id)}, {self.name}({self.age})>'
