from django.contrib import admin
from . import models
# from .models import Type, Restaurant, Review

# Setting up the Admin panel

admin.site.site_header = "Restaurants Admin"
admin.site.site_title = "Restaurants"
admin.site.index_title = "Welcome to the Restaurants admin area"

# In Restaurant we see all his reviews


class ReviewInline(admin.TabularInline):
    model = models.Review
    exclude = ['created_at']
    extra = 1


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'place', 'type')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapse']
        })
    ]
    inlines = [ReviewInline]

# In Type we see all his restaurants


class RestaurantsInline(admin.TabularInline):
    model = models.Restaurant
    exclude = ['created_at', 'image']
    extra = 1


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapse']
        })
    ]
    inlines = [RestaurantsInline]


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('note', 'user', 'id', 'stars', 'visit_date')


# Register your models here.
admin.site.register(models.Type, TypeAdmin)
admin.site.register(models.Restaurant, RestaurantAdmin)
admin.site.register(models.Review, ReviewAdmin)
