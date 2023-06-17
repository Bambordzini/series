from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')

def get_most_rated_shows(number_of_elements_to_display, page_number):
    print('numer: ', page_number)
    offset_flag = number_of_elements_to_display * (int(page_number) - 1)
    return data_manager.execute_select('''
    SELECT shows.*, string_agg(genres.name, ', ') 
    AS genre_names 
    FROM shows 
    LEFT JOIN show_genres ON shows.id = show_genres.show_id
    JOIN genres ON show_genres.genre_id = genres.id
    GROUP BY shows.id ORDER by rating DESC LIMIT %(limit)s OFFSET %(offset)s''', variables={'limit': number_of_elements_to_display, 'offset': offset_flag})


def get_total_number_of_shows():
     return data_manager.execute_select('SELECT COUNT(*) AS total_rows FROM shows')
 
def get_show(id):
    return data_manager.execute_select("""SELECT title, 
     year, 
     overview, 
     runtime, 
     trailer, 
     homepage, 
     string_agg(genres.name, ', ') AS genres_names, 
     string_agg(actors.name, ', ') AS actors_names, 
     rating FROM shows left join show_genres ON shows.id = show_genres.show_id
     left join show_characters ON shows.id = show_characters.show_id
     left JOIN genres ON show_genres.genre_id = genres.id
     left JOIN actors ON show_characters.actor_id = actors.id WHERE shows.id = %(show_id)s GROUP BY shows.id""", variables={'show_id': id})

    
    

     