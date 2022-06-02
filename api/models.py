from django.db import models

# Create your models here.


class AbstractPerson(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=11, null=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Doctor(AbstractPerson):
    post = models.CharField(verbose_name="Должность", max_length=50)

    def __str__(self):
        return self.name + ' : ' + self.post


class Patient(AbstractPerson):
    address = models.CharField(verbose_name='Адрес', max_length=100)
    district = models.IntegerField(verbose_name='Участок')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
