"""
#PALINDROMY I #ANAGRAMY
Napisz program, który prosi użytkownika o podanie dowolnego napisu. Następnie program wyświetla na ekranie to słowo wspak (od prawej do lewej) 
i wyświetla komunikat czy to wyrażenie jest palindromem (czyli czytane wspak daje do samo wyrażenie np. “ala”, “Kobyła ma mały bok”
 (inne przykłady: http://www.palindromy.pl/pal_kr.php). Podczas sprawdzania ignoruj wielkość liter oraz znaki 
 niebędące literami. Następnie wywołaj dowolną stronę internetową, 
 która pokaże anagramy oraz słowa utworzone po usunięciu liter, np. https://poocoo.pl/scrabble-slowa-z-liter/hardcoder 
Propozycja rozszerzenia: samodzielnie wyszukaj anagramy i słowa utworzone po usunięciu liter z podanego słowa, 
na przykład wykorzystując słownik wspomniany na stronie https://anagramy.wybornie.com/ 
Kody / pytania / wątpliwości / wszystkie inne miłe rzeczy można wrzucać w komentarzach! 🙂
"""
import webbrowser

def check_palindrom(word):
    word_2 = ''.join(word)[::-1]
    print(word_2)
    if word == word_2:
        return True
    else:
        return False

input_word = input("Enter your word or phrase to check if palindrome: ")
word_only_letters = "".join([ i.lower() for i in input_word if i.isalnum()])
is_palindrom = check_palindrom(word_only_letters)
print(is_palindrom)
webbrowser.open(f'https://poocoo.pl/scrabble-slowa-z-liter/{word_only_letters}')


