# ------------------------------


def new_game():                                                                             # neues Spiel wird gestartet

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print('-------------------------')
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input('Eingeben (A, B, C, oder D): ')
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------------


def check_answer(answer, guess):                                                            # überprüfung der Antwort

    while guess not in ['A', 'B', 'C', 'D']:
        print('Ungültige Eingabe. Bitte geben Sie A, B, C oder D ein.')
        guess = input('Eingeben (A, B, C, oder D): ')
        guess = guess.upper()

    if answer == guess:
        print('-------------------------')
        print('RICHTIG!')
        return 1
    else:
        print('-------------------------')
        print('FALSCH!')
        return 0

# --------------------------------


def display_score(correct_guesses, guesses):                                                # Anzeige der Punkte
    print('------------------------------------------')
    print('             ERGEBNISSE')
    print('------------------------------------------')

    print('Antworten: ', end=' ')
    for i in questions:
        print(questions.get(i), end=' ')
    print()

    print('Vermutungen: ', end=' ')
    for i in guesses:
        print(i, end=' ')
    print()

    score = int(correct_guesses)
    print('Deine Punktzahl: '+str(score)+' von 10')

    quote = int((correct_guesses / len(questions))*100)
    print('Deine Quote: '+str(quote)+'% von 100%')

# ---------------------------------


def play_again():                                                                           # Abfrage für die Schleife

    print('--------------------------------')
    response = input(' Quiz neu starten? (Ja oder Nein): ')
    response = response.upper()
    print('--------------------------------')

    if response == 'JA' or response == 'J':
        return True
    elif response == 'NEIN' or response == 'N':
        return False
    else:
        print('Ungültige Eingabe!')
        return play_again()

# ---------------------------------


questions = {                                                                               # Fragen
    'Die größte Stadt im Saarland und gleichzeitig die Landeshauptstadt ist ..? ': 'A',
    'Wie hieß die Währung von Österreich vor Einführung des Euros? ': 'B',
    'Eine beliebte Fernsehserie der 1980er Jahre war "Trio mit vier .."? ': 'B',
    'Was zählt nicht zu den Edelgasen? ': 'D',
    'Welches Tier nennt der Zoologe wissenschaftlich "Argyroneta aquatica"? ': 'A',
    'Wo wird ein "Winkeralphabet" benutzt? ': 'C',
    'Welcher Planet ist ein "rostiger Planet"? ': 'A',
    'Einen Papst mit welchem Namen gab es nicht? ': 'D',
    'Wann beginnt für gläubige Juden der Sabbat, ein Tag der Freude und des Feierns? ': 'C',
    'Welcher "Großkontinent" beinhaltet die größte zusammenhängende Landmasse der Erde? ': 'C',
}

options = [['A. Saarbrücken', 'B. Saargemünd', 'C. Friedrichsthal', 'D. Merzig'],           # Antworten
           ['A. Mark', 'B. Schilling', 'C. Peseta', 'D. Franc'],
           ['A. Hände', 'B. Fäusten', 'C. Colts', 'D. Augen'],
           ['A. Neon', 'B. Helium', 'C. Radon', 'D. Vollgas'],
           ['A. Wasserspinne', 'B. Feuersalamander', 'C. Afrikanischer Strauß', 'D. Erdmännchen'],
           ['A. Langlauf', 'B. Zugverkehr', 'C. Schifffahrt', 'D. Autobahn'],
           ['A. Mars', 'B. Venus', 'C. Jupiter', 'D. Erde'],
           ['A. Franziskus', 'B. Johannes Paul II.', 'C. Benedikt XVI.', 'D. Johannes XX.'],
           ['A. am Sonntagmorgen', 'B. am Samstagabend', 'C. am Freitagabend', 'D. am Samstagmorgen'],
           ['A. Antarktika', 'B. Amerika', 'C. Afrika-Eurasien', 'D. Ozeanien']]

new_game()                                                                                  # Start des Spiels

while play_again():                                                                         # Schleife
    new_game()

print('Bye!')
