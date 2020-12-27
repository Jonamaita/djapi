# Generated by Django 3.1.4 on 2020-12-27 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]