import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

""""READING THE DATA"""
BX_Books=pd.read_csv('BX_Books.csv',encoding='iso-8859-1',sep=';')
#print(BX_Books.head())

BX_Users=pd.read_csv('BX-Users.csv',encoding='iso-8859-1',sep=';')
#print(BX_Users.head())

BX_Book_Ratings=pd.read_csv('BX-Book-Ratings.csv',encoding='iso-8859-1',sep=';')
#print(BX_Book_Ratings.head())

""""VISUALISE THE DATA"""
ratings=pd.DataFrame(BX_Book_Ratings.groupby('ISBN')['Book-Rating'].mean())
#print(ratings)

ratings['rating-count']=pd.DataFrame(BX_Book_Ratings.groupby('ISBN')['Book-Rating'].count())
#print(ratings.head())

ratings=ratings.sort_values(by='rating-count',ascending=False)
#print(ratings)

#plt.figure(figsize=(10,4))
#plt.hist(ratings,bins=100)
#plt.show()

""""DELETION OF LOW SUPPORT VALUES"""
_tmp=ratings[ratings['rating-count']>50]
isbn_to_delete=ratings[ratings['rating-count']<50]
#print(isbn_to_delete)

isbn_to_delete=list(isbn_to_delete.index.values)
#print(isbn_to_delete)

#print(BX_Book_Ratings)

BX_Book_Ratings=BX_Book_Ratings.set_index('ISBN')

BX_Book_Ratings.drop(isbn_to_delete,inplace=True)

""""PIVOT TABLE"""
pivot_table=BX_Book_Ratings.pivot_table(index="User-ID",columns='ISBN',values='Book-Rating')
#print(pivot_table.head())

""""GENERATIONS OF CORRELATION"""
def name_for_ISBN(ISBN,df=BX_Books):
    row=df.loc[df['ISBN']==ISBN]
    print(row[['Book-Title','Book-Author','Year-Of-Publication','Publisher']])
#name_for_ISBN('038550120X')

JOHN_GRISHAM_Painted_House=pivot_table['038550120X']
#print(JOHN_GRISHAM_Painted_House)

Painted_House_similar_books=pivot_table.corrwith(JOHN_GRISHAM_Painted_House)

Painted_House_similar_books=pd.DataFrame(Painted_House_similar_books,columns=['Correlation'])
Painted_House_similar_books=Painted_House_similar_books.dropna()

#print(Painted_House_similar_books.sort_values('Correlation',ascending=False))

""""RECOMMENDATIONS"""
Painted_House_similar_books=Painted_House_similar_books.join(ratings)
#print(Painted_House_similar_books)

BX_Books=BX_Books.set_index('ISBN')
Painted_House_similar_books=Painted_House_similar_books.join(BX_Books[['Book-Title','Book-Author']])
#print(Painted_House_similar_books.head())

#print(Painted_House_similar_books.sort_values(['Correlation','rating-count'],ascending=[False,False]).head())













