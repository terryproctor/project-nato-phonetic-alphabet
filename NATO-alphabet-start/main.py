#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

nato = open(r"C:\Users\terry\OneDrive\100 days python\project nato phonetic alphabet\NATO-alphabet-start\nato_phonetic_alphabet.csv")
nato_df = pd.read_csv(nato)
nato_dict = {row.letter : row.code for (index, row) in nato_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
words = input("Enter word to convert from:\n")

phonetics = [nato_dict[letter.upper()] for letter in words if letter.upper() in nato_dict.keys()]
print(phonetics)
