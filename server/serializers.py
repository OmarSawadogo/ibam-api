from rest_framework import serializers
from . import models

class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cours
        fields = "__all__"