def my_favourite_movies(*favourites):
    """Print any number of user's favorite movies."""
    print("\nFavorite movies of user are: ")
    for favourite in favourites:
        print(f"- {favourite}")
    
def my_favourite_movies_and_year(year, *favourites):
    """Print any number of user's favorite movies."""
    print(f"\nFavorite movies of user in the year {year} are: ")
    for favourite in favourites:
        print(f"- {favourite}")
    
