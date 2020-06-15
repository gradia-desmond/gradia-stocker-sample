# Generated by Django 3.0.6 on 2020-06-15 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('remarks', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuthorizedPersonnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=11)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=11)),
                ('hkid', models.CharField(max_length=10)),
                ('remarks', models.TextField(blank=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Entity')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
