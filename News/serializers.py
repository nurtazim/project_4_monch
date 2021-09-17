from django.utils import timezone
from rest_framework import serializers



from .models import News, ImageNews, Favourite




"""Сериалайзер новостей"""


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "id image title data short_text  ".split()


class ImageNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageNews
        fields = "id image".split()


class NewsObjectSerializers(serializers.ModelSerializer):
    images = ImageNewsSerializers(many=True)

    class Meta:
        model = News
        fields = "id image title text newslink images".split()


"""Сериалайзер избранных для новостей"""


class FavouriteSerializers(serializers.ModelSerializer):
    news = NewsListSerializer

    class Meta:
        model = Favourite
        fields = "__all__"


class NewsWictFavouriteSerializers(serializers.ModelSerializer):
    is_favourite = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = "id title is_favourite".split()

    def get_is_favourite(self, news):
        request = self.context["request"]
        return bool(request.user.is_authenticated
                    and Favourite.objects.filter(user=request.user, news=news).count() > 0)












