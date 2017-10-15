import media
import fresh_tomatoes
# Code to create instances of class media and create movies website
# This is the primary code that calls the other classes. To create the links
# for other movies, simply fill out the details below
# for example movie = media.Movie('<Movie Name>',thumbnail link,trailer link)
A_walk_to_remember = media.Movie("A Walk To Remember", "http://bit.ly/2vFLXV7",
                                 "https://www.youtube.com/watch?v=k3B2XBcp7vA")
The_Mummy = media.Movie("The Mummy",
                        "https://i.ytimg.com/vi/GzorZUuZqEI/maxresdefault.jpg",
                        "https://www.youtube.com/watch?v=IjHgzkQM2Sg")
Terminator = media.Movie("Terminator",
                         "http://worldversus.com/img/terminator.jpg",
                         "https://www.youtube.com/watch?v=jNU_jrPxs-0")
Sholay = media.Movie("Sholay", "http://bit.ly/2idIuLE",
                     "https://www.youtube.com/watch?v=hLhzpe3_V_g")
movies = [A_walk_to_remember, The_Mummy, Terminator, Sholay]
fresh_tomatoes.open_movies_page(movies)
# print (media.Movie.__doc__)
