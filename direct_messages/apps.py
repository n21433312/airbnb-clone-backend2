from django.apps import AppConfig


class DirectMessagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'direct_messages'
    verbose_name = "Direct Messages" # 자동으로 만들어지는 이름 변경을 위한 코드
