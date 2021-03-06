# Generated by Django 2.1.5 on 2019-02-05 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190204_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessedVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('duration', models.IntegerField(verbose_name='duration')),
            ],
            options={
                'verbose_name': 'Processed Video',
                'verbose_name_plural': 'Processed Videos',
            },
        ),
    ]
