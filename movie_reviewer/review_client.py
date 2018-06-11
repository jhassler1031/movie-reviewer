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

#Movies Sub Menu Function ================================================
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

#Reviewers Sub Menu Function ===============================================
def reviewers_sub_menu(url):
    sub_menu_choice = display_sub_menu()

    if sub_menu_choice == "1":
        age = input("Age: ")
        occupation = input("Occupation: ")
        postal_code = input("Zip Code: ")

        requests.post(url, data={'age': age, 'occupation': occupation, 'postal_code': postal_code})
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
Age: {item['age']}
Occupation: {item['occupation']}
Zip Code: {item['postal_code']}
""")
            return True
        elif sub_menu_choice == "3":
            age = input("Age: ")
            occupation = input("Occupation: ")
            postal_code = input("Zip Code: ")

            requests.put(item_url, data={'age': age, 'occupation': occupation, 'postal_code': postal_code})
            return True
        elif sub_menu_choice == "4":
            requests.delete(item_url)
            return True

#Review Sub Menu Function
def reviews_sub_menu(url):
    sub_menu_choice = display_sub_menu()

    if sub_menu_choice == "1":
        stars = input("Stars (1 out of 5): ")
        review_text = input("Review: ")
        movie = input("Movie ID: ")
        reviewer = input("Reviewer ID: ")

        resp = requests.post(url, data={'stars': stars, 'review_text': review_text, 'movie': movie, 'reviewer': reviewer})
        print(resp)
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
Stars: {item['stars']}
Review: {item['review_text']}
Movie: {item['movie']}
Reviewer: {item['reviewer']}
""")
            return True
        elif sub_menu_choice == "3":
            stars = input("Stars (1 out of 5): ")
            review_text = input("Review: ")
            movie = input("Movie ID: ")
            reviewer = input("Reviewer ID: ")

            requests.put(item_url, data={'stars': stars, 'review_text': review_text, 'movie': movie, 'reviewer': reviewer})
            return True
        elif sub_menu_choice == "4":
            requests.delete(item_url)
            return True

#Main Menu Function =======================================================
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
        while reviewers_sub_menu(reviewers_url):
            pass
        return True
    elif main_input == "3":
        reviews = requests.get(reviews_url).json()
        for review in reviews:
            print(f"ID: {review['id']} Movie Reviewed: {review['movie']} Stars: {review['stars']}")
        while reviews_sub_menu(reviews_url):
            pass
        return True
    else:
        return False

#Main Program ============================================================
while main_menu():
    pass
