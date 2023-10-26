from rest_framework import serializers
from .models import Music, Comment


class MusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ("id", "title")


class MusicSerializer(serializers.ModelSerializer):
# PrimaryKeyRelatedField를 사용
    comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    # Nested 방법으로 진행
    # class CommentSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Comment
    #         fields = '__all__'
    # comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    
    class Meta:
        model = Music
        fields = '__all__'
        

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('music',)