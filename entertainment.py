import fresh_tomatoes
import media

gatsby=media.Movie("The Great Gatsby",
                   "A writer and wall street trader, Nick, finds himself drawn to the past and lifestyle of his millionaire neighbor, Jay Gatsby.",
                   "http://www.slantmagazine.com/assets/house/film/posterlabgreatgatsby.jpg",
                   "https://www.youtube.com/watch?v=8ud6haTTfFY")
#print(gatsby.storyline)
batman=media.Movie("The Dark Knight",
                   "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice",
                   "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                   "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")
#print(batman.storyline)
#gatsby.show_trailer()
inception=media.Movie("Inception",
                      "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
                      "http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=d3A3-zSOBT4")

shutter=media.Movie("Shutter Island",
                    "In 1954, a U.S. marshal investigates the disappearance of a murderess who escaped from a hospital for the criminally insane.",
                    "http://ia.media-imdb.com/images/M/MV5BMTMxMTIyNzMxMV5BMl5BanBnXkFtZTcwOTc4OTI3Mg@@._V1_.jpg",
                    "https://www.youtube.com/watch?v=5iaYLCiq5RM")

ryan=("Saving Private Ryan",
      "Following the Normandy Landings, a group of U.S. soldiers go behind enemy lines to retrieve a paratrooper whose brothers have been killed in action.",
      "http://ia.media-imdb.com/images/M/MV5BZjhkMDM4MWItZTVjOC00ZDRhLThmYTAtM2I5NzBmNmNlMzI1XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,679,1000_AL_.jpg",
      "https://www.youtube.com/watch?v=zwhP5b4tD6g")

redemption=("The Shawshank Redemption",
            "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
            "http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SY1000_CR0,0,672,1000_AL_.jpg",
            "https://www.youtube.com/watch?v=6hB3S9bIaco")

movies=[gatsby, batman, inception, shutter, ryan, redemption]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
