import media
import fresh_tomatoes
#Code to create instances of class media and create movies website
A_walk_to_remember = media.Movie("A Walk To Remember", "https://images-na.ssl-images-amazon.com/images/M/MV5BZDMzNWFjYzUtY2E1ZC00MzhiLThlOWUtOTkxMTI3MGQ0ZTVmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNTE2ODAyODI@._V1_.jpg", "https://www.youtube.com/watch?v=k3B2XBcp7vA")
The_Mummy = media.Movie("The Mummy", "https://i.ytimg.com/vi/GzorZUuZqEI/maxresdefault.jpg", "https://www.youtube.com/watch?v=IjHgzkQM2Sg")
Terminator = media.Movie("Terminator", "http://worldversus.com/img/terminator.jpg", "https://www.youtube.com/watch?v=jNU_jrPxs-0")
Sholay = media.Movie("Sholay", "http://fm.indsyntest.com/wordpress/wp-content/uploads/1970/01/01/sholay_120810.jpg", "https://www.youtube.com/watch?v=hLhzpe3_V_g")
movies = [A_walk_to_remember, The_Mummy, Terminator, Sholay]
fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.__doc__)

