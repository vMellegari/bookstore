from django.test import TestCase

from product.factories import CategoryFactory, ProductFactory
from product.serializers import ProductSerializer


class TestProductSerializer(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory(title="technology")
        self.product_1 = ProductFactory(
            title="mouse", price=100, category=[self.category]
        )
        self.product_serializer = ProductSerializer(self.product_1)

    def test_product_serializer(self):
        serializer_data = self.product_serializer.data
        self.assertEqual(serializer_data["price"], 100)
        self.assertEqual(serializer_data["title"], "mouse")
        self.assertEqual(
            serializer_data["category"][0]["title"], "technology")

# import pytest
# from product.models import Product, Category
# from product.serializers import ProductSerializer

# @pytest.mark.django_db
# def test_product_serializer():
#     category1 = Category.objects.create(title="Categoria 1", slug="categoria-1")
#     category2 = Category.objects.create(title="Categoria 2", slug="categoria-2")

#     product = Product.objects.create(
#         title="Produto Teste",
#         description="Descrição do produto de teste",
#         price=150,
#         active=True
#     )
    
#     product.category.set([category1, category2])

#     serializer = ProductSerializer(product)
    
#     expected_data = {
#         'title': 'Produto Teste',
#         'description': 'Descrição do produto de teste',
#         'price': 150,
#         'active': True,
#         'category': [
#             {'title': 'Categoria 1', 'slug': 'categoria-1', 'description': None, 'active': True},
#             {'title': 'Categoria 2', 'slug': 'categoria-2', 'description': None, 'active': True}
#         ]
#     }

#     assert serializer.data == expected_data