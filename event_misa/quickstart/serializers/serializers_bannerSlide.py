from rest_framework import serializers
from quickstart.models import bannerSlide
class bannerSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = bannerSlide
        fields = '__all__'
