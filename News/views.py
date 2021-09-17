from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from News.serializers import *
from rest_framework import generics


class NewsListApiView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer



class NewsItemApiView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsObjectSerializers



""" Операции с избранными  новостей"""


@permission_classes(IsAuthenticated)
@api_view(["GET", "POST", "DELETE"])
def favoultes(request):
    if request.method == "GET":
        favoultes_list = Favourite.objects.filter(user=request.user)
        data = FavouriteSerializers(favoultes_list, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        news_id = request.data["news_id"]
        Favourite.objects.create(news_id=news_id,
                                 user=request.user)
        return Response(data={"message": "Favourite created!!!!"})
    elif request.method == "DELETE":
        news_id = request.data["news_id"]
        Favourite.objects.filter(news_id=news_id,
                                 user=request.user).delete()

        return Response(data={"message": "Favourite removed!!!!"})



@api_view(["GET"])
def news_wits_favourite(request):
    news = News.objects.all()
    data = NewsWictFavouriteSerializers(news, many=True, context={"request": request}).data

    return Response(data=data)



