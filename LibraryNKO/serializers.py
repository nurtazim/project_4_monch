from rest_framework import serializers

from LibraryNKO.models import *


class librarySerializers(serializers.ModelSerializer):
    class Meta:
        model = PublicationsNKO
        fields = "__all__"


class CategoryLibrarySerializers(serializers.ModelSerializer):
    class Meta:
        model = NCOLibraryCategory
        fields = "__all__"


class LibraryFavouriteSerializers(serializers.ModelSerializer):
    library = librarySerializers

    class Meta:
        model = PublicationsFavourite
        fields = "__all__"


class PublicWictFavouriteSerializers(serializers.ModelSerializer):
    is_favourite = serializers.SerializerMethodField()

    class Meta:
        model = PublicationsNKO
        fields = "id title is_favourite".split()

    def get_is_favourite(self, public):
        request = self.context["request"]
        return bool(request.user.is_authenticated
                    and PublicationsFavourite.objects.filter(user=request.user, public=public).count() > 0)
