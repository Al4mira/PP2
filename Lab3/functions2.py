#Function1
def movie_IMBD(movie):
    return movie["imdb"]>5.5

#Function2
def sublist_with_IMBD(movies):
    sublist=[]
    for movie in movies:
        if movie_IMBD(movie):
            sublist.append(movie)
    return sublist  


#Function3
def Category_split(movies, category):
    sublist = []
    for movie in movies:
        if movie["category"] == category:
            sublist.append(movie)
    return sublist


#Function4
def IMBD_average(movie):
    sum_of_IMBD = 0
    movies_count = len(movie)
    for movie in movies:
        sum_of_IMBD+=movie["imdb"]
        average_score =(sum_of_IMBD/movies_count)
    return round(average_score, 3)


#Function5
def Category_Average(movie, category):
    sublist=[]
    cat_sum=0
   
    for movie in movies:
        if movie["category"]==category:
            sublist.append(movie)
            cat_sum+=movie["imdb"]
            average_score = (cat_sum/len(sublist))
    return round(average_score,3)


movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
print(movie_IMBD(movies[0]))
print(movie_IMBD(movies[8]))
print("*****************")

#2
sublist = sublist_with_IMBD(movies)
print(f"{len(sublist)} movies with an IMDB score above 5.5")
print(sublist)
print("*****************")

#3
category = "Romance"
sublist = Category_split(movies, category)
print(f"{len(sublist)} movies with a category {category}")
print(sublist)
print("*****************")

#4
print(f"the average IMDB score: {IMBD_average(movies)}")
print("*****************")

#5
category = "Thriller"
print(f"the average IMDB score for movies with a category {category}: {Category_Average(movies,category)}")
