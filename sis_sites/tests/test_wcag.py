# TODO: add CI for WCAG test
# from comet.models import Indicator
# from django.core.urlresolvers import reverse
# from django.test import TestCase
# from wcag_zoo.validators.tarsier import Tarsier


# class WCAGTestCase(TestCase):
#     views = ['lo_home']

#     def test_browse_pages(self):
#         instance = Tarsier()

#         for view in self.views:
#             # visit page
#             response = self.client.get(reverse(view))

#             results = instance.validate_document(response.content)
#             self.assertFalse(results['failed'], results)
