from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    model = Song
    fields = ["id","title","album","release_date","genre"]