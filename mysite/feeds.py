"""RSS Feed class """

from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post

class LatestEntriesFeed(Feed):
    title = "Blogging Posts"
    link = "/"
    description = "Updates on changes and additions to my blogging site."

    def items(self):
        published = Post.objects.exclude(published_date__exact=None)
        posts = published.order_by('-published_date')
        return posts[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    # item_link is only needed if Post has no get_absolute_url method.
    def item_link(self, item):
        return reverse('blog_detail', args=[item.pk])
