# Generated by Django 3.1.2 on 2020-12-01 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20201130_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='true_fale',
            field=models.BooleanField(default=False),
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
