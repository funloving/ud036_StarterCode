import webbrowser
# Code to create class with general movie attributes
class Movie():
    def __init__(self, movie_title,poster_image,trailer_youtube):
        #valid_ratings = ["G","R",GR"]
        self.title=movie_title
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    