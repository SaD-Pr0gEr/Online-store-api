# Generated by Django 3.1.2 on 2021-06-30 13:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210510_1838'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collections',
            options={'verbose_name': 'Коллекция', 'verbose_name_plural': 'Коллекции'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterModelOptions(
            name='productcomment',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='collections',
            name='created_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='header',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='product',
            field=models.ManyToManyField(related_name='collections', to='shop.Product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='text',
            field=models.CharField(max_length=400, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='updated_date',
            field=models.DateField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='orderpositions',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='shop.orders', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='orderpositions',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='shop.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='orderpositions',
            name='quantity',
            field=models.IntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='created_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_status',
            field=models.CharField(choices=[('open', 'Новый'), ('process', 'В процессе'), ('done', 'Выполнен')], default='open', max_length=225, verbose_name='Статус заказа'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='total_quantity',
            field=models.IntegerField(verbose_name='Общ. количество товаров в заказе'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='total_sum',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Общая сумма заказа'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='updated_date',
            field=models.DateField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=400, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=225, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.URLField(blank=True, default='https://ricesplash.learningu.org/media/images/not-available.jpg', null=True, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_date',
            field=models.DateField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='comment',
            field=models.CharField(max_length=250, verbose_name='Отзыв'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='created_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='shop.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=5, message="you can't rate more than 5"), django.core.validators.MinValueValidator(limit_value=1, message="you can't rate less than 1")], verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='updated_date',
            field=models.DateField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
