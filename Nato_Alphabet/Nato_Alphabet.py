from token import OP
import pandas as pd
import csv


#Convert csv into dictionary:

# data = pd.read_csv("nato_phonetic_alphabet.csv")


# nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}



# ## Create a list of the phonetic code words from a word that the user inputs.

# user_input = input("Enter the word: ").upper()

# phonetic_code = [nato_dict[letter] for letter in user_input]
# print(phonetic_code)


# with open("Automobile_data.csv") as car_file:
#     csv_reader = csv.DictReader(car_file)
#     data = [row for row in csv_reader]
#     print(data)

data = pd.read_csv("Automobile_data.csv")



car_dict = {index:company for (index, company) in data["company"].items()}

user_choice = input("Select the company: ")

selection = data[data["company"] == user_choice]
print(selection.to_string())




# company_name = []
