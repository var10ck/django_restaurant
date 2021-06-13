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
    list_filter = ['user',
                   'status',
                   ]
    inlines = [OrderedMealInline]

    exclude = ['user']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


@register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_filter = ['table']
    fields = [('first_name', 'middle_name', 'last_name'),
              'table',
              ]


admin.site.register(OrderStatus)
admin.site.register(TableTop)
