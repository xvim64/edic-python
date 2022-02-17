# edic-python

예전 알짜 리눅스에 포함되었던 영한사전의 Python 버전입니다.

아래 출처의 bash 스크립트르 Python 으로 구현했기 때문에 Python 이 설치된 모든 OS 에서 구동이 가능합니다

또한 \* 검색을 지원하기 때문에 lime\* 과 같이 특정 구문이 들어간 단어를 찾을 때 좋습니다.

영어 공부할 때 유용하게 사용하세요.



# 라이선스

edic.py, dic2sqlite.py 는 GNU General Public License v2.0 을 따릅니다.

한영사전 DB 는 포함하고있지 않습니다.

한영사전 DB 는 [edic](https://github.com/liks79/edic) 에서 다운 받아 사용하세요.



# 설치 및 실행하기

1. 웹페이지 오른쪽의 Release 에서 edic-python.zip 파일을 다운받아 압축을 풉니다.

2. [edic](https://github.com/liks79/edic) 에서 Code 에서 Download ZIP 으로 다운받은 파일의 압축을 풀고 data/utf-8 안의 \*\.gz 파일을 (1) 에서 압축을 푼 edic-python 폴더 안의 utf-8 폴더에 복사합니다.

3. 사전 데이터를 빌드하려면 윈도우는 dic2sqlite.cmd 를 실행합니다. 리눅스는 python3 dic2sqlite.py 를 실행합니다.

4. 윈도우라면 edic-wt.cmd 를, 리눅스라면 ./edic 을 실행하세요.



# 한영사전 DB 만들기

utf-8 폴더에 user.dic 파일을 생성하고

```
apple : 사과
lime : 라임
orange : 오렌지
banana : 바나나
```

위와 같이 ":" 를 구분기호로 해서 단어를 추가하고

dic2sqlite.cmd 를 실행하면

edic.sqlite 를 빌드할 수 있습니다.



# edic-python in debian

debian 리눅스에서 edic-python 을 실행한 영상입니다.

[![debian](https://img.youtube.com/vi/_67naCIfVakA/0.jpg)](https://youtu.be/67naCIfVakA)



# edic-python in Windows

Windows 10 에서 명령 프롬프트와 윈도우즈 터미널에서 edic-python 을 실행한 영상입니다.

[![windows](https://img.youtube.com/vi/_z164WQb0whw/0.jpg)](https://youtu.be/z164WQb0whw)



# 출처

## 추억의 터미널 영한사전
- [edic](https://github.com/liks79/edic)


