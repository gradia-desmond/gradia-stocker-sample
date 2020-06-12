# Generated by Django 3.0.6 on 2020-06-12 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grading', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ParcelTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initiated_date', models.DateTimeField(auto_now_add=True)),
                ('confirmed_date', models.DateTimeField(blank=True, null=True)),
                ('expired', models.BooleanField(default=False)),
                ('remarks', models.TextField(blank=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gave_parcels', to=settings.AUTH_USER_MODEL)),
                ('parcel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='grading.Parcel')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='received_parcels', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParcelTransferFromVault',
            fields=[
            ],
            options={
                'verbose_name': 'Parcel Transfers (initiate withdraw from vault)',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('ownerships.parceltransfer',),
        ),
        migrations.CreateModel(
            name='ParcelTransferToVault',
            fields=[
            ],
            options={
                'verbose_name': 'Confirm carats and pieces in received parcel',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('ownerships.parceltransfer',),
        ),
    ]
