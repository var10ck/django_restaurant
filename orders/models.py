from django.db import models
from django.contrib.auth.models import User
from menu.models import Meal
from decimal import Decimal

from django.utils.translation import gettext_lazy as _

TABLETOP_STATUSES = (('BR', 'Забронирован'),
                     ('OP', 'Свободен'),
                     ('OC', 'Занят')
                     )


class OrderStatus(models.Model):
    name = models.CharField(_('Название'),
                            max_length=50,
                            )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Статус заказа')
        verbose_name_plural = _('Статусы заказа')


class TableTop(models.Model):
    capacity = models.SmallIntegerField(_('Вместимость'))
    number = models.SmallIntegerField(_('Номер столика'))
    status = models.CharField(_('Статус'),
                              max_length=4,
                              choices=TABLETOP_STATUSES,
                              )

    def __str__(self):
        return f'Столик №{self.number}'

    class Meta:
        verbose_name = _('Столик')
        verbose_name_plural = _('Столики')


class Client(models.Model):
    first_name = models.CharField(_('Имя'),
                                  max_length=100,
                                  )
    middle_name = models.CharField(_('Отчество'),
                                   max_length=100,
                                   )
    last_name = models.CharField(_('Фамилия'),
                                 max_length=100,
                                 )
    table = models.ForeignKey(TableTop,
                              null=True,
                              on_delete=models.SET_NULL,
                              verbose_name=_('Столик'),
                              )

    def __str__(self):
        return f'{self.first_name}'

    class Meta:
        verbose_name = _('Клиент')
        verbose_name_plural = _('Клиенты')


class Order(models.Model):
    user = models.ForeignKey(User,
                             null=True,
                             on_delete=models.SET_NULL,
                             )
    status = models.ForeignKey(OrderStatus,
                               null=True,
                               on_delete=models.SET_NULL,
                               )
    discount = models.SmallIntegerField(_('Скидка'),
                                        default=0)

    def _get_total(self):
        sum = 0
        for m in self.meals.all():
            sum += m.meal.price * m.quantity
        return '{0:.2f}'.format(sum * Decimal(1.0 - self.discount/100, ) if self.discount else sum)

    total = property(_get_total)

    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')


class OrderedMeal(models.Model):
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              verbose_name=_('Заказ'),
                              related_name='meals',
                              )
    meal = models.ForeignKey(Meal,
                             null=True,
                             on_delete=models.SET_NULL,
                             verbose_name=_('Блюдо'),
                             related_name='meals',
                             )
    quantity = models.SmallIntegerField(_('Количество'),
                                        default=1,
                                        )

    price = models.DecimalField(_('Цена'),
                                decimal_places=2,
                                max_digits=11,
                                editable=False,
                                default=0,
                                )

    def __str__(self):
        return f'{self.meal.title}'

    def save(self, *args, **kwargs):
        self.price = self.meal.price
        super().save(*args, **kwargs)
