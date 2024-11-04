#!/usr/bin/env/python3
# Jeff Bohn
# 11/3/2024
# Chapter 17 - Working with a Database


########################################
########### Chapter 17-2 Lab ###########
########################################


import db
from objects import Movie
from menus import display_title, display_menu, display_categories


def display_movies(movies, title_term):
    print("\nMOVIES - " + title_term)
    line_format = "{:3s} {:37s} {:6s} {:5s} {:10s}"
    print(line_format.format("ID", "Name", "Year", "Mins", "Category"))
    print("-" * 64)
    for movie in movies:
        print(line_format.format(str(movie.id), movie.name.title(),
                                 str(movie.year), str(movie.minutes),
                                 movie.category.name))
    print()    

def display_movies_by_category():
    category_id = int(input("Category ID: "))
    category = db.get_category(category_id)
    if category == None:
        print("There is no category with that ID.\n")
    else:
        print()
        movies = db.get_movies_by_category(category_id)
        display_movies(movies, category.name.upper())
    
def display_movies_by_year():
    year = int(input("Year: "))
    print()
    movies = db.get_movies_by_year(year)
    display_movies(movies, str(year))


########### DISPLAY MOVIES BY MINUTES ###########
def display_movies_by_minutes():
    minutes = input(f"Enter the maximum numbers of minutes for a movie : ")
    movies = db.get_movies_by_minutes(minutes)
    display_movies(movies, f"Less than {minutes} minutes")
    # for i in movies:
    #     print(f"{i['name']:<30} Minutes: {i['minutes']}")


def add_movie():
    name        = input("Name: ")
    year        = int(input("Year: "))
    minutes     = int(input("Minutes: "))
    category_id = int(input("Category ID: "))
    
    category = db.get_category(category_id)
    if category == None:
        print("There is no category with that ID. Movie NOT added.\n")
    else:        
        movie = Movie(name=name, year=year, minutes=minutes,
                      category=category)
        db.add_movie(movie)    
        print(name + " was added to database.\n")


####### MODIFIED DELETE FUNCTION #######
def delete_movie():
    movie_id = int(input("Movie ID: "))
    while True:
        answer = input(f"Are you sure you want to delete Movie {movie_id} (y or n): ").lower()
        if answer == "y":
            db.get_movie(movie_id)
            print("Movie ID " + str(movie_id) + " was deleted from database.\n")
        else:
            display_menu()
            display_categories(db)
        break
        
        
        
def main():
    db.connect()
    display_title()
    display_categories(db)
    while True:        
        command = input("Command: ")
        if command == "menu":
            display_menu()
            display_categories(db)
        elif command == "cat":
            display_movies_by_category()
        elif command == "year":
            display_movies_by_year()
        elif command == "add":
            add_movie()
        elif command == "del":
            delete_movie()
        elif command == "min":
            display_movies_by_minutes()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()
    db.close()
    print("Bye!")

if __name__ == "__main__":
    main()
