from rest_framework.serializers import ModelSerializer
from .models import Photo


class PhotoSeriailizer(ModelSerializer):
    class Meta : 
        model = Photo
        fields = (
            "pk",
            "file",
            "description",
        )

    