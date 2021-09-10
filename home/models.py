from django.db import models
from django.shortcuts import render
# from django_extensions.db.fields import AutoSlugField

from wagtail.core.blocks import CharBlock, PageChooserBlock
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
#from streams import blocks
#from articles.models import ArticlePage, ArticleIndexPage


class HomePageCarouselImages(Orderable):
    """Between 1 and 5 images for the home page carousel."""
    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    carousel_caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel("carousel_image"),
        FieldPanel("carousel_caption"),
    ]

class HomePage(RoutablePageMixin, Page):
    """Home page model."""

    template = "home/home_page.html"
    max_count = 1

    # cover = StreamField(
    #     [('cover', blocks.CoverImageBlock())],
    #     null=True, blank=True,
    # )
    # #     ('image', ImageChooserBlock()),
    #     ('teaser', blocks.RichtextBlock(null=True, blanc=True, features=['h1', 'h2', 'h3', 'h4', "bold", "italic"])),
    #     ('sub_teaser', blocks.RichtextBlock(null=True, blanc=True, features=['h4', 'h5', 'h6', "bold", "italic"])),
    # ])

    banner = StreamField([
        ('image', ImageChooserBlock(blank=True, null=True)),
        ('banner_title', CharBlock(max_length=100, blank=True, null=True)),
        ('banner_sub_title', CharBlock(max_length=100, blank=True, null=True)),
    ], null=True, blank=True)

    # content = StreamField(
    #     [
    #         ("cta", blocks.CTABlock(blank=True, null=True)),
    #     ],
    #     null=True,
    #     blank=True,
    # )

    content_panels = Page.content_panels + [
        # MultiFieldPanel(
        #     [
        #         StreamFieldPanel('cover'),
        #     ],
        #         heading="Cover",
        #         classname="collapsible collapsed",
        # ),

        MultiFieldPanel(
            [
            StreamFieldPanel('banner'),
            ],
            heading="Banner Options",
            classname = "collapsible collapsed",
        ),

        #StreamFieldPanel("content"),

        MultiFieldPanel(
                [InlinePanel("carousel_images", max_num=5, min_num=0, label="Image")],
                heading="Carousel Images",
        ),
    ]


    class Meta:

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


    @route(r'^subscribe/$')
    def the_subscribe_page(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        return render(request, "home/subscribe.html", context)