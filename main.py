import csv
import random

def read_csv_to_dict(filename):
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # This line is needed to skip the header
        return {rows[1]: rows[0] for rows in csv_reader}

def quiz(word_dict):
    word, translation = random.choice(list(word_dict.items()))
    user_answer = input(f'What is the German translation for the Romanian word "{word}"?\n')
    print(f'You answered: {user_answer}')
    print(f'The correct answer is: {translation}\n')

def main():
    filename = 'example.csv' 
    word_dict = read_csv_to_dict(filename)
    while True:
        quiz(word_dict)

if __name__ == "__main__":
    main()