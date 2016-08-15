
import fresh_tomatoes
import movie



judge_dredd = movie.Movie("Judge Dredd",
                        "About the justice",
                        "http://vignette2.wikia.nocookie.net/judgedredd/images/a/af/Judge-dredd-movie-poster-1995-1020256541.jpeg",
                        "https://www.youtube.com/watch?v=43-BefmjMFg")
#print(judge_dredd.storyline)
#judge_dredd.show_trailer()


robocop = movie.Movie("RoboCop",
                        "About the honor",
                        "http://www.impawards.com/1987/posters/robocop_xlg.jpg",
                        "https://www.youtube.com/watch?v=zbCbwP6ibR4")


terminator = movie.Movie("Terminator",
                        "About the bots",
                        "http://imgc.allpostersimages.com/images/P-473-488-90/17/1723/KK53D00Z/posters/the-terminator.jpg",
                        "https://www.youtube.com/watch?v=W7cqcjon4gI")



movies =  [judge_dredd, robocop, terminator]
#fresh_tomatoes.open_movies_page(movies)
print(movie.Movie.VALID_RATINGS)      
print(movie.Movie.__doc__)
print(movie.Movie.__name__)
print(movie.Movie.__module__)
