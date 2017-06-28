import media
import fresh_tomatoes

#create all instances of favorite movies of all time broken down into
#movie title, a short description, the associated poster and trailer on youtube
moonlight = media.Movie("Moonlight",
			"A portrait of contemporary African American life, identity, family, friendship and love",
			"https://upload.wikimedia.org/wikipedia/en/thumb/8/84/Moonlight_%282016_film%29.png/220px-Moonlight_%282016_film%29.png",
			"https://youtu.be/9NJj12tJzqc")

full_metal_jacket = media.Movie("Full Metal Jacket",
			"The experience of the Vietnam War shown through a group of raw Marine volunteers",
			"https://upload.wikimedia.org/wikipedia/en/thumb/9/99/Full_Metal_Jacket_poster.jpg/220px-Full_Metal_Jacket_poster.jpg",
			"https://youtu.be/x9f6JaaX7Wg")

amelie = media.Movie("Amelie",
			"Experience contemporary Parisian life through the story of a shy waitress who decides to change lives for the better",
			"https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Amelie_poster.jpg/220px-Amelie_poster.jpg",
			"https://youtu.be/HUECWi5pX7o")

la_ceremonie = media.Movie("La Ceremonie",
			"A film inspired by the novel A Judgement in Stone by Ruth Rendell",
			"https://upload.wikimedia.org/wikipedia/en/5/5a/Laceremonieposter.jpg",
			"https://youtu.be/H63eq2zYsI0")

#array storing the movie instances						
movies = [moonlight, full_metal_jacket, amelie, la_ceremonie]
#generates web page with function from fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
