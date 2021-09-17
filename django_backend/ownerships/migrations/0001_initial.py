# Generated by Django 3.1.4 on 2021-09-17 11:33

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
            name='StoneTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initiated_date', models.DateTimeField(auto_now_add=True)),
                ('confirmed_date', models.DateTimeField(blank=True, null=True)),
                ('fresh', models.BooleanField(default=True)),
                ('remarks', models.TextField(blank=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_stones', to=settings.AUTH_USER_MODEL)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gave_stones', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='grading.stone')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='received_stones', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParcelTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initiated_date', models.DateTimeField(auto_now_add=True)),
                ('confirmed_date', models.DateTimeField(blank=True, null=True)),
                ('fresh', models.BooleanField(default=True)),
                ('remarks', models.TextField(blank=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_parcels', to=settings.AUTH_USER_MODEL)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gave_parcels', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='grading.parcel')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='received_parcels', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='stonetransfer',
            constraint=models.UniqueConstraint(condition=models.Q(fresh=True), fields=('item',), name='only_one_fresh_transfer_per_stone'),
        ),
        migrations.AddConstraint(
            model_name='parceltransfer',
            constraint=models.UniqueConstraint(condition=models.Q(fresh=True), fields=('item',), name='only_one_fresh_transfer_per_parcel'),
        ),
    ]
