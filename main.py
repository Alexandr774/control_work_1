from utills import load_random_word, statistic_game


def main():
    main_words = load_random_word()
    main_player = statistic_game()
    print("Как вас зовут?")
    user_name = input()
    print(f'Привет {user_name}!')
    print(f'Составь {main_words.len_subword()} слов из слова {main_words.word.upper()}')

    while main_words.len_subword() != main_player.count_words():
        print('Введите слово!')
        input_user = input()
        if main_player.has_uses(input_user) == True:
            print('Слово уже использовано!')
        if input_user == 'stop':
            break
        else:
            if len(input_user) < 3:
                print('Слишком короткое слово')
            else:
                if main_words.checking_words(input_user):
                    print("Слово есть")
                    main_player.add_word(input_user)
                else:
                    print("Слова нет!")

    print(f'Игра завершена угадано {len(main_player.used_words)} слов!')


main()
