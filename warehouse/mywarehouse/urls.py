from rest_framework.routers import DefaultRouter
from .views import InflowViewSet, OutflowViewSet


router = DefaultRouter()
router.register('inflow', InflowViewSet, basename='track-inflow')
router.register('outflow', OutflowViewSet, basename='track-outflow')

urlpatterns = [
    
] + router.urls