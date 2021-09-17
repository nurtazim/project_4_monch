from django.urls import path
from Legis import views


urlpatterns = [
    path("legislationsnko/",views.LawAllApiView.as_view()),
    path("categotylaw/",views.LawAllCategoryApiView.as_view()),
    path("lawfavorites/",views.lawfavoultes),
    path("lawwitsfavourite/",views.law_wits_favourite)

]

