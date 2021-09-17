from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from LibraryNKO.models import *
from rest_framework import generics

from LibraryNKO.serializers import *


class LibraryAllApiView(generics.ListCreateAPIView):
    queryset = PublicationsNKO.objects.all()
    serializer_class = librarySerializers


class LibraryCategoryAllApiView(generics.ListAPIView):
    queryset = PublicationsNKO.objects.all()
    serializer_class = CategoryLibrarySerializers


""" Операции с избранными  библиотек"""


@permission_classes(IsAuthenticated)
@api_view(["GET", "POST", "DELETE"])
def libraryfavoultes(request):
    if request.method == "GET":
        favoultes_list = PublicationsFavourite.objects.filter(user=request.user)
        data = LibraryFavouriteSerializers(favoultes_list, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        public_id = request.data["public_id"]
        PublicationsFavourite.objects.create(public_id=public_id,
                                             user=request.user)
        return Response(data={"message": "Favourite created!!!!"})
    elif request.method == "DELETE":
        public_id = request.data["public_id"]
        PublicationsFavourite.objects.filter(public_id=public_id,
                                             user=request.user).delete()

        return Response(data={"message": "Favourite removed!!!!"})


@api_view(["GET"])
def Library_wits_favourite(request):
    public = PublicationsNKO.objects.all()
    data = PublicWictFavouriteSerializers(public, many=True, context={"request": request}).data

    return Response(data=data)
