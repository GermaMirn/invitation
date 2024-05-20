from django.db import models


class Answer(models.Model):
  fio = models.CharField('fio', max_length=100, default='не известно')
  come = models.CharField('come', max_length=50, default='I cant come')
  numberPeople = models.IntegerField(default=0)
  beverages = models.CharField('beverages', max_length=50)

  def __str__(self):
    return self.fio
  
  class Meta:
    verbose_name = 'Ответ'
    verbose_name_plural = 'Ответы'
