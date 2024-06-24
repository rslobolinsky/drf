from rest_framework.serializers import ValidationError


class LessonValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if 'youtube.com' not in tmp_val:
            raise ValidationError('Неверная ссылка, она должна содержать youtube.com')