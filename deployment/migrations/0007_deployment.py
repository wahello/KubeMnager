# Generated by Django 2.1 on 2018-08-28 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deployment', '0006_delete_deployment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deployment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('namespace', models.CharField(default='default', max_length=100)),
            ],
        ),
    ]
