from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id","title","artist","album","release_date","genre"]

# class Song_Likes_Serializer(serializers.ModelSerializer):
#     model = Song_Likes
#     fields = ['id','liked_song_id',"like_status"]