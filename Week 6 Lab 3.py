'''
Author: Muhammad Moiz Farooq/20240779
Whitecliffe College , AKL
'''

class Movie:
    def __init__(self, title, genre, year):
        self.title = title
        self.genre = genre
        self.year = year
        self.available = True

    def mark_as_rented(self):
        self.available = False

    def mark_as_available(self):
        self.available = True

    def __str__(self):
        return f"Title: {self.title}, Genre: {self.genre}, Year: {self.year}. {'Available' if self.available else 'Rented'}"


class Customer:
    def __init__(self, name):
        self.name = name
        self.rented_movies = []

    def rent_movie(self, movie):
        if movie.available:
            movie.mark_as_rented()
            self.rented_movies.append(movie)
            print(f"{self.name} rented {movie.title}")
        else:
            print(f"{movie.title} is not available.")

    def return_movie(self, movie):
        if movie in self.rented_movies:
            movie.mark_as_available()
            self.rented_movies.remove(movie)
            print(f"{self.name} returned {movie.title}")
        else:
            print(f"{self.name} did not rent {movie.title}")

    def list_rented_movies(self):
        if self.rented_movies:
            print(f"{self.name}'s Rented Movies:")
            for movie in self.rented_movies:
                print(movie)
        else:
            print(f"{self.name} has no rented movies.")


class RentalStore:
    def __init__(self):
        self.movies = []
        self.customers = {}

    def add_movie(self, movie):
        self.movies.append(movie)

    def list_movies(self):
        if self.movies:
            print("Available movies:")
            for movie in self.movies:
                print(movie)
        else:
            print("No movies available.")

    def find_movie(self, title):
        for movie in self.movies:
            if title.lower() == movie.title.lower():
                return movie
        return None

    def add_customer(self, name):
        self.customers[name] = Customer(name)

    def get_customer(self, name):
        return self.customers.get(name)


def menu():
    print("Movie Rental System Menu")
    print("1. List Available Movies")
    print("2. Rent a Movie")
    print("3. Add a Movie to Store")
    print("4. Return a Movie")
    print("5. List Rented Movies")
    print("6. Exit")


def main():
    store = RentalStore()
    store.add_movie(Movie("The Matrix", "Sci-Fi", 1999))
    store.add_movie(Movie("Inception", "Sci-Fi", 2010))
    store.add_movie(Movie("The Social Network", "Drama", 2010))
    store.add_movie(Movie("The Godfather", "Crime", 1972))

    store.add_customer("Alice")
    store.add_customer("Bob")

    while True:
        menu()
        choice = input('Enter your choice: ').strip()

        if choice == "":
            continue
        elif choice == "1":
            store.list_movies()
        elif choice == "2":
            customer_name = input("Enter your name: ").strip()
            customer = store.get_customer(customer_name)
            if not customer:
                print("Customer not found.")
                continue
            movie_title = input("Enter movie title to rent: ").strip()
            movie = store.find_movie(movie_title)
            if not movie:
                print("Movie not found.")
                continue
            customer.rent_movie(movie)
        elif choice == "3":
            title = input("Enter movie title: ").strip()
            genre = input("Enter movie genre: ").strip()
            year = int(input("Enter movie year: ").strip())
            store.add_movie(Movie(title, genre, year))
            print(f"Movie {title} added to the store.")
        elif choice == "4":
            customer_name = input("Enter your name: ").strip()
            customer = store.get_customer(customer_name)
            if not customer:
                print("Customer not found.")
                continue
            movie_title = input("Enter movie title to return: ").strip()
            movie = store.find_movie(movie_title)
            if not movie:
                print("Movie not found.")
                continue
            customer.return_movie(movie)
        elif choice == "5":
            customer_name = input("Enter your name: ").strip()
            customer = store.get_customer(customer_name)
            if not customer:
                print("Customer not found.")
                continue
            customer.list_rented_movies()
        elif choice == "6":
            print("Existing....")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
if __name__ == "__main__" :
    main()     
