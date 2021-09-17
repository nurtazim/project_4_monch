from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from Legis.models import LegisFavourite, LawAllNKO, NCOCategory
from Legis.serializers import LawSerializers, LegisFavouriteSerializers, LegisWictFavouriteSerializers, \
    lawCategorySerializers


class LawAllApiView(generics.ListAPIView):
    queryset = LawAllNKO.objects.all()
    serializer_class = LawSerializers


class LawAllCategoryApiView(generics.ListAPIView):
    queryset = LawAllNKO.objects.all()
    serializer_class = lawCategorySerializers


""" Операции с избранными  законов"""


@permission_classes(IsAuthenticated)
@api_view(["GET", "POST", "DELETE"])
def lawfavoultes(request):
    if request.method == "GET":
        favoultes_list = LegisFavourite.objects.filter(user=request.user)
        data = LegisFavouriteSerializers(favoultes_list, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        legis_id = request.data["legis_id"]
        LegisFavourite.objects.create(legis_id=legis_id,
                                      user=request.user)
        return Response(data={"message": "Favourite created!!!!"})
    elif request.method == "DELETE":
        legis_id = request.data["legis_id"]
        LegisFavourite.objects.filter(legis_id=legis_id,
                                      user=request.user).delete()

        return Response(data={"message": "Favourite removed!!!!"})


@api_view(["GET"])
def law_wits_favourite(request):
    legis = LawAllNKO.objects.all()
    data = LegisWictFavouriteSerializers(legis, many=True, context={"request": request}).data

    return Response(data=data)
