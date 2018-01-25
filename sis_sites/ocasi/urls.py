from django.conf.urls import include, url
from django.views.generic import TemplateView
from sis_sites.ocasi.views import BrowseRegistry, MyWorkspaceView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='sis_sites/ocasi/home.html'), name="ocasi_home"),
    url(r'^help/$', TemplateView.as_view(template_name='sis_sites/ocasi/help.html'), name="ocasi_help"),
    url(r'^data-portal/$', TemplateView.as_view(template_name='sis_sites/ocasi/data_portal.html'), name="ocasi_data_portal"),

    url(r'^evaluation/$', TemplateView.as_view(template_name='sis_sites/ocasi/evaluation.html'), name="ocasi_evaluation"),
    url(r'^evaluation/create-logic-model/$', TemplateView.as_view(template_name='sis_sites/ocasi/create_logic_model.html'), name="ocasi_create_logic_model"),
    url(r'^evaluation/design-evaluation-plan/$', TemplateView.as_view(template_name='sis_sites/ocasi/evaluation_plan.html'), name="ocasi_evaluation_plan"),
    url(r'^evaluation/review-data-collection-tools/$', TemplateView.as_view(template_name='sis_sites/ocasi/review_data_collection_tools.html'), name="ocasi_review_data_collection_tools"),

    url(r'^registry/$', BrowseRegistry.as_view(), name="ocasi_registry"),
    url(r'^my-workspace/$', MyWorkspaceView.as_view(), name="ocasi_my_workspace"),

    url(r'^', include('logicaloutcomes.urls')),
]
