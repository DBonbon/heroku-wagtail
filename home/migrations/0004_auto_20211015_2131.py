# Generated by Django 3.2.7 on 2021-10-15 19:31

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0003_remove_homepage_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='cover_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='sub_teaser',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='teaser',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]