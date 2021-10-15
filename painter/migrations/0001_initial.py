# Generated by Django 3.2.7 on 2021-10-15 12:25

from django.db import migrations, models
import django.db.models.deletion
import streams.blocks
import wagtail.contrib.routable_page.models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaintersPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('subtitle', wagtail.core.fields.RichTextField(blank=True, help_text='Catchy, short informative description of the page', max_length=250, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='PainterPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('artist_names', wagtail.core.fields.StreamField([('names', wagtail.core.blocks.StructBlock([('first_name', wagtail.core.blocks.CharBlock(max_length=60)), ('last_name', wagtail.core.blocks.CharBlock(max_length=60))]))])),
                ('artist_dates', wagtail.core.fields.StreamField([('dates', wagtail.core.blocks.StructBlock([('date_of_birth', wagtail.core.blocks.DateBlock()), ('date_of_death', wagtail.core.blocks.DateBlock())]))])),
                ('bio', wagtail.core.fields.RichTextField(null=True)),
                ('pitch', wagtail.core.fields.RichTextField(null=True)),
                ('links', wagtail.core.fields.StreamField([('link', wagtail.core.blocks.StructBlock([('button_title', wagtail.core.blocks.CharBlock(max_length=60, required=False)), ('button_text', streams.blocks.RichtextBlock(features=['bold', 'italic'], required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(help_text='If selected, this url will be used first', required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If added, this url will be used secondarily to the button page', required=False))], blanc=True, null=True))])),
                ('painter_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]