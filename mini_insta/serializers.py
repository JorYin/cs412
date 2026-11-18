# File: serializers.py
# Author: Jordan Yin (jordany@bu.edu)
# Description: REST API serializers for MiniInsta profiles, posts, and photos.

from rest_framework import serializers

from .models import Photo, Post, Profile


class PhotoSerializer(serializers.ModelSerializer):
    """Serialize a photo attached to a post."""

    image = serializers.SerializerMethodField()

    class Meta:
        """Configure the fields exposed by PhotoSerializer."""

        model = Photo
        fields = ['id', 'post', 'image', 'timestamp']

    def get_image(self, obj):
        """Return the photo's public URL or uploaded file URL."""
        return obj.get_image_url()


class ProfileSerializer(serializers.ModelSerializer):
    """Serialize the profile fields used by the MiniInsta REST API."""

    post_count = serializers.SerializerMethodField()

    class Meta:
        """Configure the fields exposed by ProfileSerializer."""

        model = Profile
        fields = [
            'id',
            'username',
            'display_name',
            'profile_image_url',
            'bio_text',
            'join_date',
            'post_count',
        ]

    def get_post_count(self, obj):
        """Return the number of posts belonging to this profile."""
        return obj.get_all_posts().count()


class PostSerializer(serializers.ModelSerializer):
    """Serialize posts and provide nested photo data and creation inputs."""
    photos = PhotoSerializer(source='photo_set', many=True, read_only=True)
    image_urls = serializers.ListField(
        child=serializers.URLField(),
        write_only=True,
        required=False,
    )
    profile_id = serializers.PrimaryKeyRelatedField(
        source='profile',
        queryset=Profile.objects.all(),
    )

    class Meta:
        """Configure the fields used to read and create posts."""

        model = Post
        fields = [
            'id',
            'profile_id',
            'caption',
            'timestamp',
            'photos',
            'image_urls',
        ]
        read_only_fields = ['timestamp']

    def create(self, validated_data):
        """Create a post and an associated photo for every supplied URL."""
        image_urls = validated_data.pop('image_urls', [])
        post = Post.objects.create(**validated_data)

        for image_url in image_urls:
            Photo.objects.create(post=post, image_url=image_url)

        return post