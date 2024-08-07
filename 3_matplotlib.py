# -*- coding: utf-8 -*-
"""3. Matplotlib.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ntmJXV66xWnZe3xy-5SKoKf32xAJ9HK2

# **1. Matplotlib**
* 파이썬 기반 시각화 라이브러리
* 한글에 대한 지원이 완벽하지 않음
* 판다스와 연동이 용이함
* [Matplotlib 공식 홈페이지](https://matplotlib.org)
"""

!pip install matplotlib

# MATHLAB과 비슷하게 명령어 스타일로 동작하는 함수들의 모음
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4]) # 리스트의 값들은 y값들이며, x값은 자동으로 만들어줌
plt.show()

plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
plt.show()

import numpy as np

data = np.arange(1, 100)
plt.plot(data)
plt.show()

data1 = np.arange(1, 50)
plt.plot(data1)
data2 = np.arange(50, 100)
plt.plot(data2)
plt.show() # 색은 자동으로 입혀짐(정해줄 수도 있음)

# 여러개의 plot을 그리는 방법
# subplot(행개수, 열개수, plot번호)
data1 = np.arange(1, 50)
plt.subplot(2, 1, 1)
plt.plot(data1)

data2 = np.arange(50, 100)
plt.subplot(2, 1, 2)
plt.plot(data2)

plt.show()

"""# **2. 스타일 옵션**"""

# 한글 fonts-nanum 설치
# 재시작 필요
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

plt.rc('font', family = 'NanumBarunGothic')

plt.figure(figsize = (3, 4)) # inch
plt.plot([1, 2, 3], [1, 2, 3])
plt.title('제목', fontsize=30)
plt.xlabel('X축', fontsize=20)
plt.ylabel('Y축', fontsize=20, rotation=0)
plt.show()

plt.figure(figsize=(15, 10))
plt.title('마커설정', fontsize=30)
plt.plot(np.arange(10), np.arange(10), color='pink', marker='o', linestyle='-.')
plt.plot(np.arange(10), np.arange(10)*2, color='skyblue', marker='v', linestyle='--')
plt.plot(np.arange(10), np.arange(10)*3, color='yellow', marker='*', ms=10, linestyle='') # ms: 마커 크기 설정

# 범례
# 기본 위치는 왼쪽 상단
plt.legend(['10', '10*2', '10*3'], fontsize=15, loc='lower right', ncol=3)

plt.xlim(0, 12)
plt.ylim(0, 30)

plt.show()

x = ['파이썬', '웹개발', '데이터분석', '머신러닝', '딥러닝', '컴퓨터비전']
y = [95, 70, 75, 60, 50, 30]
plt.figure(figsize=(8, 5))
plt.title('AI 성적표', fontsize=25)
plt.ylabel('수강생 점수')
plt.bar(x, y, alpha=0.5, color='deeppink')
plt.show()

x = ['파이썬', '웹개발', '데이터분석', '머신러닝', '딥러닝', '컴퓨터비전']
y = [95, 70, 75, 60, 50, 30]
plt.figure(figsize=(8, 5))
plt.title('AI 성적표', fontsize=25)
plt.xlabel('수강생 점수')
plt.barh(x, y, alpha=0.5, color='deepskyblue')
plt.show()

