# Generated by Django 5.0.6 on 2024-06-24 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_system', '0003_alter_service_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='categories',
            field=models.ManyToManyField(to='reservation_system.category'),
        ),
    ]
