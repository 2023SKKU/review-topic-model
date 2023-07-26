# review-topic-model

Topic modeling using BERTopic

## Usage
### Data loading
csv 파일로 저장된 리뷰 데이터를 받습니다. <br/>
리뷰의 텍스트는 csv 파일에 '<strong>content</strong>' 컬럼에 있어야 합니다. <br/>
별점을 사용할 경우 별점 데이터는 csv 파일에 '<strong>star_rating</strong>' 컬럼에 있어야 합니다. <br/>
아래 코드와 같이 ```FeatureExtraction```에 csv 파일의 경로를 지정해주면 해당 파일의 내용을 불러옵니다.
```python
from feature_extraction import FeatureExtraction

fe = FeatureExtraction('./닭가슴살1.csv')
```
### Basic topic modeling
```FeatureExtraction```의 ```train_topic_model_with_bertopic```을 이용하면 BERTopic 기반의 토픽 모델 학습을 진행합니다. <br/>
학습이 완료된 후 ```get_topics_with_keyword```을 호출하면 각 토픽 별로 추출된 키워드들을 출력하고, 키워드 내용이 담긴 2차원 리스트를 반환합니다.
```python
# training topic model
fe.train_topic_model_with_bertopic('닭가슴살')
# extract topic and keyword
topics = fe.get_topics_with_keyword(top_n_word=10)
```
#### Parameter information

| Method | Parameter | Description | Default value |
| :---: | :---: | :---: | :---: |
| ```train_topic_model_with_bertopic``` | ```product_name``` | 상품의 이름을 지정합니다. | 필수 입력 |
| ```train_topic_model_with_bertopic``` | ```n_topic``` | 토픽 모델링을 진행할 때 토픽의 개수를 지정합니다. <br/>*BERTopic에서는 어느 토픽에도 속하지 않는 요소를 따로 분류하기 때문에 일반적인 경우 ```n_topic```보다 1개 적은 개수의 토픽이 추출됩니다. 경우에 따라 더 적은 개수의 토픽이 출력될 수도 있습니다. | 5 |
| ```train_topic_model_with_bertopic``` | ```star_rating_range``` | 특정 별점의 리뷰만 추출하여 토픽 모델 학습을 진행합니다. list, tuple 등의 형태로 입력 받습니다. 예를 들어 ```[4, 5]```를 전달했다면 4 <strong>이상</strong> 5 <strong>이하</strong>의 별점을 가진 리뷰만 불러옵니다. | None (전체) |
| ```get_topics_with_keyword``` | ```top_n_word``` | 각 토픽 당 추출하는 키워드의 개수를 지정합니다. | 10 |

### Dynamic topic modeling
시간별로 변화하는 토픽을 볼 수 있는 Dynamic topic modeling입니다. <br/>
```get_topics_per_month```를 호출하면 월별로 dynamic topic modeling된 결과를 보여주는 dataframe을 반환합니다. <br/>
```get_topics_per_month```에서 반환된 dataframe을 ```get_keywords_with_time_series```에 넣어 호출하면 단어의 중요도 추이가 토픽 빈도의 추이와 가장 비슷한 단어를 추출하여 list로 반환합니다.
```python
dtm = fe.get_topics_per_month()
print(dtm)
# extract keyword based on dtm
print(fe.get_keywords_with_time_series(dtm, 0))
```
#### Parameter information

| Method | Parameter | Description | Default value |
| :---: | :---: | :---: | :---: |
| ```get_keywords_with_time_series``` | ```dtm``` | ```get_topics_per_month```에서 반환된 dataframe입니다. | 필수 입력 |
| ```get_keywords_with_time_series``` | ```topic_idx``` | 비교하고자 하는 토픽의 index입니다. (일반적으로 [0, n_topic-1) 사이의 정수) | 필수 입력 |
| ```get_keywords_with_time_series``` | ```metric``` | 두 시계열의 유사도를 판단하는 지표입니다. ```['pearson', 'mse', 'dtw']``` 중 하나 | ```'pearson'``` |
| ```get_keywords_with_time_series``` | ```top_n_words``` | 각 토픽 당 추출하는 키워드의 개수를 지정합니다. | 5 |
