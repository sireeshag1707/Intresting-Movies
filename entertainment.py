import fresh_tomatoes
import media
student_ofthe_year=media.Movie("student_ofthe_year",
                               "a boy loves a girl in their college",
                               "https://i.pinimg.com/originals/08/5a/12/085a12d23ce7aae4d807e4fe5ee13cc4.jpg",
                               "https://youtu.be/fivOhPjX9YM")
student_ofthe_year.show_trailer()
now_you_see_me2=media.Movie("now_you_see_me2",
                            "five members play with people",
                            "https://images-na.ssl-images-amazon.com/images/I/61I25k4TvuL._SY679_.jpg",
                            "https://www.youtube.com/watch?v=InqU8CLwbPg")
savyasachi=media.Movie("savyasachi",
                       "he had a twin brother",
                       "https://i.pinimg.com/736x/0d/1f/06/0d1f06f4e25e968c17caa7924a0cc5af.jpg",
                       "https://www.youtube.com/watch?v=An9lC-F_HMg&t=23s")
insidious=media.Movie("insidious",
                        "horror story",
                        "https://movieposters2.com/images/1133133-b.jpg",
                        "https://www.youtube.com/watch?v=acQyrwQyCOk")
size_zero=media.Movie("size_zero",
                      "fat girl story",
                      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSR0Z51doxBrVT5IW_SLOo79uz7Q5Vr5ZTI6Tvye7a-CF4whb4RKw",
                      "https://youtu.be/Qz_TznvtY-M")
thamasha=media.Movie("thamasha",
                 "a boy and girl love story",
                 "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwZbPh4yWUdgCOf_8Rce_qIrbN1bSphDkrplKuEafnGfBf3cYz",
                 "https://youtu.be/o-e5eWVCzx8")
movies=[student_ofthe_year,now_you_see_me2,savyasachi,insidious,size_zero,thamasha]
fresh_tomatoes.open_movies_page(movies)
