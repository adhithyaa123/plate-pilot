# Generated by Django 3.2.25 on 2024-11-26 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.basemodel')),
                ('phone', models.CharField(max_length=15)),
                ('table', models.CharField(max_length=15)),
                ('status', models.BooleanField(default=False)),
                ('total', models.PositiveIntegerField(null=True)),
                ('waiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('api.basemodel',),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.basemodel')),
                ('item', models.CharField(max_length=200)),
                ('qty', models.PositiveIntegerField(default=1)),
                ('price', models.PositiveIntegerField()),
                ('order_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.order')),
            ],
            bases=('api.basemodel',),
        ),
    ]
