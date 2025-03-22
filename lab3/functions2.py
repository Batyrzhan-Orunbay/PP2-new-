
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
def imdb(movies):
    name=input("name:")
    for movie in movies:
        if movie["name"]==name:
            if movie["imdb"]>5.5:
                return True
    return False
print(imdb(movies))


#2
def filter_movies(movies):
    result=[]
    for movie in movies:
        if movie["imdb"]>5.5:
            result.append(movie)
    return result
print(filter_movies(movies))
    

#3
def samecategory(category):
    names = []
    for movie in movies:
        if movie["category"] == category:
            names.append(movie["name"])
    return names
print(samecategory("Romance"))


#4
def average():
    a = 0
    for movie in movies:
        a = movie["imdb"] + a
    return a / len(movies)
print(average())


#5
def avgcategory(category):
    avg = 0
    s = 0
    for i in movies:
        if i["category"] == category:
            avg += i['imdb']
            s += 1
    return avg / s
print(avgcategory("Thriller"))
    