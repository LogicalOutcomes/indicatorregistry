from django.conf.urls import patterns, include, url
from logicaloutcomes.local import views

# Below are the 'recommended' locations for the paths to aristotle extensions.
urlpatterns = patterns('',
    url(r'^/?$', views.home, name='lo_home'),
    url(r'^comparer/?$', views.comparer, name='comparer'),
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect': '/user/password/done/'},
        name='password_reset_confirm',),
    url(r'^user/password/done/$',
        'django.contrib.auth.views.password_reset_complete'),
    )