from sklearn.cluster import DBSCAN
import pandas as pd

# 군집화 클래스
class Clustering:

    # 카테고리 별로 군집화
    # cluster_number 열에 군집 번호 생성
    def addClusterNumber(news_df, vector_list):
        cluster_number_list = []

        for vector in vector_list:
            model = DBSCAN(eps=0.1, min_samples=1, metric='cosine')
            result = model.fit_predict(vector)
            cluster_number_list.extend(result)

        news_df['cluster_number'] = cluster_number_list  # 군집 번호 칼럼 추가


    def getClusteredArticle(news_df): # 카테고리 별로 군집의 개수를 센다.
        category_names = ["정치", "경제", "사회", "생활/문화", "세계", "IT/과학", "연예", "스포츠"]
 
        cluster_counts_df = pd.DataFrame(columns=["category", "cluster_number", "cluster_count"])

        for i in range(8):
            tmp = news_df[news_df['category'] == category_names[i]]['cluster_number'].value_counts().reset_index()
            tmp.columns = ['cluster_number', 'cluster_count']
            tmp['category'] = [category_names[i]] * len(tmp)

            cluster_counts_df = pd.concat([cluster_counts_df, tmp])

        # 상위 군집 10개씩만 추출
        cluster_counts_df = cluster_counts_df[cluster_counts_df.index < 10]
        
        return cluster_counts_df