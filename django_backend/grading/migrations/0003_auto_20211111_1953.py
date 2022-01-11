# Generated by Django 3.1.4 on 2021-11-11 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grading', '0002_auto_20211104_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stone',
            name='basic_fluorescence_1',
            field=models.CharField(blank=True, choices=[('VS', 'Very Strong'), ('S', 'Strong'), ('M', 'Medium'), ('F', 'Faint'), ('N', 'None'), ('MG', 'Medium Green'), ('MW', 'Medium White'), ('MB', 'Medium Blue'), ('MY', 'Medium Yellow')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='stone',
            name='basic_fluorescence_2',
            field=models.CharField(blank=True, choices=[('VS', 'Very Strong'), ('S', 'Strong'), ('M', 'Medium'), ('F', 'Faint'), ('N', 'None'), ('MG', 'Medium Green'), ('MW', 'Medium White'), ('MB', 'Medium Blue'), ('MY', 'Medium Yellow')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='stone',
            name='basic_fluorescence_3',
            field=models.CharField(blank=True, choices=[('VS', 'Very Strong'), ('S', 'Strong'), ('M', 'Medium'), ('F', 'Faint'), ('N', 'None'), ('MG', 'Medium Green'), ('MW', 'Medium White'), ('MB', 'Medium Blue'), ('MY', 'Medium Yellow')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='stone',
            name='basic_fluorescence_final',
            field=models.CharField(blank=True, choices=[('VS', 'Very Strong'), ('S', 'Strong'), ('M', 'Medium'), ('F', 'Faint'), ('N', 'None'), ('MG', 'Medium Green'), ('MW', 'Medium White'), ('MB', 'Medium Blue'), ('MY', 'Medium Yellow')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='stone',
            name='gw_fluorescence',
            field=models.CharField(blank=True, choices=[('VS', 'Very Strong'), ('S', 'Strong'), ('M', 'Medium'), ('F', 'Faint'), ('N', 'None'), ('MG', 'Medium Green'), ('MW', 'Medium White'), ('MB', 'Medium Blue'), ('MY', 'Medium Yellow')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='stone',
            name='gw_fluorescence_adjusted_1',
            field=models.CharField(blank=True, choices=[('VS', 'Very Strong'), ('S', 'Strong'), ('M', 'Medium'), ('F', 'Faint'), ('N', 'None'), ('MG', 'Medium Green'), ('MW', 'Medium White'), ('MB', 'Medium Blue'), ('MY', 'Medium Yellow')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='stone',
            name='gw_fluorescence_adjusted_2',
            field=models.CharField(blank=True, choices=[('VS', 'Very Strong'), ('S', 'Strong'), ('M', 'Medium'), ('F', 'Faint'), ('N', 'None'), ('MG', 'Medium Green'), ('MW', 'Medium White'), ('MB', 'Medium Blue'), ('MY', 'Medium Yellow')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='stone',
            name='gw_fluorescence_adjusted_3',
            field=models.CharField(blank=True, choices=[('VS', 'Very Strong'), ('S', 'Strong'), ('M', 'Medium'), ('F', 'Faint'), ('N', 'None'), ('MG', 'Medium Green'), ('MW', 'Medium White'), ('MB', 'Medium Blue'), ('MY', 'Medium Yellow')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='stone',
            name='gw_fluorescence_adjusted_final',
            field=models.CharField(blank=True, choices=[('VS', 'Very Strong'), ('S', 'Strong'), ('M', 'Medium'), ('F', 'Faint'), ('N', 'None'), ('MG', 'Medium Green'), ('MW', 'Medium White'), ('MB', 'Medium Blue'), ('MY', 'Medium Yellow')], max_length=4, null=True),
        ),
    ]
