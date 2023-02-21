from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False, verbose_name='наименование')
	description = models.TextField(null=False, blank=False, verbose_name='описание')
	price = models.DecimalField(max_digits=10, decimal_places=3, null=False, blank=False, verbose_name='цена')

	class Meta:
		verbose_name = 'продукт'
		verbose_name_plural = 'продукты'

	def __str__(self):
		return self.name


class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	items = models.ManyToManyField(Item)
	discount = models.ForeignKey('Discount', on_delete=models.PROTECT, null=True, blank=True)
	tax = models.ForeignKey('Tax', on_delete=models.PROTECT, null=True, blank=True)

	def __str__(self):
		return f'{self.user} order #{self.pk}'

	class Meta:
		verbose_name = 'заказ'
		verbose_name_plural = 'заказы'


class Discount(models.Model):
	discount = models.IntegerField()

	class Meta:
		verbose_name = 'скидка'
		verbose_name_plural = 'скидки'

	def __str__(self):
		return str(self.discount)


class Tax(models.Model):
	tax = models.IntegerField()

	class Meta:
		verbose_name = 'налог'
		verbose_name_plural = 'налоги'

	def __str__(self):
		return str(self.tax)
