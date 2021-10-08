from rest_framework import serializers
from sharing.models import Sharing, SharingMessage, Learnings, LikesForLearning, \
    CommentsForLearning, LoveForSharing, CommentsForSharing
from user.models import User
from django_countries.serializers import CountryFieldMixin
# from rest_framework.validators import UniqueTogetherValidator  # one student can tag a teacher once


class SharingSerializers(CountryFieldMixin, serializers.ModelSerializer):
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    teacher = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', required=False, allow_null=True)
    s_photo = serializers.ImageField(required=True, allow_null=True)
    # s_location = serializers.CharField(required=False, allow_null=True)
    # likes_count = serializers.SerializerMethodField()
    # likes_sharing = LikesToSharingSerializers(many=True, read_only=True)
    # comments_sharing = CommentSerializers(many=True, read_only=True)

    class Meta:
        model = Sharing
        fields = ['id', 'username', 'teacher', 's_teacher_name', 's_photo', 's_appreciation', 's_video_talk',
                  's_video_dance', 's_teacher_country', 's_student_country', 's_date', 's_location', 's_teacher_video', ]


class SharingMessageSerializers(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = SharingMessage
        fields = ['username', 'shareid', 'messagetext', 'created']


class LearningsSerializers(serializers.ModelSerializer):
    """
    for CRUD operations.
    Keep the learning update limited to PUT ONLY, do not use patch.
    create and update methods overridden such that when there is video file available,
    videouploaded Boolean field is made True, otherwise False.
    """
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Learnings
        fields = ['id', 'username', 'shareidobj', 'lesson', 'timestamp', 'video']  # only for serialization , NOT Deserialization

    def create(self, validated_data):
        video = validated_data.pop('video', False)
        if video:
            validated_data['video'] = video
            validated_data['videouploaded'] = True
            return Learnings.objects.create(**validated_data)
        return Learnings.objects.create(**validated_data)

    def update(self, instance, validated_data):
        video = validated_data.pop('video', False)
        if video:
            validated_data['video'] = video
            validated_data['videouploaded'] = True

            instance.shareidobj = validated_data.get('shareidobj', instance.shareidobj)
            instance.username = validated_data.get('username', instance.username)
            instance.lesson = validated_data.get('lesson', instance.lesson)
            instance.timestamp = validated_data.get('timestamp', instance.timestamp)
            instance.video = validated_data.get('video', instance.video)
            instance.videouploaded = validated_data.get('videouploaded', instance.videouploaded)

            instance.save()
            return instance
        else:
            validated_data['videouploaded'] = False

            instance.shareidobj = validated_data.get('shareidobj', instance.shareidobj)
            instance.username = validated_data.get('username', instance.username)
            instance.lesson = validated_data.get('lesson', instance.lesson)
            instance.timestamp = validated_data.get('timestamp', instance.timestamp)
            instance.video = validated_data.get('video', instance.video)
            instance.videouploaded = validated_data.get('videouploaded', instance.videouploaded)

            instance.save()
            return instance


# for Listing and retrieving only.
class LearningsSerializersWithoutVideo(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Learnings
        fields = ['id', 'username', 'shareidobj', 'lesson', 'timestamp', 'videouploaded']
        read_only_fields = ['id', 'username', 'shareidobj', 'lesson', 'timestamp', 'videouploaded']


class LikesForLearningSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = LikesForLearning
        fields = '__all__'

    # add the total likes count to the serialized data   ----------------
    # def to_representation(self, instance):
        # representation = super().to_representation(instance)
        # representation['likes'] = instance.


class CommentsForLearningSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = CommentsForLearning
        fields = '__all__'


class LoveForSharingSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = LoveForSharing
        fields = "__all__"


class CommentsForSharingSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = CommentsForSharing
        fields = "__all__"








"""
class LikesToSharingSerializers(serializers.ModelSerializer):
    l_liker = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = LikesToSharing
        fields = ['id', 'l_shareid', 'l_liker', 'l_type']


class CommentSerializers(serializers.ModelSerializer):
    c_commenter = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Comments
        fields = ['id', 'c_shareid', 'c_commenter', 'c_comment', 'c_time']
"""
