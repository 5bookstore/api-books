from django.urls import path
from reviews.views import (
    ReviewListAndCreateViews,
    ReviewRetriveUpdateDestroyViews
)


urlpatterns = [
    path("user/<str:book_id>/reviews/", ReviewListAndCreateViews.as_view()),
    path(
        "user/<str:book_id>/reviews/<int:review_id>",
        ReviewRetriveUpdateDestroyViews.as_view()
    ),
]
