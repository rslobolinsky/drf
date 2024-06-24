from rest_framework import serializers

from materials.models import Course, Lesson, Subscribe
from materials.validators import LessonValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LessonValidator(field='url_video')]


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson', many=True)
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, instance):
        return instance.lesson.all().count()

    def get_is_subscribed(self, instance):
        user = self.context['request'].user
        sub = Subscribe.objects.filter(user=user, course=instance)
        if sub.exists():
            return 'Подписка оформлена'
        else:
            return 'Вы не подписаны на курс'

