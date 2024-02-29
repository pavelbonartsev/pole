ОПИСАНИЕ НА РУССКОМ

В данном репозитории находится код консольной игры "Поле чудес".  Суть игры - как можно раньше угадать, какое слово зашифровано, по сути классическая версия "Поля чудес", но возможно, в следующих версиях будут какие-то авторские дополнения. Программа написана полностью на языке Python. Чтобы запустить игру, просто скачайте сам файл и запустите его (условие: наличие Python IDLE на вашем устройстве) или скопируйте содержимое файла и вставьте его в какой-либо файл формата .py на своем устройстве и запустите (опять же, Python IDLE также должен быть установлен). Чтобы начать работать со словом, предложенным программой, вам следует попробовать угадать букву угадываемого слова и ввести ее в консоль (игра к регистру ввода букв нечувствительна), используя буквы алфавита того языка, словом которого является текущее угадываемое слово. Если же вы хотите попробовать ввести все слово целиком, вводите его целиком, вместо того, чтобы угадывать букву слова. Программа отличит ввод слова от ввода буквы и в случае совпадения текущего угадываемого слова с пользовательским вариантом ввода слова без учета регистра поздравит Вас с победой. Вы можете воспользоваться командами, которые позволяют узнать какие-либо данные о игровом процессе или сменить условия игрового процесса. Каждая из них начинается знаком "/". Программа отличит ввод команды от ввода буквы либо слова. Полный перечень команд:
/cm (сокращение change mode) - сменить игровой режим с более визуализированного на упрощенный 
либо с более визуалированного на упрощенный.
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
/help - вывод данного перечня команд и правил игры. По умолчанию выводится в начале выполнения программы.

ОПИСАНИЕ НА АНГЛИЙСКОМ

This repository contains the code of the console game "Field of Wonders". The essence of the game is to guess which word is encrypted as early as possible, in fact the classic version of the "Field of Miracles", but perhaps in future versions there will be some author's additions. The program is written entirely in Python. To start the game, simply download the file itself and run it (condition: Python IDLE on your device) or copy the contents of the file and paste it into some format file.py on your device and run (again, Python IDLE should also be installed). To start working with the word suggested by the program, you should try to guess the letter of the guessed word and enter it into the console (the game is case insensitive to letter input) using the letters of the alphabet of the language whose word is the current guessed word. If you want to try to enter the whole word, enter it in its entirety, instead of guessing the letter of the word. The program will distinguish the input of a word from the input of a letter and, if the current guessed word matches the user's case-insensitive word input option, it will congratulate you on your victory. You can use commands that allow you to find out any information about the gameplay or change the conditions of the gameplay. Each of them begins with a "/" sign. The program will distinguish the input of a command from the input of a letter or word. The full list of commands:
/cm (abbreviation change mode) - change the game mode from a more visualized to a simplified one 
or from a more visualized to a simplified one.
/used - letters of the Russian or English alphabet used during the period of guessing this word
(depending on which language word is the current guessed word).
/rest - those letters of the Russian or English alphabet
(depending on which language word is the current word being guessed),
which have not yet been used in guessing this word.
Russian Russian /cl (abbreviation change language) - change the language, the words of which will be
the words that will be offered for guessing after successfully guessing
the current word (the language of the words changes either from Russian to English or from English
to Russian).
PLEASE NOTE: when using this command, the language of the words offered
for guessing will change, the language of the program interface is always Russian.
/help - output of this list of commands and rules of the game. By default, it is displayed at the beginning of the program execution.
