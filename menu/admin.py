from django.contrib import admin
from django.contrib.admin import register
from admin_numeric_filter.admin import NumericFilterModelAdmin, SingleNumericFilter, RangeNumericFilter, \
    SliderNumericFilter
from .models import Menu, MealIngredient, Ingredient, \
    MealType, Unit, Meal


@register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_filter = ['created',
                   'updated',
                   ]


class MealIngredientInline(admin.TabularInline):
    model = MealIngredient
    fk_name = 'meal'
    verbose_name = 'Ингредиент'
    verbose_name_plural = 'Ингредиенты'


@register(Meal)
class MealAdmin(NumericFilterModelAdmin):
    list_display = ['id',
                    'title',
                    'type',
                    'sku',
                    'description',
                    'is_active',
                    'price',
                    ]
    list_filter = ['type',
                   'is_active',
                   ('price', SliderNumericFilter),
                   ]
    prepopulated_fields = {'slug': ('title', 'sku')}
    inlines = [MealIngredientInline]


admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(MealType)



