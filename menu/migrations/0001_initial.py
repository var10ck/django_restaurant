# Generated by Django 2.2.24 on 2021-06-12 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('sku', models.CharField(max_length=20, verbose_name='Артикул')),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.CharField(max_length=200, verbose_name='Описние')),
                ('weight', models.SmallIntegerField(blank=True, null=True, verbose_name='Масса')),
                ('number_of_calories', models.SmallIntegerField(blank=True, null=True, verbose_name='Количество калорий')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активно')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('Instructions', models.TextField(blank=True, verbose_name='Инструкции')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='MealType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип продукта',
                'verbose_name_plural': 'Типы продуктов',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('summary', models.CharField(max_length=200, verbose_name='Описние')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Единица измерения',
                'verbose_name_plural': 'Единицы измерения',
            },
        ),
        migrations.CreateModel(
            name='MealIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='menu.Ingredient', verbose_name='Ингредиент')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='menu.Meal', verbose_name='Блюдо')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='menu.Unit', verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Ингредиент блюда',
                'verbose_name_plural': 'Ингредиенты блюда',
            },
        ),
        migrations.AddField(
            model_name='meal',
            name='menu',
            field=models.ManyToManyField(related_name='meals', to='menu.Menu'),
        ),
        migrations.AddField(
            model_name='meal',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='menu.MealType', verbose_name='Тип'),
        ),
    ]
