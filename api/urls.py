from django.urls import path, include
from api.models import RestaurantResource, TypeResource, ReviewResource
from tastypie.api import Api

api = Api(api_name='v1')
restaurant_resource = RestaurantResource()
type_resource = TypeResource()
review_resource = ReviewResource()
api.register(restaurant_resource)
api.register(type_resource)
api.register(review_resource)

urlpatterns = [
    path('', include(api.urls), name='index')
]
