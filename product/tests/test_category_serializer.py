import pytest
from product.models.category import Category
from product.serializers import CategorySerializer

@pytest.mark.django_db
def test_category_serializer():
    category = Category.objects.create(
        title="Eletrônicos",
        slug="eletronicos",
        description="Categoria de produtos eletrônicos",
        active=True
    )

    serializer = CategorySerializer(category)
    
    expected_data = {
        'title': 'Eletrônicos',
        'slug': 'eletronicos',
        'description': 'Categoria de produtos eletrônicos',
        'active': True
    }

    assert serializer.data == expected_data