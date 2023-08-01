from django.db import models

# Create your models here.
class Base(models.Model):
    name = models.CharField('name', max_length = 77, blank = True)
    autor = models.CharField('autor', max_length = 50,)

    def __str__(self):
        return str(self.id)
    # def __str__(self):
    #     return f'Книга {self.name}'

    class Meta:
        verbose_name = 'Автор/Книга'
        verbose_name_plural = 'Автор/Книга'