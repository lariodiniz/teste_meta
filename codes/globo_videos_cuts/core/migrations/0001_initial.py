# Generated by Django 2.1.5 on 2019-02-04 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CuttingJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, choices=[(0, 'process'), (1, 'sucess'), (2, 'failure')], default=0, verbose_name='status')),
                ('path', models.CharField(max_length=200, verbose_name='path')),
            ],
            options={
                'verbose_name': 'Cutting Job',
                'verbose_name_plural': 'Cutting Jobs',
            },
        ),
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('start_time', models.CharField(max_length=12, verbose_name='start time')),
                ('end_time', models.CharField(max_length=12, verbose_name='end time')),
            ],
            options={
                'verbose_name': 'Program',
                'verbose_name_plural': 'Programs',
            },
        ),
        migrations.AddField(
            model_name='cuttingjobs',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Programs', verbose_name='program'),
        ),
    ]
