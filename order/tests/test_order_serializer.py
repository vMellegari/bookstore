import pytest
from django.contrib.auth.models import User
from order.models import Order
from order.serializers import OrderSerializer

@pytest.mark.django_db
def test_order_serializer():
    user = User.objects.create(username="testuser", password="testpassword")
    
    order = Order.objects.create(user=user)
    
    serializer = OrderSerializer(order)
    
    expected_data = {
        'product': [],
        'total': 0.0
    }
    
    assert serializer.data == expected_data