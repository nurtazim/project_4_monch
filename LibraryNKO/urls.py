from django.urls import path
from LibraryNKO import views

urlpatterns = [
    path("library/", views.LibraryAllApiView.as_view()),
    path("librarycategory/", views.LibraryCategoryAllApiView.as_view()),
    path("libraryfavorites/", views.libraryfavoultes),
    path("librarywitsfavourite/", views.Library_wits_favourite),

]
