"""Сериалайзер законов"""
from rest_framework import serializers

from Legis.models import LegisFavourite, NCOCategory, LawAllNKO


class LawSerializers(serializers.ModelSerializer):
    class Meta:
        model = LawAllNKO
        fields = "__all__"

class lawCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = NCOCategory
        fields = "id category  ".split()


"""Сериалайзер избранных для законов"""


class LegisFavouriteSerializers(serializers.ModelSerializer):
    legis = LawSerializers

    class Meta:
        model = LegisFavourite
        fields = "__all__"


class LegisWictFavouriteSerializers(serializers.ModelSerializer):
    is_favourite = serializers.SerializerMethodField()

    class Meta:
        model = LawAllNKO
        fields = "id title is_favourite".split()

    def get_is_favourite(self, legis):
        request = self.context["request"]
        return bool(request.user.is_authenticated
                    and LegisFavourite.objects.filter(user=request.user, legis=legis).count() > 0)
