# Generated by Django 3.2.3 on 2021-06-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20210531_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizz',
            name='pergunta6',
            field=models.CharField(blank=True, choices=[('1', 'Spring'), ('2', 'Winter'), ('3', 'Fall'), ('4', 'Azul'), ('5', 'Summer')], default='Unspecified', max_length=1),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='pergunta8',
            field=models.CharField(blank=True, choices=[('1', 'Cores Frias'), ('2', 'Cores Quentes')], default='Unspecified', max_length=1),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='pergunta9',
            field=models.CharField(blank=True, choices=[('1', 'Cores Frias'), ('2', 'Cores Quentes')], default='Unspecified', max_length=1),
        ),
    ]
