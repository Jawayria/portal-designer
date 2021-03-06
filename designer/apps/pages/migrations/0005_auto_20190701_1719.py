# Generated by Django 1.11.21 on 2019-07-01 17:19

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('branding', '0001_initial'),
        ('pages', '0004_auto_20190613_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexPageBranding',
            fields=[
                ('branding_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='branding.Branding')),
                ('site_title', models.CharField(blank=True, max_length=128, null=True, verbose_name='Site Title')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='branding', to='pages.IndexPage', unique=True)),
            ],
            bases=('branding.branding',),
        ),
        migrations.CreateModel(
            name='ProgramPageBranding',
            fields=[
                ('branding_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='branding.Branding')),
                ('program_title', models.CharField(blank=True, max_length=128, null=True, verbose_name='Program Title')),
            ],
            bases=('branding.branding',),
        ),
        migrations.AlterField(
            model_name='programpage',
            name='uuid',
            field=models.UUIDField(unique=True),
        ),
        migrations.AddField(
            model_name='programpagebranding',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='branding', to='pages.ProgramPage', unique=True),
        ),
    ]
