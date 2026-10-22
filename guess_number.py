"""Игра «Угадай число»."""

from random import randint


def play_round():
    number = randint(1, 100)
    attempts = 0
    print('\nУгадайте число от 1 до 100')

    while True:
        try:
            guess = int(input('Введите число: '))
        except ValueError:
            print('Введите целое число от 1 до 100.')
            continue

        if not 1 <= guess <= 100:
            print('Число должно быть от 1 до 100.')
            continue

        attempts += 1
        if guess < number:
            print('Ваше число меньше того, что загадано.')
        if guess > number:
            print('Ваше число больше того, что загадано.')
        if guess == number:
            print(f'Вы угадали число! Количество попыток: {attempts}.')
            break


def main():
    print('Игра «Угадай число»')
    while True:
        play_round()
        answer = input('Сыграть ещё раз? (д/н): ').strip().lower()
        if answer not in ('д', 'да'):
            print('Спасибо за игру!')
            break


if __name__ == '__main__':
    main()
