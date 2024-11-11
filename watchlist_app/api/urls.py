from django.urls import path

# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (
    WatchListAV,
    WatchDetailAV,
    StreamPlatformListAV,
    StreamPlatformDetailAV,
)

# urlpatterns = [
#     path("list/", movie_list, name="movie-list"),
#     path("<int:pk>", movie_details, name="movie-detail"),
# ]

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("list/<int:pk>", WatchDetailAV.as_view(), name="movie-detail"),
    path("stream/", StreamPlatformListAV.as_view(), name="streamplatform-list"),
    path(
        "stream/<int:pk>",
        StreamPlatformDetailAV.as_view(),
        name="streamplatformdetail-list",
    ),
]
