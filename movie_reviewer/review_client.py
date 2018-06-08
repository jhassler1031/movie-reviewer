#API client interface through the CLI --- Hard Mode
import requests

movies_url = "http://localhost:8000/movies/"
reviewers_url = "http://localhost:8000/reviewers/"
reviews_url = "http://localhost:8000/reviews/"

def display_sub_menu():
    print("""
What would you like to do?
1) Add an entry
2) View full details of a single entry
3) Modify an entry
4) Delete an entry
Press <enter> to return to the main menu
""")
    sub_menu_input = input("> ")
    return sub_menu_input

def get_id():
    item_id = input("Enter the ID number: ")
    return item_id

def movies_sub_menu(url):
    sub_menu_choice = display_sub_menu()

    if sub_menu_choice == "1":
        title = input("Title: ")
        imdb_link = input("IMDB link: ")
        director = input("Director: ")
        release_year = input("Release year: ")
        genre = input("Genre: ")

        requests.post(url, data={'title': title, 'imdb_link': imdb_link, 'director': director, \
                                'release_year': release_year, 'genre': genre})
        return True
    elif sub_menu_choice == "":
        return False
    else:
        item_id = get_id()
        item_url = url + item_id
        item = requests.get(item_url).json()

        if sub_menu_choice == "2":
            print(f"""
ID: {item['id']}
Title: {item['title']}
IMDB Link: {item['imdb_link']}
Director: {item['director']}
Year Released: {item['release_year']}
Genre: {item['genre']}
""")
            return True
        elif sub_menu_choice == "3":
            title = input("Title: ")
            imdb_link = input("IMDB link: ")
            director = input("Director: ")
            release_year = input("Release year: ")
            genre = input("Genre: ")

            requests.put(item_url, data={'title': title, 'imdb_link': imdb_link, 'director': director, \
                                    'release_year': release_year, 'genre': genre})
            return True
        elif sub_menu_choice == "4":
            requests.delete(item_url)
            return True


def main_menu():
    print("""
What would you like to view?
1) Movies
2) Reviewers
3) Reviews
Press <enter> to exit
""")
    main_input = input("> ")

    if main_input == "1":
        movies = requests.get(movies_url).json()
        for movie in movies:
            print(f"ID: {movie['id']} Title: {movie['title']} Released: {movie['release_year']} Genre: {movie['genre']}")
        while movies_sub_menu(movies_url):
            pass
        return True
    elif main_input == "2":
        reviewers = requests.get(reviewers_url).json()
        for reviewer in reviewers:
            print(f"ID: {reviewer['id']} Age: {reviewer['age']} Occupation: {reviewer['occupation']} Zip: {reviewer['postal_code']}")

        return True
    elif main_input == "3":
        reviews = requests.get(reviews_url).json()
        for review in reviews:
            print(f"ID: {review['id']} Movie Reviewed: {review['movie'].title} Stars: {review['stars']}")

        return True
    else:
        return False
    #return main_input






while main_menu():
    pass
