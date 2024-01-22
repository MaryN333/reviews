# from django.db import models
from tastypie.resources import ModelResource
from restaurant.models import Type, Restaurant, Review
from tastypie.authorization import Authorization
from tastypie.authorization import DjangoAuthorization
from .authentication import CustomAuthentication
from tastypie.serializers import Serializer
from tastypie.authentication import BasicAuthentication

from tastypie import fields


class ReviewResource(ModelResource):
    restaurant = fields.ForeignKey(
        'api.models.RestaurantResource', 'restaurant')

    class Meta:
        queryset = Review.objects.all()
        resource_name = 'reviews'
        allowed_methods = ['get']


class TypeResource(ModelResource):
    class Meta:
        queryset = Type.objects.all()
        resource_name = 'types'
        allowed_methods = ['get']  # jen cteni


class RestaurantResource(ModelResource):
    # new
    type = fields.ForeignKey(TypeResource, 'type', full=True)
    image = fields.FileField(attribute="image", null=True, blank=True)
    #

    class Meta:
        queryset = Restaurant.objects.all()
        resource_name = 'restaurants'
        allowed_methods = ['get', 'post', 'delete', 'patch']
        excludes = ['created_at']
        authorization = Authorization()
        # authorization = DjangoAuthorization()
        authentication = CustomAuthentication()
        # new
        # serializer = CustomSerializer()
        #

    def hydrate(self, bundle):
        bundle.obj.type_id = bundle.data['type_id']
        # new
        if 'image_path' in bundle.data and bundle.data['image_path'] is not None:
            bundle.obj.image_path = bundle.data['image_path']
        #
        return bundle

    # V Postman, GET, zobrazi se type
    def dehydrate(self, bundle):
        bundle.data['type_id'] = bundle.obj.type_id
        bundle.data['type'] = bundle.obj.type
        return bundle

    def dehydrate_title(self, bundle):
        return bundle.data['title'].upper()

# new ???
# class CustomSerializer(Serializer):
#     formats = ['json', 'xml', 'text', 'multipart']
#     content_types = {
#         'json': 'application/json',
#         'xml': 'application/xml',
#         'text': 'text/plain',
#         'multipart': 'multipart/form-data',
#     }

#     def deserialize(self, content, format='application/json'):
#         if format == 'multipart':
#             # Обработка 'multipart/form-data'
#             data = self.deserialize_multipart(content)
#         else:
#             data = super(CustomSerializer, self).deserialize(content, format)

#         return data
    #
