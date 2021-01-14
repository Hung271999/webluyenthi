# Generated by Django 3.1.2 on 2020-11-30 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20201128_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='subjects',
        ),
        migrations.AddField(
            model_name='exam',
            name='subjects',
            field=models.ManyToManyField(to='home.Subjects'),
        ),
        migrations.AlterField(
            model_name='question',
            name='exam',
            field=models.ManyToManyField(to='home.Exam'),
        ),
    ]