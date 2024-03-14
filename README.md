***ОПИСАНИЕ НА РУССКОМ***

В данном репозитории находится код консольной игры "Поле чудес".  Суть игры - как можно раньше угадать, какое слово зашифровано, по сути классическая версия "Поля чудес", но возможно, в следующих версиях будут какие-то авторские дополнения. Программа написана полностью на языке Python. Чтобы запустить игру, просто скачайте сам файл и запустите его (условие: наличие Python IDLE на вашем устройстве) или скопируйте содержимое файла и вставьте его в какой-либо файл формата .py на своем устройстве и запустите (опять же, Python IDLE также должен быть установлен). Чтобы начать работать со словом, предложенным программой, вам следует попробовать угадать букву угадываемого слова и ввести ее в консоль (игра к регистру ввода букв нечувствительна), используя буквы алфавита того языка, словом которого является текущее угадываемое слово. Если же вы хотите попробовать ввести все слово целиком, вводите его целиком, вместо того, чтобы угадывать букву слова. Программа отличит ввод слова от ввода буквы и в случае совпадения текущего угадываемого слова с пользовательским вариантом ввода слова без учета регистра поздравит Вас с победой. Вы можете воспользоваться командами, которые позволяют узнать какие-либо данные о игровом процессе или сменить условия игрового процесса. Каждая из них начинается знаком "/". Программа отличит ввод команды от ввода буквы либо слова. Полный перечень команд:
/cm (сокращение change mode) - сменить визуал игры с продвинутого на упрощенный 
либо с упрощенного на продвинутый.
/used - использованные в период угадывания данного слова буквы русского либо английского алфавита
(в зависимости от того, словом какого языка является текущее угадываемое слово).
/rest - те буквы русского либо английского алфавита
(в зависимости от того, словом какого языка является текущее угадываемое слово),
которые пока не были использованы при угадывании данного слова.
/cl (сокращение change language) - сменить язык, словами которого будут являться
слова, которые будут предлагаться для угадывания после успешного отгадывания 
текущего слова (язык слов меняется либо с русского на английский, либо с английского
на русский).
ОБРАТИТЕ ВНИМАНИЕ: при использовании этой команды сменится язык предлагаемых
для угадывания слов, сам же язык интерфейса программы всегда русский.
/help - вывод текста-помощника. По умолчанию выводится в начале выполнения программы.
В упрощенном визуале данные выводятся текстом стандартного размера. Анимация салюта при угадывании слова
не выводится.
В продвинутом режиме каждый символ текущего угадываемого символа по сравнению с любой буквой из этого
документа в несколько раз больше и выполнен псевдографикой (только, если угадывается английское слово). 
После того, как слово успешно отгадано, появляется анимация салюта.


***ОПИСАНИЕ НА АНГЛИЙСКОМ***

This repository contains the code for the console game "Field of Miracles". The essence of the game is to guess as early as possible which word is encrypted, essentially a classic version of “Field of Miracles”, but perhaps in future versions there will be some author’s additions. The program is written entirely in Python. To run the game, simply download the file itself and run it (condition: Python IDLE on your device) or copy the contents of the file and paste it into some .py file on your device and run (again, Python IDLE must also be installed). To start working with a word suggested by the program, you should try to guess the letter of the guessed word and enter it into the console (the game is case-insensitive), using the letters of the alphabet of the language whose word is the current word being guessed. If you want to try typing the entire word, enter the entire word instead of guessing the letter of the word. The program will distinguish between entering a word and entering a letter, and if the current guessed word matches the user's case-insensitive word entry, it will congratulate you on your victory. You can use commands that allow you to find out any data about the gameplay or change the conditions of the gameplay. Each of them begins with a "/". The program will distinguish between entering a command and entering a letter or word. Full list of commands:
/cm (short for change mode) - change the game visuals from advanced to simplified
or from simplified to advanced.
/used - letters of the Russian or English alphabet used during the period of guessing a given word
(depending on which language the current guessed word is a word).
/rest - those letters of the Russian or English alphabet
(depending on which language the current word being guessed is a word),
which have not yet been used when guessing this word.
/cl (abbreviation change language) - change the language whose words will be
words that will be offered for guessing after successful guessing
current word (the language of the words changes either from Russian to English, or from English
into Russian).
PLEASE NOTE: Using this command will change the language of the suggested
to guess words, the program interface language itself is always Russian.
/help - displays help text. By default, it is displayed at the beginning of program execution.
In a simplified visual, data is displayed in standard text size. Fireworks animation when guessing a word
not displayed.
In advanced mode, each character of the current character being guessed compared to any letter from that
the document is several times larger and is made in pseudographics (only if the English word is guessed).
After the word is successfully guessed, a fireworks animation appears.

<image src="https://raw.githubusercontent.com/pavelbonartsev/githubphotozz/main/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-03-14%20202511.png" width = "1000">
<image src="https://raw.githubusercontent.com/pavelbonartsev/githubphotozz/main/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-03-14%20203052.png" width = "1000">
<image src="https://github.com/pavelbonartsev/githubphotozz/blob/main/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-03-14%20203204.png?raw=true" width = "1000">
