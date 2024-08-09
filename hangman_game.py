# 1) generate random existing french word
from faker import Faker

# Créez une instance de Faker pour le français
fake = Faker('fr_FR')

# Générez des mots en français
def generate_random_word():
    random_word = fake.word()
    return random_word

# 2) set up game parameter


# 3) Add undercscore to the hidden word
def add_underscore(word):
    print(word)
    under_scorded_word = []
    for x in word:
        create_underscore = x.replace(x, "_")
        under_scorded_word.append(create_underscore)
    return under_scorded_word


def game():
    random_word = generate_random_word()
    under_scorded_word = add_underscore(random_word)
    new_under_scorded_word = ''.join(under_scorded_word)
    player_life = 5
    player_letter = []
    letter_list = []

    while player_life > 0:
        new_word = []
        for x in random_word:
            if x in letter_list:
                new_word.append(x)
            else:
                new_word.append("_")
        str_new_word = ''.join(new_word)
        print(str_new_word)
        print(f"Life: {player_life}")
        user_letter  = input("Give me one letter from the alphabets\n")
        if user_letter in random_word:
            letter_list.append(user_letter)
            print("You find a letter")
        else:
            player_letter.append(user_letter)
            print("wrong letter ")
            player_life -= 1


game()


