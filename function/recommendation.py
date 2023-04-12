from DB import get_DB
import pickle

def recommend(book_title):
    cosine_sim = pickle.load(open('cosine_sim.pickle', 'rb'))
    
    recommendation_books = []
    # try:
    #     book = cosine_sim[book_title]
    # except:
    #     print("No DataBase for Book")
    for data in cosine_sim[book_title].sort_values(ascending=False)[1:11].index:
        similar_books = get_DB.get_ratings(data) # 책 정보 받아오기
    
        item = []
        item.append(similar_books ['Book-Title'])
        item.append(similar_books['Book-Author'])
        item.append(similar_books['Publisher'])
        item.append(similar_books['Year-Of-Publication'])
        item.append(similar_books['Image-URL-M'])
        
        recommendation_books.append(item)
        
    return recommendation_books