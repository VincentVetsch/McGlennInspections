from django.db import models
TYPE_CHOICE = (
    ('P', 'Parent'),
    ('C', 'Child'),
    ('I', 'Individual')
)


# TODO - run syncdb, after you have verified the fields
# TODO - look at ways of using a second table as a fk
# TODO - look at nano apps
# Create your models here.
class Navigation(models.Model):
    '''
        Navigation:  This model is for creating site navigation
        links.  This application should be used as an extension
        for the base.html file for the site or a extension of
        other templates.  This should help easily manage links
        for the site.  There shouldn't be any views.py, just the
        admin.py.
    '''

    title = models.CharField(max_length=100,
                             help_text="This is the title for the link"
                            )
    slug = models.SlugField(unique=True)
    # DONE - Research models.UrlField for links
    link = models.URLField(max_length=200,
                            blank=True,
                            help_text="This is the http link"
                           )
    # Type is either parent, individual or child
    type_of_link = models.CharField(max_length=1,
                                    choices=TYPE_CHOICE,
                                    help_text="The type of link or element"
                                   )
    # Parent of link
    parent = models.CharField(max_length=100,
                              blank=True,
                              help_text="The parent of the link"
                             )
    # Level of the navigation
    level = models.IntegerField()
    div_class = models.CharField(max_length=20)
    icon_field = models.ImageField(
        upload_to="images/navigation/",
        help_text="32x32px image",
        blank=True
    )

    def __unicode__(self):
        return self.title
