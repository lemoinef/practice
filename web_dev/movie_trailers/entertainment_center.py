import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

# print(toy_story.storyline)

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                    "http://www.youtube.com/watch?v=-9ceBgWV8io")
# print(avatar.storyline)

back_to_the_future = media.Movie("Back To The Future",
                                "Marty McFly issent back in time to 1955, meets his future parents in high school.",
                                "https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",
                                "https://www.youtube.com/watch?v=qvsgGtivCgs")

# back_to_the_future.show_trailer()
indiana_jones = media.Movie("Raiders of the Lost Ark",
                            "An explorer finds the ark",
                            "https://upload.wikimedia.org/wikipedia/en/4/4c/Raiders_of_the_Lost_Ark.jpg",
                            "https://www.youtube.com/watch?v=XkkzKHCx154")

empire_strikes_back = media.Movie("The Empire Strikes Back", "The Empire is in pursuit of Luke Skywalker",
                                  "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                                  "https://www.youtube.com/watch?v=JNwNXF9Y6kY")

movies = [empire_strikes_back, indiana_jones, back_to_the_future]
fresh_tomatoes.open_movies_page(movies)
