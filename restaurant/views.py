from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Restaurant, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count, F, Func, IntegerField


# Create your views here.


def index(request):
    # return HttpResponse("Hello from the Restaurant app")
    searchTerm = request.GET.get('searchRestaurant')
    if searchTerm:
        restaurants = Restaurant.objects.filter(title__icontains=searchTerm)
    else:
        restaurants = Restaurant.objects.all()

    # Number of comments,                  без all
    # posts = restaurants.annotate(num_comments=Count('reviews')).all()
    # Average rating based on reviews
    # stars = Restaurant.objects.annotate(avg_rating=Func(
    #     Avg('reviews__stars'), function='ROUND', output_field=IntegerField()))
    restaurants = restaurants.annotate(num_comments=Count('reviews'), avg_rating=Func(
        Avg('reviews__stars'), function='ROUND', output_field=IntegerField()))
    # restaurants = Restaurant.objects.all()

    # return HttpResponse(''.join([str(rest) + '<br>' for rest in restaurants]))
    # return HttpResponse(restaurants)
    # return render(request=request, template_name='restaurant/restaurants.html', context={'restaurants': restaurants})
    # , 'posts': posts, 'stars': stars})
    return render(request, 'restaurant/restaurants.html', {'restaurants': restaurants, 'searchTerm': searchTerm})


# def single_restaurant(request, rest_id):
    # restaurant = Restaurant.objects.get(pk=rest_id)
    # return render(request, 'restaurant/single_restaurant.html', {'restaurant': restaurant})

    # Option 1
    # try:
    #     restaurant = Restaurant.objects.get(pk=rest_id)
    #     return render(request, 'restaurant/single_restaurant.html', {'restaurant': restaurant})
    # except Restaurant.DoesNotExist:
    #     raise Http404()
    #   # Option 2
    # restaurant = get_object_or_404(Restaurant, pk=rest_id)
    # reviews = Review.objects.filter(restaurant=restaurant)
    # return render(request, 'restaurant/single_restaurant.html', {'restaurant': restaurant, 'reviews': reviews})


def single_restaurant(request, rest_id):
    restaurant = get_object_or_404(Restaurant, pk=rest_id)
    reviews = Review.objects.filter(restaurant=restaurant)

    # Calculate the number of reviews and average rating
    num_reviews = reviews.count()
    avg_rating = reviews.aggregate(avg_rating=Func(
        Avg('stars'), function='ROUND', output_field=IntegerField()))

    return render(request, 'restaurant/single_restaurant.html', {
        'restaurant': restaurant,
        'reviews': reviews,
        'num_reviews': num_reviews,
        'avg_rating': avg_rating['avg_rating'] if avg_rating['avg_rating'] is not None else "No ratings yet"
    })


@login_required
def createreview(request, rest_id):
    restaurant = get_object_or_404(Restaurant, pk=rest_id)
    if request.method == 'GET':
        return render(request, 'restaurant/createreview.html', {'form': ReviewForm(), 'restaurant': restaurant})
    else:
        try:
            form = ReviewForm(request.POST)
            # We create and save a new review object from the form's values but do not yet put it into the
            # database (commit=False) because we want to specify the user and movie relationships for the review.
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.restaurant = restaurant

            newReview.save()
            return redirect('restaurant:single_restaurant', newReview.restaurant.id)
        except ValueError:
            return render(request, 'restaurant/createreview.html', {'form': ReviewForm(), 'error': 'bad data passed in'})


@login_required
def updatereview(request, review_id):
    # supply the logged-in user to ensure that other users can't access the review – for example,
    # if they manually enter the URL path in the browser. Only the user who created this review can update/delete it.
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        # render ReviewForm we used previously in creating a review, but this time, we pass the review object into the form so that the form's fields will be populated with the object's values, ready for the user to edit. Saves us time!
        return render(request, 'restaurant/updatereview.html', {'review': review, 'form': form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('restaurant:single_restaurant', review.restaurant.id)
        except ValueError:
            return render(request, 'restaurant/updatereview.html', {'review': review, 'form': form, 'error': 'Bad data in form'})


@login_required
def deletereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('restaurant:single_restaurant', review.restaurant.id)
