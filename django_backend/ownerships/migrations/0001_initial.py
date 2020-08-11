# Generated by Django 3.0.6 on 2020-08-10 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grading', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractItemTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initiated_date', models.DateTimeField(auto_now_add=True)),
                ('confirmed_date', models.DateTimeField(blank=True, null=True)),
                ('fresh', models.BooleanField(default=True)),
                ('remarks', models.TextField(blank=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_parcels', to=settings.AUTH_USER_MODEL)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gave_parcels', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='received_parcels', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StoneTransfer',
            fields=[
                ('abstractitemtransfer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ownerships.AbstractItemTransfer')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='grading.Stone')),
            ],
            bases=('ownerships.abstractitemtransfer',),
        ),
        migrations.CreateModel(
            name='ParcelTransfer',
            fields=[
                ('abstractitemtransfer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ownerships.AbstractItemTransfer')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='grading.Parcel')),
            ],
            bases=('ownerships.abstractitemtransfer',),
        ),
    ]
