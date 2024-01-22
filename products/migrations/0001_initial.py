# Generated by Django 5.0.1 on 2024-01-22 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img_url', models.CharField(max_length=1000)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('category', models.CharField(choices=[('Electronics', 'electronics'), ('Fashion', 'fashion'), ('Home', 'home'), ('Stationary', 'stationary'), ('Sports', 'sports')], max_length=50)),
            ],
        ),
    ]
