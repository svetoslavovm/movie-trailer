import media
import fresh_tomatoes

# Create 'Toy Story' movie instance
toy_story = media.Movie(
    'Toy Story',
    'A story about a bunch of toys that come alive',
    ('http://media.comicbook.com/uploads1/2015/03/' +
        'group-disney-announces-toy-story-4-is-happening-126226.jpeg'),
    'https://www.youtube.com/watch?v=KYz2wyBy3kc')

# Create 'School of Rock' movie instance
school_of_rock = media.Movie(
    'School of Rock',
    'We don\'t need education',
    ('http://ia.media-imdb.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXk' +
        'FtZTcwNjczMTQyMQ@@._V1_SX640_SY720_.jpg'),
    'https://www.youtube.com/watch?v=5afGGGsxvEA')

# Create 'Ratatouille' movie instance
ratatouille = media.Movie(
    'Ratatouille',
    'He\'s dying to become a chef',
    ('http://ia.media-imdb.com/images/M/MV5BMTMzODU0NTkxMF5BMl5BanBnXk' +
        'FtZTcwMjQ4MzMzMw@@._V1_SX640_SY720_.jpg'),
    'https://www.youtube.com/watch?v=R1tcS0pBgY8')

movies = [toy_story, school_of_rock, ratatouille]
fresh_tomatoes.open_movies_page(movies)

# print ( media.Movie.__doc__ )
# print ( media.Movie.__name__ + ' is in ' + media.Movie.__module__ + '.py' )
# print ( toy_story.get_title() )
