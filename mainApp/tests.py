from django.test import TestCase,Client
from django.core.urlresolvers import resolve

#local imports
from . import views

# Create your tests here.

class WasisiAppTestBase(TestCase):
    """
    Base class for unit testing of mainApp
    """

    def setUp(self):
        """
        Every test needs a client.
        """
        self.client = Client()

    def url_resolves(self,url,name):
        """
        Helper function to resolve the given url to the given name
        and test whethere this is true
        """
        found = resolve(url)
        self.assertEqual(found.func,name)

    def template_used_is(self,url,template):
        """
        The response returned by accessing the given url uses the
        given template
        """
        response = self.client.get(url)
        self.assertTemplateUsed(response,template)

    def response_is_200(self,url):
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

#=======================================================================
#=======================================================================

class MainPageTest(WasisiAppTestBase):
    """
    Class for testing index page functionality
    """

    def test_index_url_resolves_to_(self):
        """
        Test: the url view  resolves to the correct view function.
        """
        self.url_resolves('/',views.index)


    def test_index_url_response_is_200(self):
        """
            Test: the url view returns 200 OK.
        """
        self.response_is_200('/')

    def test_index_template(self):
        """
        Test: the template index is the correct on
        """
        self.template_used_is('/','wasisi/index.html')


