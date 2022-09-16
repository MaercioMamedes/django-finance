# Generated by Django 3.2 on 2022-09-09 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('StockExchange', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='ticker',
            field=models.CharField(default='a', max_length=10, verbose_name='código do papel'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assets_wallet', models.ManyToManyField(to='StockExchange.Asset')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
