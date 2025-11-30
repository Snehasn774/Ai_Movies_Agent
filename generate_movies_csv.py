import pandas as pd

movies = [
    # Kannada – Yash
    ["KGF Chapter 1", "Yash", "Kannada", 2018, "Action"],
    ["KGF Chapter 2", "Yash", "Kannada", 2022, "Action"],
    ["Masterpiece", "Yash", "Kannada", 2015, "Action"],
    ["Mr. and Mrs. Ramachari", "Yash", "Kannada", 2014, "Romance"],
    ["Googly", "Yash", "Kannada", 2013, "Romance"],
    ["Santhu Straight Forward", "Yash", "Kannada", 2016, "Action"],
    ["Lucky", "Yash", "Kannada", 2012, "Romance"],
    ["Rajadhani", "Yash", "Kannada", 2011, "Drama"],
    ["Modalasala", "Yash", "Kannada", 2010, "Romance"],
    ["Drama", "Yash", "Kannada", 2012, "Drama"],

    # Kannada – Puneeth Rajkumar
    ["Raajakumara", "Puneeth Rajkumar", "Kannada", 2017, "Family"],
    ["Yuvarathnaa", "Puneeth Rajkumar", "Kannada", 2021, "Action"],
    ["Natasaarvabhowma", "Puneeth Rajkumar", "Kannada", 2019, "Action"],
    ["Power", "Puneeth Rajkumar", "Kannada", 2014, "Action"],
    ["Milana", "Puneeth Rajkumar", "Kannada", 2007, "Romance"],

    # Telugu – Allu Arjun
    ["Pushpa", "Allu Arjun", "Telugu", 2021, "Action"],
    ["Ala Vaikunthapuramuloo", "Allu Arjun", "Telugu", 2020, "Drama"],
    ["Sarrainodu", "Allu Arjun", "Telugu", 2016, "Action"],
    ["DJ", "Allu Arjun", "Telugu", 2017, "Action"],
    ["Race Gurram", "Allu Arjun", "Telugu", 2014, "Action"],

    # Telugu – Mahesh Babu
    ["Maharshi", "Mahesh Babu", "Telugu", 2019, "Drama"],
    ["Sarileru Neekevvaru", "Mahesh Babu", "Telugu", 2020, "Action"],
    ["Spyder", "Mahesh Babu", "Telugu", 2017, "Thriller"],
    ["Srimanthudu", "Mahesh Babu", "Telugu", 2015, "Drama"],
    ["Businessman", "Mahesh Babu", "Telugu", 2012, "Action"],

    # Hindi – Shah Rukh Khan
    ["Jawan", "Shah Rukh Khan", "Hindi", 2023, "Action"],
    ["Pathaan", "Shah Rukh Khan", "Hindi", 2023, "Action"],
    ["Chennai Express", "Shah Rukh Khan", "Hindi", 2013, "Comedy"],
    ["Raees", "Shah Rukh Khan", "Hindi", 2017, "Action"],
    ["Dilwale", "Shah Rukh Khan", "Hindi", 2015, "Romance"],

    # Hindi – Deepika Padukone
    ["Padmaavat", "Deepika Padukone", "Hindi", 2018, "Drama"],
    ["Chennai Express", "Deepika Padukone", "Hindi", 2013, "Comedy"],
    ["Bajirao Mastani", "Deepika Padukone", "Hindi", 2015, "Drama"],
    ["Piku", "Deepika Padukone", "Hindi", 2015, "Drama"],
    ["Tamasha", "Deepika Padukone", "Hindi", 2015, "Romance"],

    # English – Tom Cruise
    ["Top Gun Maverick", "Tom Cruise", "English", 2022, "Action"],
    ["Mission Impossible Fallout", "Tom Cruise", "English", 2018, "Action"],
    ["Mission Impossible Rogue Nation", "Tom Cruise", "English", 2015, "Action"],
    ["Oblivion", "Tom Cruise", "English", 2013, "Sci-Fi"],
    ["Jack Reacher", "Tom Cruise", "English", 2012, "Thriller"],

    # English – Emma Watson
    ["Harry Potter and the Deathly Hallows", "Emma Watson", "English", 2011, "Fantasy"],
    ["Beauty and the Beast", "Emma Watson", "English", 2017, "Romance"],
    ["Little Women", "Emma Watson", "English", 2019, "Drama"],
    ["Noah", "Emma Watson", "English", 2014, "Drama"],
    ["The Circle", "Emma Watson", "English", 2017, "Thriller"]
]

df = pd.DataFrame(movies, columns=["title", "actor", "language", "year", "genre"])
df.to_csv("movies.csv", index=False)

print("movies.csv successfully created with", len(df), "movies!")
