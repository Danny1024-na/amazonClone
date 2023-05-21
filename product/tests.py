from django.test import TestCase

# Create your tests here.
def test_product_list_view(self):
    response =self.client.get('/amazonclone')
    self.assertEqual(response.status_code,200)

def text_views_uses_correct_template(self):
    response = self.client.get('/amazonclone')
    self.assertTemplateUsed(response ,'product_list.html')

