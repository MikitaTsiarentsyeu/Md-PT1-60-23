from django.db import models

class Regi(models.Model):
    name = models.CharField('Имя', max_length = 50)
    mail = models.CharField('Почта', max_length = 50)
    phone = models.CharField('Телефон', max_length = 50)
    details = models.TextField('Детали')
    

    def __str__(self):
        return str(self.id)

    


    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'