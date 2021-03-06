# Generated by Django 2.0 on 2020-03-25 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0003_auto_20200323_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out_trade_num', models.UUIDField()),
                ('order_num', models.CharField(max_length=50)),
                ('trade_no', models.CharField(max_length=120)),
                ('status', models.CharField(max_length=20)),
                ('payway', models.CharField(default='alipay', max_length=20)),
                ('address', models.ForeignKey(on_delete=True, to='userapp.Address')),
                ('user', models.ForeignKey(on_delete=True, to='userapp.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodsid', models.PositiveIntegerField()),
                ('colorid', models.PositiveIntegerField()),
                ('sizeid', models.PositiveIntegerField()),
                ('count', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=True, to='order.Order')),
            ],
        ),
    ]
