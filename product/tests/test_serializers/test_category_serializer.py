from django.test import TestCase

from product.factories import CategoryFactory, ProductFactory
from product.serializers import CategorySerializer


class TestCategorySerializer(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory(title="food")
        self.category_serializer = CategorySerializer(self.category)

    def test_order_serializer(self):
        serializer_data = self.category_serializer.data

        self.assertEqual(serializer_data["title"], "food")

# import pytest
# from product.models.category import Category
# from product.serializers import CategorySerializer

# @pytest.mark.django_db
# def test_category_serializer():
#     category = Category.objects.create(
#         title="Eletrônicos",
#         slug="eletronicos",
#         description="Categoria de produtos eletrônicos",
#         active=True
#     )

#     serializer = CategorySerializer(category)
    
#     expected_data = {
#         'title': 'Eletrônicos',
#         'slug': 'eletronicos',
#         'description': 'Categoria de produtos eletrônicos',
#         'active': True
#     }

#     assert serializer.data == expected_data