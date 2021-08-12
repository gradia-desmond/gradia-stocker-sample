# Generated by Django 3.1.4 on 2021-08-12 02:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stonegrading', '0002_auto_20210812_0215'),
        ('customers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GiaVerification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_number', models.CharField(blank=True, max_length=10)),
                ('invoice_number', models.CharField(blank=True, max_length=10)),
                ('started', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoldwayVerification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_order', models.CharField(blank=True, max_length=10)),
                ('invoice_number', models.CharField(blank=True, max_length=10)),
                ('started', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_parcel_code', models.CharField(max_length=15)),
                ('total_carats', models.DecimalField(decimal_places=3, max_digits=5)),
                ('total_pieces', models.IntegerField()),
                ('reference_price_per_carat', models.PositiveIntegerField()),
                ('gradia_parcel_code', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Split',
            fields=[
                ('original_parcel', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='grading.parcel')),
                ('split_date', models.DateTimeField(auto_now_add=True)),
                ('split_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('intake_date', models.DateTimeField(auto_now_add=True)),
                ('release_date', models.DateTimeField(blank=True, null=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.entity')),
                ('intake_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='signed_off_on_stone_intake', to=settings.AUTH_USER_MODEL)),
                ('release_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='signed_off_on_stone_release', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'customer receipt',
            },
        ),
        migrations.AddField(
            model_name='parcel',
            name='receipt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='grading.receipt'),
        ),
        migrations.CreateModel(
            name='Stone',
            fields=[
                ('giagradingadjustmixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stonegrading.giagradingadjustmixin')),
                ('basic_diamond_description', models.CharField(blank=True, choices=[('NATURAL', 'Natural'), ('UNNATURAL', 'Unnatural')], max_length=15, null=True)),
                ('basic_carat', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('basic_color_1', models.CharField(blank=True, choices=[('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J')], max_length=1, null=True)),
                ('basic_color_2', models.CharField(blank=True, choices=[('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J')], max_length=1, null=True)),
                ('basic_color_3', models.CharField(blank=True, choices=[('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J')], max_length=1, null=True)),
                ('basic_color_final', models.CharField(blank=True, choices=[('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J')], max_length=1, null=True)),
                ('basic_clarity_1', models.CharField(blank=True, choices=[('IF+', 'IF+'), ('IF', 'IF'), ('IF-', 'IF-'), ('VVS1+', 'VVS1+'), ('VVS1', 'VVS1'), ('VVS1-', 'VVS1-'), ('VVS2+', 'VVS2+'), ('VVS2', 'VVS2'), ('VVS2-', 'VVS2-'), ('VS1+', 'VS1+'), ('VS1', 'VS1'), ('VS1-', 'VS1-'), ('VS2+', 'VS2+'), ('VS2', 'VS2'), ('VS2-', 'VS2-'), ('SI1+', 'SI1+'), ('SI1', 'SI1'), ('SI1-', 'SI1-'), ('SI2+', 'SI2+'), ('SI2', 'SI2'), ('SI2-', 'SI2-'), ('I1+', 'I1+'), ('I1', 'I1'), ('I1-', 'I1-')], max_length=5, null=True)),
                ('basic_clarity_2', models.CharField(blank=True, choices=[('IF+', 'IF+'), ('IF', 'IF'), ('IF-', 'IF-'), ('VVS1+', 'VVS1+'), ('VVS1', 'VVS1'), ('VVS1-', 'VVS1-'), ('VVS2+', 'VVS2+'), ('VVS2', 'VVS2'), ('VVS2-', 'VVS2-'), ('VS1+', 'VS1+'), ('VS1', 'VS1'), ('VS1-', 'VS1-'), ('VS2+', 'VS2+'), ('VS2', 'VS2'), ('VS2-', 'VS2-'), ('SI1+', 'SI1+'), ('SI1', 'SI1'), ('SI1-', 'SI1-'), ('SI2+', 'SI2+'), ('SI2', 'SI2'), ('SI2-', 'SI2-'), ('I1+', 'I1+'), ('I1', 'I1'), ('I1-', 'I1-')], max_length=5, null=True)),
                ('basic_clarity_3', models.CharField(blank=True, choices=[('IF+', 'IF+'), ('IF', 'IF'), ('IF-', 'IF-'), ('VVS1+', 'VVS1+'), ('VVS1', 'VVS1'), ('VVS1-', 'VVS1-'), ('VVS2+', 'VVS2+'), ('VVS2', 'VVS2'), ('VVS2-', 'VVS2-'), ('VS1+', 'VS1+'), ('VS1', 'VS1'), ('VS1-', 'VS1-'), ('VS2+', 'VS2+'), ('VS2', 'VS2'), ('VS2-', 'VS2-'), ('SI1+', 'SI1+'), ('SI1', 'SI1'), ('SI1-', 'SI1-'), ('SI2+', 'SI2+'), ('SI2', 'SI2'), ('SI2-', 'SI2-'), ('I1+', 'I1+'), ('I1', 'I1'), ('I1-', 'I1-')], max_length=5, null=True)),
                ('basic_clarity_final', models.CharField(blank=True, choices=[('IF+', 'IF+'), ('IF', 'IF'), ('IF-', 'IF-'), ('VVS1+', 'VVS1+'), ('VVS1', 'VVS1'), ('VVS1-', 'VVS1-'), ('VVS2+', 'VVS2+'), ('VVS2', 'VVS2'), ('VVS2-', 'VVS2-'), ('VS1+', 'VS1+'), ('VS1', 'VS1'), ('VS1-', 'VS1-'), ('VS2+', 'VS2+'), ('VS2', 'VS2'), ('VS2-', 'VS2-'), ('SI1+', 'SI1+'), ('SI1', 'SI1'), ('SI1-', 'SI1-'), ('SI2+', 'SI2+'), ('SI2', 'SI2'), ('SI2-', 'SI2-'), ('I1+', 'I1+'), ('I1', 'I1'), ('I1-', 'I1-')], max_length=5, null=True)),
                ('basic_fluorescence_1', models.CharField(blank=True, choices=[('VS', 'Very Strong'), ('S', 'Strong'), ('M', 'Medium'), ('F', 'Faint'), ('N', 'None')], max_length=4, null=True)),
                ('basic_fluorescence_2', models.CharField(blank=True, choices=[('VS', 'Very Strong'), ('S', 'Strong'), ('M', 'Medium'), ('F', 'Faint'), ('N', 'None')], max_length=4, null=True)),
                ('basic_fluorescence_3', models.CharField(blank=True, choices=[('VS', 'Very Strong'), ('S', 'Strong'), ('M', 'Medium'), ('F', 'Faint'), ('N', 'None')], max_length=4, null=True)),
                ('basic_fluorescence_final', models.CharField(blank=True, choices=[('VS', 'Very Strong'), ('S', 'Strong'), ('M', 'Medium'), ('F', 'Faint'), ('N', 'None')], max_length=4, null=True)),
                ('basic_culet_1', models.CharField(blank=True, choices=[('N', 'None'), ('VS', 'Very Small'), ('S', 'Small'), ('M', 'Medium'), ('SL', 'Slightly Large'), ('L', 'Large'), ('VL', 'Very Large'), ('XL', 'Extremely Large')], max_length=2, null=True)),
                ('basic_culet_2', models.CharField(blank=True, choices=[('N', 'None'), ('VS', 'Very Small'), ('S', 'Small'), ('M', 'Medium'), ('SL', 'Slightly Large'), ('L', 'Large'), ('VL', 'Very Large'), ('XL', 'Extremely Large')], max_length=2, null=True)),
                ('basic_culet_3', models.CharField(blank=True, choices=[('N', 'None'), ('VS', 'Very Small'), ('S', 'Small'), ('M', 'Medium'), ('SL', 'Slightly Large'), ('L', 'Large'), ('VL', 'Very Large'), ('XL', 'Extremely Large')], max_length=2, null=True)),
                ('basic_culet_final', models.CharField(blank=True, choices=[('N', 'None'), ('VS', 'Very Small'), ('S', 'Small'), ('M', 'Medium'), ('SL', 'Slightly Large'), ('L', 'Large'), ('VL', 'Very Large'), ('XL', 'Extremely Large')], max_length=2, null=True)),
                ('basic_culet_characteristic_1', models.CharField(blank=True, choices=[('N', 'None'), ('SAB', 'Slightly Abraded'), ('CH', 'Chipped')], max_length=5, null=True)),
                ('basic_culet_characteristic_2', models.CharField(blank=True, choices=[('N', 'None'), ('SAB', 'Slightly Abraded'), ('CH', 'Chipped')], max_length=5, null=True)),
                ('basic_culet_characteristic_3', models.CharField(blank=True, choices=[('N', 'None'), ('SAB', 'Slightly Abraded'), ('CH', 'Chipped')], max_length=5, null=True)),
                ('basic_culet_characteristic_final', models.CharField(blank=True, choices=[('N', 'None'), ('SAB', 'Slightly Abraded'), ('CH', 'Chipped')], max_length=5, null=True)),
                ('basic_girdle_characteristic_1', models.CharField(blank=True, choices=[('FAC', 'Faceted'), ('POL', 'Polished'), ('BRU', 'Bruted')], max_length=3, null=True)),
                ('basic_girdle_characteristic_2', models.CharField(blank=True, choices=[('FAC', 'Faceted'), ('POL', 'Polished'), ('BRU', 'Bruted')], max_length=3, null=True)),
                ('basic_girdle_characteristic_3', models.CharField(blank=True, choices=[('FAC', 'Faceted'), ('POL', 'Polished'), ('BRU', 'Bruted')], max_length=3, null=True)),
                ('basic_girdle_characteristic_final', models.CharField(blank=True, choices=[('FAC', 'Faceted'), ('POL', 'Polished'), ('BRU', 'Bruted')], max_length=3, null=True)),
                ('basic_polish_1', models.CharField(blank=True, choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('GD', 'Good'), ('F', 'Fair'), ('P', 'Poor')], max_length=4, null=True)),
                ('basic_polish_2', models.CharField(blank=True, choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('GD', 'Good'), ('F', 'Fair'), ('P', 'Poor')], max_length=4, null=True)),
                ('basic_polish_3', models.CharField(blank=True, choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('GD', 'Good'), ('F', 'Fair'), ('P', 'Poor')], max_length=4, null=True)),
                ('basic_polish_final', models.CharField(blank=True, choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('GD', 'Good'), ('F', 'Fair'), ('P', 'Poor')], max_length=4, null=True)),
                ('basic_girdle_min_grade_final', models.CharField(blank=True, choices=[('ETN', 'Extremely Thin'), ('VTN', 'Very Thin'), ('THN', 'Thin'), ('MED', 'Medium'), ('STK', 'Slightly Thick'), ('THK', 'Thick'), ('VTK', 'Very Thick'), ('ETK', 'Extremely Thick')], max_length=10, null=True)),
                ('basic_remarks', models.TextField(blank=True, null=True)),
                ('date_from_gw', models.DateTimeField(blank=True, null=True)),
                ('gw_return_reweight', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('gw_color', models.CharField(blank=True, choices=[('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J')], max_length=1, null=True)),
                ('gw_clarity', models.CharField(blank=True, choices=[('IF+', 'IF+'), ('IF', 'IF'), ('IF-', 'IF-'), ('VVS1+', 'VVS1+'), ('VVS1', 'VVS1'), ('VVS1-', 'VVS1-'), ('VVS2+', 'VVS2+'), ('VVS2', 'VVS2'), ('VVS2-', 'VVS2-'), ('VS1+', 'VS1+'), ('VS1', 'VS1'), ('VS1-', 'VS1-'), ('VS2+', 'VS2+'), ('VS2', 'VS2'), ('VS2-', 'VS2-'), ('SI1+', 'SI1+'), ('SI1', 'SI1'), ('SI1-', 'SI1-'), ('SI2+', 'SI2+'), ('SI2', 'SI2'), ('SI2-', 'SI2-'), ('I1+', 'I1+'), ('I1', 'I1'), ('I1-', 'I1-')], max_length=5, null=True)),
                ('gw_fluorescence', models.CharField(blank=True, choices=[('VS', 'Very Strong'), ('S', 'Strong'), ('M', 'Medium'), ('F', 'Faint'), ('N', 'None')], max_length=5, null=True)),
                ('gw_remarks', models.TextField(blank=True, null=True)),
                ('gw_color_adjusted_1', models.CharField(blank=True, choices=[('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J')], max_length=1, null=True)),
                ('gw_color_adjusted_2', models.CharField(blank=True, choices=[('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J')], max_length=1, null=True)),
                ('gw_color_adjusted_3', models.CharField(blank=True, choices=[('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J')], max_length=1, null=True)),
                ('gw_color_adjusted_final', models.CharField(blank=True, choices=[('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J')], max_length=1, null=True)),
                ('gw_clarity_adjusted_1', models.CharField(choices=[('IF+', 'IF+'), ('IF', 'IF'), ('IF-', 'IF-'), ('VVS1+', 'VVS1+'), ('VVS1', 'VVS1'), ('VVS1-', 'VVS1-'), ('VVS2+', 'VVS2+'), ('VVS2', 'VVS2'), ('VVS2-', 'VVS2-'), ('VS1+', 'VS1+'), ('VS1', 'VS1'), ('VS1-', 'VS1-'), ('VS2+', 'VS2+'), ('VS2', 'VS2'), ('VS2-', 'VS2-'), ('SI1+', 'SI1+'), ('SI1', 'SI1'), ('SI1-', 'SI1-'), ('SI2+', 'SI2+'), ('SI2', 'SI2'), ('SI2-', 'SI2-'), ('I1+', 'I1+'), ('I1', 'I1'), ('I1-', 'I1-')], max_length=5)),
                ('gw_clarity_adjusted_2', models.CharField(choices=[('IF+', 'IF+'), ('IF', 'IF'), ('IF-', 'IF-'), ('VVS1+', 'VVS1+'), ('VVS1', 'VVS1'), ('VVS1-', 'VVS1-'), ('VVS2+', 'VVS2+'), ('VVS2', 'VVS2'), ('VVS2-', 'VVS2-'), ('VS1+', 'VS1+'), ('VS1', 'VS1'), ('VS1-', 'VS1-'), ('VS2+', 'VS2+'), ('VS2', 'VS2'), ('VS2-', 'VS2-'), ('SI1+', 'SI1+'), ('SI1', 'SI1'), ('SI1-', 'SI1-'), ('SI2+', 'SI2+'), ('SI2', 'SI2'), ('SI2-', 'SI2-'), ('I1+', 'I1+'), ('I1', 'I1'), ('I1-', 'I1-')], max_length=5)),
                ('gw_clarity_adjusted_3', models.CharField(choices=[('IF+', 'IF+'), ('IF', 'IF'), ('IF-', 'IF-'), ('VVS1+', 'VVS1+'), ('VVS1', 'VVS1'), ('VVS1-', 'VVS1-'), ('VVS2+', 'VVS2+'), ('VVS2', 'VVS2'), ('VVS2-', 'VVS2-'), ('VS1+', 'VS1+'), ('VS1', 'VS1'), ('VS1-', 'VS1-'), ('VS2+', 'VS2+'), ('VS2', 'VS2'), ('VS2-', 'VS2-'), ('SI1+', 'SI1+'), ('SI1', 'SI1'), ('SI1-', 'SI1-'), ('SI2+', 'SI2+'), ('SI2', 'SI2'), ('SI2-', 'SI2-'), ('I1+', 'I1+'), ('I1', 'I1'), ('I1-', 'I1-')], max_length=5)),
                ('gw_clarity_adjusted_final', models.CharField(choices=[('IF+', 'IF+'), ('IF', 'IF'), ('IF-', 'IF-'), ('VVS1+', 'VVS1+'), ('VVS1', 'VVS1'), ('VVS1-', 'VVS1-'), ('VVS2+', 'VVS2+'), ('VVS2', 'VVS2'), ('VVS2-', 'VVS2-'), ('VS1+', 'VS1+'), ('VS1', 'VS1'), ('VS1-', 'VS1-'), ('VS2+', 'VS2+'), ('VS2', 'VS2'), ('VS2-', 'VS2-'), ('SI1+', 'SI1+'), ('SI1', 'SI1'), ('SI1-', 'SI1-'), ('SI2+', 'SI2+'), ('SI2', 'SI2'), ('SI2-', 'SI2-'), ('I1+', 'I1+'), ('I1', 'I1'), ('I1-', 'I1-')], max_length=5)),
                ('gw_fluorescence_adjusted_1', models.CharField(blank=True, choices=[('VS', 'Very Strong'), ('S', 'Strong'), ('M', 'Medium'), ('F', 'Faint'), ('N', 'None')], max_length=4, null=True)),
                ('gw_fluorescence_adjusted_2', models.CharField(blank=True, choices=[('VS', 'Very Strong'), ('S', 'Strong'), ('M', 'Medium'), ('F', 'Faint'), ('N', 'None')], max_length=4, null=True)),
                ('gw_fluorescence_adjusted_3', models.CharField(blank=True, choices=[('VS', 'Very Strong'), ('S', 'Strong'), ('M', 'Medium'), ('F', 'Faint'), ('N', 'None')], max_length=4, null=True)),
                ('gw_fluorescence_adjusted_final', models.CharField(blank=True, choices=[('VS', 'Very Strong'), ('S', 'Strong'), ('M', 'Medium'), ('F', 'Faint'), ('N', 'None')], max_length=4, null=True)),
                ('gw_adjust_remarks', models.TextField(blank=True, null=True)),
                ('date_from_gia', models.DateTimeField(blank=True, null=True)),
                ('gia_color', models.CharField(blank=True, choices=[('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J')], max_length=1, null=True)),
                ('post_gia_final_color', models.CharField(blank=True, choices=[('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J')], max_length=1, null=True)),
                ('gia_material_testing', models.CharField(blank=True, max_length=20, null=True)),
                ('auto_table_size_rounded_grade', models.CharField(choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('GD', 'Good'), ('F', 'Fair'), ('P', 'Poor')], max_length=4)),
                ('auto_crown_angle_rounded_grade_grade', models.CharField(choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('GD', 'Good'), ('F', 'Fair'), ('P', 'Poor')], max_length=4)),
                ('auto_pavilion_angle_rounded_grade', models.CharField(choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('GD', 'Good'), ('F', 'Fair'), ('P', 'Poor')], max_length=4)),
                ('auto_star_length_rounded_grade', models.CharField(blank=True, choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('GD', 'Good'), ('F', 'Fair'), ('P', 'Poor')], max_length=4, null=True)),
                ('auto_lower_half_rounded_grade', models.CharField(choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('GD', 'Good'), ('F', 'Fair'), ('P', 'Poor')], max_length=4)),
                ('auto_girdle_thick_rounded_grade', models.CharField(blank=True, choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('GD', 'Good'), ('F', 'Fair'), ('P', 'Poor')], max_length=4, null=True)),
                ('auto_girdle_grade', models.CharField(choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('GD', 'Good'), ('F', 'Fair'), ('P', 'Poor')], max_length=4)),
                ('auto_crown_height_rounded_grade', models.CharField(choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('GD', 'Good'), ('F', 'Fair'), ('P', 'Poor')], max_length=4)),
                ('auto_total_depth_rounded_grade', models.CharField(choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('GD', 'Good'), ('F', 'Fair'), ('P', 'Poor')], max_length=4)),
                ('auto_individual_cut_grade_grade', models.CharField(choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('GD', 'Good'), ('F', 'Fair'), ('P', 'Poor')], max_length=4)),
                ('auto_est_table_cut_grade_grade', models.CharField(choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('GD', 'Good'), ('F', 'Fair'), ('P', 'Poor')], max_length=4)),
                ('auto_gradia_cut_grade_grade', models.CharField(choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('GD', 'Good'), ('F', 'Fair'), ('P', 'Poor')], max_length=4)),
                ('auto_final_sarine_cut_grade', models.CharField(choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('GD', 'Good'), ('F', 'Fair'), ('P', 'Poor')], max_length=4)),
                ('auto_final_gradia_cut_grade', models.CharField(choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('GD', 'Good'), ('F', 'Fair'), ('P', 'Poor')], max_length=4)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('internal_id', models.IntegerField(unique=True)),
                ('external_id', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('basic_grader_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='basic_grader_1', to=settings.AUTH_USER_MODEL)),
                ('basic_grader_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='basic_grader_2', to=settings.AUTH_USER_MODEL)),
                ('basic_grader_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='basic_grader_3', to=settings.AUTH_USER_MODEL)),
                ('basic_inclusions_1', models.ManyToManyField(blank=True, related_name='basic_inclusions_1', to='stonegrading.Inclusion')),
                ('basic_inclusions_2', models.ManyToManyField(blank=True, related_name='basic_inclusions_2', to='stonegrading.Inclusion')),
                ('basic_inclusions_3', models.ManyToManyField(blank=True, related_name='basic_inclusions_3', to='stonegrading.Inclusion')),
                ('basic_inclusions_final', models.ManyToManyField(blank=True, related_name='basic_inclusions_final', to='stonegrading.Inclusion')),
                ('data_entry_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='entered_data_for_stone', to=settings.AUTH_USER_MODEL)),
                ('gia_verification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='grading.giaverification')),
                ('gw_adjust_grader_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='gw_adjust_grader_1', to=settings.AUTH_USER_MODEL)),
                ('gw_adjust_grader_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='gw_adjust_grader_2', to=settings.AUTH_USER_MODEL)),
                ('gw_adjust_grader_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='gw_adjust_grader_3', to=settings.AUTH_USER_MODEL)),
                ('gw_verification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='grading.goldwayverification')),
                ('split_from', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='grading.split')),
            ],
            options={
                'abstract': False,
            },
            bases=('stonegrading.giagradingadjustmixin', models.Model),
        ),
        migrations.AddField(
            model_name='parcel',
            name='split_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='grading.split'),
        ),
    ]
