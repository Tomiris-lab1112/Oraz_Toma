#Python functions for movies
# Dictionary of movies
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

#1. Проверка рейтинга одного фильма 
'''
Функция, которая получает один фильм и возвращает True, если его IMDB больше 5.5, иначе будет False.
'''
def is_good_movie(movie):
    return movie["imdb"] > 5.5

#Пример:
print(is_good_movie(movies[0]))  # True


#2. Список фильмов с IMDB > 5.5 
'''
Функция получает весь список фильмов и возвращает новый список только с теми, у которых рейтинг больше 5.5.
''' 
def good_movies_list(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

#Пример:
good_list = good_movies_list(movies)
for m in good_list:
    print(m["name"], m["imdb"])


#3. Фильмы по категории
'''
Функция получает название категории (например, "Romance") и возвращает список фильмов только этой категории.
'''
def movies_by_category(movies, category_name):
    return [movie for movie in movies if movie["category"].lower() == category_name.lower()]

#Пример:
romance_movies = movies_by_category(movies, "Romance")
for m in romance_movies:
    print(m["name"], m["imdb"])


#4.  Средний рейтинг IMDB для списка фильмов
'''
Функция получает список фильмов и возвращает средний рейтинг IMDB.
'''
def average_imdb(movies_list):
    if not movies_list:
        return 0
    total = sum(movie["imdb"] for movie in movies_list)
    return total / len(movies_list)

#Пример:
print(average_imdb(movies))  # Средний рейтинг всех фильмов


#5. Средний рейтинг IMDB для категории
'''
Функция получает название категории и возвращает средний рейтинг только для фильмов этой категории.
'''
def average_imdb_by_category(movies, category_name):
    category_movies = movies_by_category(movies, category_name)
    return average_imdb(category_movies)

#Пример:
print(average_imdb_by_category(movies, "Romance"))  # Средний рейтинг Romance


'''
Пример использования: 
analyzer = MovieAnalyzer(movies)

# Проверка одного фильма
print(analyzer.is_good_movie(movies[0]))  # True

# Все фильмы с рейтингом > 5.5
for m in analyzer.good_movies_list():
    print(m["name"], m["imdb"])

# Фильмы категории "Romance"
for m in analyzer.movies_by_category("Romance"):
    print(m["name"], m["imdb"])

# Средний рейтинг всех фильмов
print("Средний рейтинг всех фильмов:", analyzer.average_imdb())

# Средний рейтинг фильмов категории "Romance"
print("Средний рейтинг Romance:", analyzer.average_imdb_by_category("Romance"))
'''