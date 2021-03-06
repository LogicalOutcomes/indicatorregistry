from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url


# Below are the 'recommended' locations for the paths to aristotle extensions.
# At this point the 'glossary' extension *requires* being in the root at `/glossary/`.
urlpatterns = patterns(
    '',
    url(r'^', include('local.urls')),
    url(r'^', include('indicators.urls')),
    url(r'^', include('aristotle_mdr.urls')),
    url(r'^ddi/', include('aristotle_ddi_utils.urls', app_name="aristotle_ddi_utils", namespace="aristotle_ddi_utils")),
    url(r'^dse/', include('aristotle_dse.urls', app_name="aristotle_dse", namespace="aristotle_dse")),
    url(r'^comet/', include('comet.urls', app_name="comet", namespace="comet")),
    url(r'^mallard/', include('mallard_qr.urls', app_name="mallard_qr", namespace="mallard_mdr")),
    url(r'^api/', include('aristotle_mdr_api.urls', app_name="aristotle_mdr_api", namespace="aristotle_mdr_api")),

    # Auth views
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect': '/user/password/done/'},
        name='password_reset_confirm',),
    url(r'^user/password/done/$',
        'django.contrib.auth.views.password_reset_complete'),

    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
)

handler404 = 'local.views.handler404'
handler500 = 'local.views.handler500'
handler403 = 'local.views.handler403'
handler400 = 'local.views.handler400'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
