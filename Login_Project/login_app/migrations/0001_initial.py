# Generated by Django 3.2 on 2023-04-13 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
