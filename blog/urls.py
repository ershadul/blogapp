from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^all$', 'blog.views.all_posts'),
    # url(r'^blog/', include('blog.urls')),
)