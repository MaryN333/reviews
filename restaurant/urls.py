from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
# from .views import single_restaurant

app_name = 'restaurant'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:rest_id>', views.single_restaurant, name='single_restaurant'),
    path('<int:rest_id>/create', views.createreview, name='createreview'),
    path('review/<int:review_id>', views.updatereview, name='updatereview'),
    path('review/<int:review_id>/delete',
         views.deletereview, name='deletereview'),
    # path('api/v1/restaurants/<int:restaurant_id>/reviews/',
    #      single_restaurant, name='restaurant-reviews'),
]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
