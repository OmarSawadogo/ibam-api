from rest_framework import viewsets
from . import models
from . import serializers

class CoursViewset(viewsets.ModelViewSet):
    queryset = models.Cours.objects.all()
    serializer_class = serializers.CoursSerializer