from fabric.api import local


def deploy():
    # 무중단 배포를 위한 설정
    local('heroku maintenance:on')
    # 변경내역 서버에 반영
    local('git push heroku master')
    # 사용후 다시 중지
    local('heroku maintenance:off')

def runserver():
    local("python manage.py runserver --settings=ddingproject.settings.dev")