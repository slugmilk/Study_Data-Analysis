# -*- coding: utf-8 -*-
"""7. 서울시 따릉이 API 활용.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZRKhZJwXydyPee8jORArkQFMXOeGnHcr

# **1. 따릉이 API**
* https://www.bikeseoul.com/app/station/getStationRealtimeStatus.do
"""

import requests
import folium
import json
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

"""### 1-1. 데이터 요청하기"""

targetSite = 'https://www.bikeseoul.com/app/station/getStationRealtimeStatus.do'
request = requests.post(targetSite, data={'stationGrpSeq':'ALL'})
print(request.text)

"""### 1-2. json 데이터 처리하기
* json.loads(): json 타입의 문자열 데이터를 파이썬에서 처리할 수 있도록 변환(딕셔너리로 변환)
"""

bike_json = json.loads(request.text)
print(bike_json)
print(type(bike_json))

"""### 1-3. 딕셔너리 타입의 데이터를 데이터프레임으로 변환하기
* json_normalize(): 딕셔너리 자료구조 타입의 데이터를 판다스 데이터프레임으로 변환
"""

bike_df = pd.json_normalize(bike_json, 'realtimeList')
bike_df

bike_df.columns

"""* stationLongitude: 대여소 경도
* stationLatitude: 대여소 위도
* rackTotCn: 주차 가능한 전체 자전거 대수
* parkingBikeTotCnt: 주차된 따릉이 총 대수
* parkingQRBikeCnt: 주차된 따릉이 QR형 총 대수
* parkingELECBikeCnt: 주차된 새싹 따릉이 총 대수
* stationId: 고유한 대여서 번호
* stationName: 대여소 이름


"""

bike_df_map = bike_df[['stationName', 'stationId', 'stationLongitude', 'stationLatitude',
                       'rackTotCnt' ,'parkingBikeTotCnt', 'parkingQRBikeCnt', 'parkingELECBikeCnt']]
bike_df_map

bike_df_map.dtypes

# 형변환
bike_df_map['stationLongitude'] = bike_df_map['stationLongitude'].astype(float)
bike_df_map['stationLatitude'] = bike_df_map['stationLatitude'].astype(float)

bike_df_map['rackTotCnt'] = bike_df_map['rackTotCnt'].astype(int)
bike_df_map['parkingBikeTotCnt'] = bike_df_map['parkingBikeTotCnt'].astype(int)
bike_df_map['parkingQRBikeCnt'] = bike_df_map['parkingQRBikeCnt'].astype(int)
bike_df_map['parkingELECBikeCnt'] = bike_df_map['parkingELECBikeCnt'].astype(int)
bike_df_map['total'] = bike_df_map['parkingBikeTotCnt'] + bike_df_map['parkingQRBikeCnt'] + bike_df_map['parkingELECBikeCnt']

bike_df_map.dtypes

bike_df_map.head()

bike_df_map.shape

bike_map = folium.Map(location=[bike_df_map['stationLatitude'].mean(),
                                bike_df_map['stationLongitude'].mean()],
                      zoom_start=12)

for index, data in bike_df_map.iterrows():
    popup_str = '{} 일반:{}대, QR:{}대, 새싹:{}대, 총:{}대'.format(
        data['stationName'], data['parkingBikeTotCnt'], data['parkingQRBikeCnt'],
        data['parkingELECBikeCnt'], data['total']
    )
    popup = folium.Popup(popup_str, max_width=600)
    folium.Marker(location=[data['stationLatitude'], data['stationLongitude']],
                  popup=popup).add_to(bike_map)
bike_map

