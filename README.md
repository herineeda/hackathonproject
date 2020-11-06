# 아이띵동 소개

![슬라이드1](https://user-images.githubusercontent.com/48933109/98249261-65aa4300-1fb9-11eb-9396-43ccffff2100.JPG)
![슬라이드2](https://user-images.githubusercontent.com/48933109/98249268-680c9d00-1fb9-11eb-8bfc-f26b74498e25.JPG)
![슬라이드3](https://user-images.githubusercontent.com/48933109/98249276-6a6ef700-1fb9-11eb-95c9-b0409f3774e9.JPG)
![슬라이드4](https://user-images.githubusercontent.com/48933109/98249293-6d69e780-1fb9-11eb-8cba-fdd7d02cf55d.JPG)
![슬라이드5](https://user-images.githubusercontent.com/48933109/98249304-6fcc4180-1fb9-11eb-820c-0b163655ca23.JPG)
![슬라이드6](https://user-images.githubusercontent.com/48933109/98249313-72c73200-1fb9-11eb-94cf-de7be8d36423.JPG)
![슬라이드7](https://user-images.githubusercontent.com/48933109/98249318-75298c00-1fb9-11eb-9fdf-47c5ce8a7a04.JPG)
![슬라이드8](https://user-images.githubusercontent.com/48933109/98249333-78247c80-1fb9-11eb-82f9-ad821d442fd2.JPG)
![슬라이드9](https://user-images.githubusercontent.com/48933109/98249344-7b1f6d00-1fb9-11eb-8043-7006062cf087.JPG)
![슬라이드10](https://user-images.githubusercontent.com/48933109/98249352-7d81c700-1fb9-11eb-9435-15871d999475.JPG)
![슬라이드11](https://user-images.githubusercontent.com/48933109/98249364-807cb780-1fb9-11eb-94c4-bdfe76c5b3e0.JPG)
![슬라이드12](https://user-images.githubusercontent.com/48933109/98249373-8377a800-1fb9-11eb-812e-51cdf2fcf6e7.JPG)
![슬라이드13](https://user-images.githubusercontent.com/48933109/98249382-85da0200-1fb9-11eb-855d-a212887b85ae.JPG)
![슬라이드14](https://user-images.githubusercontent.com/48933109/98249395-88d4f280-1fb9-11eb-87cb-fc51f0d89527.JPG)
![슬라이드15](https://user-images.githubusercontent.com/48933109/98249402-8a9eb600-1fb9-11eb-9736-fffa4d576a96.JPG)
![슬라이드16](https://user-images.githubusercontent.com/48933109/98249417-8e323d00-1fb9-11eb-9ce4-afd83df846df.JPG)
![슬라이드17](https://user-images.githubusercontent.com/48933109/98249434-925e5a80-1fb9-11eb-836c-3fd8f028bc0c.JPG)
![슬라이드18](https://user-images.githubusercontent.com/48933109/98249442-95594b00-1fb9-11eb-90aa-a238bbacaa92.JPG)
![슬라이드19](https://user-images.githubusercontent.com/48933109/98249454-97bba500-1fb9-11eb-8b81-d72967f4a996.JPG)
![슬라이드20](https://user-images.githubusercontent.com/48933109/98249460-9a1dff00-1fb9-11eb-92eb-ba2cf788223f.JPG)
![슬라이드21](https://user-images.githubusercontent.com/48933109/98249466-9e4a1c80-1fb9-11eb-8d4b-de51f145a4e3.JPG)
![슬라이드22](https://user-images.githubusercontent.com/48933109/98249479-a1dda380-1fb9-11eb-9002-24c3df040a8b.JPG)
![슬라이드23](https://user-images.githubusercontent.com/48933109/98249485-a43ffd80-1fb9-11eb-88c3-311cef04df2a.JPG)


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

