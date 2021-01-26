# Generated by Django 3.1.4 on 2021-01-25 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("grading", "0001_initial")]

    operations = [
        migrations.RemoveField(model_name="stone", name="sheryl_symmetry"),
        migrations.RemoveField(model_name="stone", name="symmetry_grade"),
        migrations.AddField(
            model_name="stone",
            name="final_sarine_cut",
            field=models.CharField(
                choices=[("EX", "Excellent"), ("VG", "Very Good"), ("GOOD", "Good"), ("F", "Fair"), ("P", "Poor")],
                default="EX",
                max_length=4,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="stone",
            name="final_sheryl_cut",
            field=models.CharField(
                choices=[("EX", "Excellent"), ("VG", "Very Good"), ("GOOD", "Good"), ("F", "Fair"), ("P", "Poor")],
                default="EX",
                max_length=4,
            ),
            preserve_default=False,
        ),
    ]
