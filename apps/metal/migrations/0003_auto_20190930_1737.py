# Generated by Django 2.2.5 on 2019-09-30 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metal', '0002_auto_20190928_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementtraceassay',
            name='aluminum_percent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='aluminum_ppm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='cerium_percent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='cerium_ppm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='lanthanum_percent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='lanthanum_ppm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='magnesium_percent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='magnesium_ppm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='mercury_percent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='mercury_ppm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='molybdenum_percent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='molybdenum_ppm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='phosphorous_percent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='phosphorous_ppm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='platinum_percent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='platinum_ppm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='rhodium_percent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='rhodium_ppm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='scandium_percent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='scandium_ppm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='silicon_percent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='silicon_ppm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='sodium_percent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='sodium_ppm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='tantalum_percent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='tantalum_ppm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='titanium_percent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='titanium_ppm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='tungsten_percent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='tungsten_ppm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='uranium_percent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='uranium_ppm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='vanadium_percent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='elementtraceassay',
            name='vanadium_ppm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='metal',
            name='element_trace_assay_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='metal.ElementTraceAssay'),
        ),
    ]
