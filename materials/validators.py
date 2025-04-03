import re

from django.core.exceptions import ValidationError


def validate_video_link(value):
    """
    Проверяет, что ссылка ведет на youtube.com.
    """
    if not re.match(r'https?://(www\.)?youtube\.com/watch\?v=', value):
        raise ValidationError('Ссылка должна вести на видео с youtube.com.')


class VideoLinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        validate_video_link(value)