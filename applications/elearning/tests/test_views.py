import pytest
from django.core import mail
from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from django.test import RequestFactory
from mock import patch
from mixer.backend.django import Mixer
# from mixer.backend.django import mixer
mixer = Mixer(fake=False)
pytestmark = pytest.mark.django_db
from django.test import TestCase
from django.core.urlresolvers import reverse, resolve

from applications.mainapp.models import Product
from applications.mainapp import views
from applications.mainapp.forms  import ProductForm
from django.test import Client, RequestFactory
from django.test import TestCase, LiveServerTestCase
from django.contrib.auth.models import User

from mock import patch, MagicMock

# NB rf is the pytest.fixture for RequestFactory that comes with pytest-django 


class BaseAcceptanceTest(LiveServerTestCase):
    def setUp(self):
        self.client = Client()
        
class TestCRUDonProduct(TestCase):
    def setUp(self):
        super(TestCRUDonProduct, self).setUp()
        self.user = mixer.blend('auth.User')
        self.product = mixer.blend(Product)

    def tearDown(self):
        super(TestCRUDonProduct, self).tearDown()
        Product.objects.all().delete()
        User.objects.all().delete()

    #Create-rund
    @patch('applications.mainapp.models.Product.save', MagicMock(name="save"))
    def test_ProductCreateView_shoud_create_a_product(self):
        Product.objects.all().delete()
        '''
        In order to Create a product:
            -I need to create a user
            -I need to create a Product
            -I need to prepare and POST my data
            -I need to add Assign a user to the Request
            -I need post the request to the CreateView
        In the final I have a New Product added into the DB
        '''
        #Create user
        user = mixer.blend('auth.User', username='fred', password='secret')
        #create Product
        product = mixer.blend('mainapp.Product')

        #create another Product through Views
        factory = RequestFactory()
        #url = reverse('wadiyabi:product_create')
        request = factory.post(reverse('wadiyabi:product_create'), data={
            'showoff': 'foo',
            'quantity': 3,
            'price': 34,
        })
        request.user = user
        #get the response
        response = views.ProductCreateView.as_view()(request)

        #assertion
        #pytest.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Product.save.called)
        self.assertEqual(Product.save.call_count, 1)

    #c-Read-ud
    def test_ProductDetailView(self):
        #Create user an logged in
        user = mixer.blend('auth.User', username='fred', password='secret')

        #create product
        products = mixer.cycle(20).blend('mainapp.Product')
        product = Product.objects.first()

        #try to access the delete url
        url = reverse('wadiyabi:product_detail', args=(product.id,))
        response = RequestFactory().get(url)

        #assign a user to the response
        response.user = user
        response = views.ProductDetailView.as_view()(response, pk=product.pk)

        #assert
        self.assertEqual(response.status_code, 200)

    #cr-Update-d
    #@pytest.mark.skip(reason="not implemented")
    def test_ProductUpdateView_should_update_the_product_content(self):
        #Delete all Products
        Product.objects.all().delete()

        #Create user (fixture)
        user = mixer.blend('auth.User', is_superuser=True)

        #create a Product (fixture)
        product = mixer.blend('mainapp.Product')

        #Fields to update
        data = dict( showoff='showoff 33333', )

        #Preparing to post to the Update url
        url = reverse('wadiyabi:product_update', kwargs={'pk': product.pk})
        request = RequestFactory().post(url, data=data)

        #assign a user
        request.user = user

        #Post to Update URL
        response = views.ProductUpdateView.as_view()(request, pk=product.pk)
        
        #Assertion: status code
        self.assertEqual(response.status_code, 200)
        #Refresh the db and Get the latest Product
        product.refresh_from_db()
        product = Product.objects.get(pk=product.pk)
        #pytest.set_trace()

        #Assertion
        #self.assertEqual(product.showoff, data['showoff'])

    #cru-Delete
    def test_ProductDeleteView_should_delete_and_redirect(self):
        Product.objects.all().delete()
        User.objects.all().delete()
        user = mixer.blend('auth.User', is_superuser=True)
        product = Product.objects.first()
        client = Client()
        #response = client.delete(reverse('wadiyabi:product_delete', args=(product.id,)))
        response = client.delete('/wadiyabi/delete/1')
        self.assertEqual(response.reason_phrase, 'Found')
        self.assertEqual(response.wsgi_request.method, 'DELETE')
        self.assertEqual(response.status_code, 302)
        count_number_of_products = Product.objects.all().count()
        #pytest.set_trace()
        self.assertEqual(0, count_number_of_products)


class TestBuyProducts(TestCase):

    def setUp(self):
        self.user     = mixer.blend(User, username='testuser') 
        self.users    = mixer.cycle().blend(User)
        self.product  =  mixer.blend(Product, author=self.user)
        self.products =  mixer.cycle().blend(Product, author=self.user)
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

    def tearDown(self):
        Product.objects.all().delete()
        User.objects.all().delete()

    @pytest.mark.first
    def test_user_can_buy_a_product(self):
        '''
        In order to Buy a product:
            -When a User click on the BUY button 
            -If get directed to the Buy page
        '''
        user = mixer.blend(User)
        user.set_password('12345')
        user.save()

        product = mixer.blend('mainapp.Product', author=user)
        
        client = Client()
        
        #selling the first Product
        url = reverse('wadiyabi:product_selling', args=(product.id,))
        #pytest.set_trace()
        request = client.post(url)
        request.user = user
        #get the response
        response = views.ProductSelling.as_view()(request)

        #assertion
        #pytest.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Product.save.called)
        self.assertEqual(Product.save.call_count, 1)


    @pytest.mark.skip(reason="not implemented")
    def test_user_can_buy_a_product_that_doesn_t_belongs_to_him(self):
        pass

    @pytest.mark.skip(reason="not implemented")
    def test_user_who_have_sold_a_product_has_one_less_product(self):
        pass

    @pytest.mark.skip(reason="not implemented")
    def test_checkout_response_true(self):
        pass

    @pytest.mark.skip(reason="not implemented")
    def test_checkout_credit_card_got_refuse(self):
        pass

class TestFollowers(TestCase):
	def test_init(self):
		pass

class TestComments(TestCase):
	def test_init(self):
		pass


#UserProfile
#Like
#follow
#block

'''
In order to test:
    I need to create a User
    I need to create a Product
    I need to update the field that I want to update on the recent Product
    I need to get a url or prepare the url
    I need to mock the request with the data
'''