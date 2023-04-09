from django.db import models

class Reg(models.Model):
    name = models.CharField('Имя', max_length = 50)
    phone = models.CharField('Телефон', max_length = 50)
    mail = models.CharField('Почта', max_length = 50)
    

    def __str__(self):
        return str(self.id)

    # def get_absolute_url(self):
    #     return f'/form/{self.id}'


    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'