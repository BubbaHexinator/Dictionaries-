# Create three dictionaries with classmates' names as keys, location, years and tech as values.
classmate_city = {
    "Anna": "London",
    "Mohammad": "Hong Kong",
    "Viral": "Seattle",
    "Lizette": "Chicago"
}

classmate_years = {
    "Anna": 7,
    "Mohammad": 0,
    "Viral": 5,
    "Lizette": 2
}

classmate_tech = {
    "Anna": "Java",
    "Mohammad": "Microsoft Office",
    "Viral": "C#",
    "Lizette": "JavaScript"
}



# Create a series from each dictionary
series_of_people = pd.Series(classmate_city, name = "City")
series_of_years = pd.Series(classmate_years, name = "Years")
series_of_tech = pd.Series(classmate_tech, name = "Tech")

# Preview one of the Series
series_of_people
