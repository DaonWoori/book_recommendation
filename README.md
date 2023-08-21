# book_recommendation

## 목차
1. [프로젝트 소개](#프로젝트-소개)
2. [프로젝트 목표](#프로젝트-목표)
3. [프로젝트 기능 구현](#프로젝트-기능-구현)
4. [프로젝트 결과](#프로젝트-결과)
5. [프로젝트 회고](#프로젝트-회고)

### 프로젝트 소개
```
코사인 유사도를 활용한 도서 추천 사이트인 나만의 책방 개발

- 프로젝트 기간: 2023.04.07 ~ 2023.04.12
- Skills: pandas, numpy, sklearn, flask, mongoDB, pymongo, pickle
- 출처: 코드스테이츠 AIB 부트캠프
```

### 프로젝트 목표

<p align="center"><img width="500" alt="image" src="https://github.com/DaonWoori/book_recommendation/assets/88466357/809fe263-ab97-4e54-913e-18f9d346f226"></p>


 책을 읽는다는 것은 가장 쉽게 다양한 경험을 간접적으로 체험해볼 수 있는 기회이자, 지식을 넓힐 수 있는 가장 좋은 방법이다. 그러나 스마트폰의 개발로 사람들이 책을 읽는 시간이 점점 줄어들고 있다.

 실제 통계청에서 진행한 조사에 따르면 우리나라 국민들이 하루 중 책을 읽는데 사용하는 시간은 단 8분이라고 한다. 이와 더불어 독서를 하는 인구와 1인 당 연간 독서 권수도 매년 감소하고 있는 추세이다.

![image](https://github.com/DaonWoori/book_recommendation/assets/88466357/8ca4361e-0064-444a-9dd1-09fd2e2fdb16)

 도서 추천 플랫폼인 “나만의 책방”은 사람들이 독서를 좀 더 쉽게 접근했으면 하는 마음으로 계획되었다. 여러 사용자들의 도서 평점 정보를 분석하여 자신에게 맞는 도서를 추천 받을 수 있는 서비스를 제공할 것이다.

---

### 프로젝트 기능 구현

**파이프라인**

![image](https://github.com/DaonWoori/book_recommendation/assets/88466357/0c16687d-d19e-4fb6-96a8-b8218b850c86)

1.  캐글에서 csv 파일 다운로드(🔗 [Kaggle: Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset?select=Users.csv))
2.  데이터 전처리 및 병합
3.  pymongo를 활용해 DB에 데이터 적재
4.  sklearn을 활용해 코사인 유사도계산
5.  결과를 피클링을 통해 .pickle 파일로 저장
6.  DB 내의 파일과 피클 파일을 불러와서 웹 페이지 내 추천 알고리즘 구현

**데이터 소개**

-   Books.csv: 책 정보를 담고 있는 데이터 셋  
    -   ISBN: 도서번호
    -   Book-Title: 책 제목
    -   Book-Author: 작가
    -   Year-of-Publication: 출판연도
    -   Publisher: 출판사
    -   Image-URL-M: 표지 이미지 URL
      
-   Ratings.csv: 사용자들이 책에 매긴 점수를 담고 있는 데이터 셋
    -   User-ID: 유저 아이디
    -   ISBN: 도서번호
    -   Book-Rating: 평점정보

:arrow_forward: ISBN을 기준으로 두 데이터를 병합

![image](https://github.com/DaonWoori/book_recommendation/assets/88466357/0a907bfc-9641-4c54-8814-154425df7ce0)


**mongoDB**

-   pymongo를 활용하여 데이터를 mongoDB에 적재

![image](https://github.com/DaonWoori/book_recommendation/assets/88466357/87ac857e-9df9-4730-b177-bbc311207f2e)
![image](https://github.com/DaonWoori/book_recommendation/assets/88466357/616b898f-13a9-43b6-a69a-edac1f678d5f)


**추천 알고리즘 구현**

- 피벗 테이블 만들기

  ```
  ratings_matrix = rating_books.pivot_table('Book-Rating', index='User-ID', columns='Book-Title')
  ratings_matrix = ratings_matrix.fillna(0)
  ```

- 코사인 유사도 계산

  ```
  item_sim = cosine_similarity(ratings_matrix_T, ratings_matrix_T)
  # 코사인 유사도의 결과를 도서명과 매핑하여 DataFrame으로 변환
  item_sim_df = pd.DataFrame(data=item_sim, index=ratings_matrix.columns, columns=ratings_matrix.columns)
  ```

> 코사인 유사도(Cosine Similarity): 두 벡터 간의 코사인 각도를 이용하여 구할 수 있는 두 벡터의 유사도
> 
> (출처: https://wikidocs.net/24603)

- 계산된 코사인 유사도를 피클 파일로 저장
- 사용자가 책 제목을 입력하면 코사인 유사도가 높은 10개의 도서를 화면에 출력

---

### 프로젝트 결과

**홈 페이지** 

![image](https://github.com/DaonWoori/book_recommendation/assets/88466357/3d7f331c-4252-475b-bf5f-5fcbb697ec4c)


**도서 추천 페이지**

![image](https://github.com/DaonWoori/book_recommendation/assets/88466357/01183632-c0e1-48d8-996e-5cf64a6f779c)


**시연 영상**

[<iframe src="https://play-tv.kakao.com/embed/player/cliplink/439899556?service=daum_tistory" width="860" height="513" frameborder="0" allowfullscreen="true"></iframe>](https://tv.kakao.com/v/439899556)

---

### 프로젝트 회고

**한계점**

- 책 제목 만을 활용해 추천 기능 사용
- 데이터베이스 내에 입력되어 있는 책 제목 그대로 입력해야 알고리즘 작동

**향후 개선 사항**

- 회원 기능을 추가하여 조금 더 개인에게 맞는 추천 서비스를 제공
- 현재 서비스를 제공 중인 도서에 대한 정보를 제공해주는 페이지 추가
- 도서 추천 페이지에서 구매 페이지 등으로 이동할 수 있는 링크 연결
