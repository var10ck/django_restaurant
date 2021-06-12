from django.db import models
from django.utils.translation import gettext_lazy as _
import os
from django.urls import reverse
import uuid
from django.utils.text import slugify


class Menu(models.Model):
    title = models.CharField(_('Заголовок'),
                             max_length=200,
                             )
    summary = models.CharField(_('Описние'),
                               max_length=200,
                               )
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MealType(models.Model):
    title = models.CharField(_('Название'),
                             max_length=100,
                             )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('Тип продукта')
        verbose_name_plural = _('Типы продуктов')


class Ingredient(models.Model):
    name = models.CharField(_('Название'),
                            max_length=150,
                            )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Ингредиент')
        verbose_name_plural = _('Ингредиенты')


class Unit(models.Model):
    name = models.CharField(_('Название'),
                            max_length=10,
                            )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Единица измерения')
        verbose_name_plural = _('Единицы измерения')


class Meal(models.Model):
    type = models.ForeignKey(MealType,
                             models.CASCADE,
                             related_name='meals',
                             verbose_name=_('Тип')
                             )
    menu = models.ManyToManyField(Menu,
                                  related_name='meals',
                                  )
    title = models.CharField(_('Заголовок'),
                             max_length=200,
                             )
    sku = models.CharField(_('Артикул'),
                           max_length=20,
                           )
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            )
    description = models.CharField(_('Описание'),
                                   max_length=200,
                                   )
    weight = models.SmallIntegerField(_('Масса'),
                                      null=True,
                                      blank=True,
                                      )
    number_of_calories = models.SmallIntegerField(_('Количество калорий'),
                                                  blank=True,
                                                  null=True,
                                                  )
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Дата обновления')
    is_active = models.BooleanField(_('Активно'),
                                    default=False,
                                    )
    price = models.DecimalField(_('Цена'),
                                max_digits=11,
                                decimal_places=2,
                                )
    Instructions = models.TextField('Инструкции',
                                    blank=True,
                                    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('Блюдо')
        verbose_name_plural = _('Блюда')
        ordering = ('title',)


class MealIngredient(models.Model):
    meal = models.ForeignKey(Meal,
                             on_delete=models.DO_NOTHING,
                             verbose_name=_('Блюдо'),
                             )
    ingredient = models.ForeignKey(Ingredient,
                                   on_delete=models.DO_NOTHING,
                                   verbose_name=_('Ингредиент'),
                                   )
    quantity = models.IntegerField(_('Количество'),
                                   )
    unit = models.ForeignKey(Unit,
                             on_delete=models.DO_NOTHING,
                             verbose_name=_('Единица измерения'),
                             )

    def __str__(self):
        return f'{self.meal.title}'

    class Meta:
        verbose_name = _('Ингредиент блюда')
        verbose_name_plural = _('Ингредиенты блюда')
