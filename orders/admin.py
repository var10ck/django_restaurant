from django.contrib import admin
from django.contrib.admin import register
from .models import OrderedMeal, OrderStatus, TableTop, \
    Client, Order


class OrderedMealInline(admin.TabularInline):
    model = OrderedMeal
    fk_name = 'order'
    verbose_name = 'Заказанное блюдо'
    verbose_name_plural = 'Заказанные блюда'


@register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'status',
                    'discount',
                    'total',
                    ]
    list_editable = ['status',
                     ]
    inlines = [OrderedMealInline]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


admin.site.register(Client)
admin.site.register(OrderStatus)
admin.site.register(TableTop)
