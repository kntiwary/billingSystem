from django.urls import path, include
from rest_framework.routers import DefaultRouter

from order.views import ItemViewSet, OrderViewSet, CustomerViewSet

router = DefaultRouter()
router.register('item', ItemViewSet)
router.register('checkout', OrderViewSet)
router.register('customer', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls))
]
