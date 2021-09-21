from django.urls import path, include
from rest_framework.routers import DefaultRouter

from order.views import ItemViewSet, OrderViewSet, CustomerViewSet, transaction_awk

router = DefaultRouter()
router.register('item', ItemViewSet)
router.register('checkout', OrderViewSet)
router.register('customer', CustomerViewSet)
# router.register('employees', CompanyViewSet)
# router.register('employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('transactionAwk', transaction_awk)
]
