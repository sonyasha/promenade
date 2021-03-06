# Generated by Django 2.1 on 2018-10-23 00:07

from django.db import migrations, models
from promenade.utils import unique_slug_generator

def update_slug(apps, schema_editor):
    SinglePoint = apps.get_model('paths', 'SinglePoint')

    for point in SinglePoint.objects.all():
        if not point.slug:
            point.slug = unique_slug_generator(point, point.name, point.slug)
            point.save()


class Migration(migrations.Migration):

    dependencies = [
        ('paths', '0005_auto_20181021_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='singlepoint',
            name='slug',
            field=models.SlugField(blank=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='singlepoint',
            name='name',
            field=models.CharField(max_length=70),
        ),
        migrations.RunPython(update_slug, reverse_code=migrations.RunPython.noop),
    ]
