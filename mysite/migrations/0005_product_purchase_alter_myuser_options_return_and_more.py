# Generated by Django 4.1.6 on 2023-02-06 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_alter_myuser_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('quantity', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.product')),
            ],
            options={
                'verbose_name': 'Purchase',
                'verbose_name_plural': 'Purchases',
                'ordering': ('created',),
            },
        ),
        migrations.AlterModelOptions(
            name='myuser',
            options={'ordering': ('username',), 'verbose_name': 'MyUser', 'verbose_name_plural': 'MyUsers'},
        ),
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('delete', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mysite.purchase')),
            ],
            options={
                'verbose_name': 'return',
                'verbose_name_plural': 'returns',
            },
        ),
        migrations.AddField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
