from django.db import models
TYPE_CHOICE = (
    ('P', 'Parent'),
    ('C', 'Child'),
    ('I', 'Individual')
)


# DONE - Run syncdb, after you have verified the fields
# DONE - Look at ways of using a second table as a fk
# TODO - Look at nano apps
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
    # DONE - Doesn't seem to allow Django links
    link = models.CharField(max_length=200,
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


def create_link_item(title, link, link_type):
    '''create_link_item:  Creates a link item for a sliding menu effect
       Arguments:
           title:   The title of the hyperlink
           link:    The address of the hyperlink
       Returns:     A list item with achor tags
    '''
    if link_type == 'I':
        listitem = '  <li class="sliding-element">'
    elif link_type == 'C':
        listitem = '      <li class="sliding-element">'
    else:
        return "<p><b>Failure<b></p>"
    anchor = '<a href="' + link + '">'
    endanchor = '</a></li>\n'
    return listitem + anchor + title + endanchor


def get_navigation():
    '''get_navigation:  Gets the navigation information
        Returns:  The navigation links A Navigation object
    '''
    output_string = '<h4 class="nav-title">Main</h4>\n<div>\n'
    output_string += '<ul id="sliding-navigation">\n'
    n = Navigation.objects.all()
    individuals = n.filter(type_of_link='I')
    parents = n.filter(type_of_link='P')
    children = n.filter(type_of_link='C')
    for i in individuals:
        output_string += create_link_item(i.title, i.link, 'I')
    output_string += '</ul>\n</div>\n'
    for p in parents:
        output_string += '<h6 class="nav-title">' + p.title + '</h6>\n<div class="nav-div">\n'
        output_string += '<ul id="sliding-navigation">\n'
        for c in children:
            if c.parent == p.div_class:
                output_string += create_link_item(c.title, c.link, 'C')
        output_string += '</ul>\n</div>\n'
    output_string += '</ul>\n'
    return output_string
