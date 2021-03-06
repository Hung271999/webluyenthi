# Generated by Django 3.1.2 on 2020-12-01 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20201201_1739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='true_fale',
            new_name='true',
        ),
        migrations.AlterField(
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
