import webbrowser

class Movie():
	#the valid ratings that can be applied to each movie
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	#defines and stores the parameters for the Movie class
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	#opens the stored youtube trailer url in browser	
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
