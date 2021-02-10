from django.apps import AppConfig


# 요 클래스가 config/settings.py파일의 INSTALLED_APPS항목에 추가되지 않으면 장고는 pybo앱을 인식하지 못하고, db관련작업을 할 수 없다.
class PyboConfig(AppConfig):
    name = 'pybo'
