# 프로젝 트 명
프로젝트 설명

## Prerequirement
+ git
+ python3.8.x
+ 배포
    + heroku cli

## Installation
Mac/Linux일 시 상황에 따라 python3, pip3 사용
```shell
# 가상환경 생성 및 활성화
python -m venv venv
.\venv\Scripts\activate

# 앱폴더로 이동 및 필요한 패키지 설치
cd app
pip install -r requirements.txt
```

## Test
+ 로컬 테스트
    ```shell
    python manage.py migrate
    python manage.py runserver
    ```
+ 프로덕션 환경 테스트  
    ```shell
    python manage.py collectstatic
    python manage.py migrate
    python manage.py runserver
    ```

## Deployment
```shell
fap deploy
```