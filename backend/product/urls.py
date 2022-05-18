from django.urls import path, include

from . import views

urlpatterns = [
    path('latest-products/',views.LatestProductList.as_view(), name="latestproduct")
]