# ## Zapoznaj się z prostymi typami zmiennych
# # print('Hello world') # fun print wyświetla wynik
# # name_of_car = 'mercedes'  # zmienna name_of_car jest typu string
# # print(name_of_car)
# # print('Lubię samochód marki mercedes a moja rodzina też lubi samochód marki: mercedes')
# # ############Przyklad 1
# # a = 2  # zmienna a ma typ integer (liczba całkowita)
# # b = 7.345134   # zmienna b typ float (liczba zmiennoprzecinkowa)
# # c = a + b
# # # d = b ** a  # ** to operator potęgowania  b^a
# # # print(a)
# # # print(b)
# # print(c)
# # # print(d)
# # # print(type(b)) # fun type sprawdza typ zmiennej
# # # # print("#####################")
# # z = 'Ala'
# # x = "ma"
# # y = "koty"
# # zdanie = y + x + z
# # print(zdanie)
# # #print(y,x,z)
# # # X = 2
# # # Y = '2'
# # print("Zmienna X ma typ: ",type(X))
# # print("Zmienna Y ma typ: ",type(Y))
# # print(z,"ma kotów: ",str(X))
# # print(z,"ma kotów: ",Y)
# # print(X+Y)
# # print("#####################")
# # zm1 = input("Podaj zmienną x =") # fun input służy do wprowadzania wartości przez uzytkownika w konsoli
# # zm2 = input("Podaj zmienną y =") # wynik funkcji (argument wyjściowy funkcji) input ma typ string
# # c = zm1 + zm2  # konwersję zmiennej string na  float
# # print(c)

# # zm1 = input("Podaj zmienną x =") # fun imput służy do wprowadzania wartości przez uzytkownika w konsoli
# # zm2 = input("Podaj zmienną y =") # wynik funkcji (argument wyjściowy funkcji) input ma typ string
# # c = float(zm1) + float(zm2)  # konwersję zmiennej string na  float
# # print(c)
# #print("#####################")

# # usun = input("Podaj zmienną ktorą chcesz usunąć z pamięci: ")
# # del(usun)

# # print("#####################")
# # ###########Zmienne logiczne ###############
# # a = True
# # b = False # zmienna b typ logiczny bool
# # print(type(a))
# # x = '1'
# # y = 1
# # print(x == y)   # operator ==  oznacza czy x równe y?
# # print(x != y)   # operator !=  oznacza czy x różny od y?
# # a = 3
# # b = 5
# # print(a < b)
# # print(a >= b)

# ##############Zadania do wykonania, Twoje pierwsze algorytmy

# # 1. Wykonaj odejmowanie, mnożenie i dzielenie 2 dowolnych liczb


# # x = float(input( 'Podaj x= ') )
# # y = float(input( 'Podaj y= ') )
# # różnica = x-y
# # print('różnica to', różnica)

# # x = float(input('Podaj x= '))
# # y = float(input('Podaj y= '))
# # iloraz = x/y
# # print('iloraz to', iloraz)


# # x = float(input('Podaj x= '))
# # y = float(input('Podaj y= '))
# # iloczyn = x*y
# # print('iloczyn to', iloczyn)



# # 2. Oblicz wyrażenie 2x+5y   gdzie: x,y to dowolne dwie liczby które podaje użytkownik (w konsoli)

# # x = float(input('Podaj x= '))
# # y = float(input('Podaj y= '))
# # wynik = 2*x+5*y
# # print('wynik wyrażenia to', wynik)

# # 3. Popraw zmienną zdanie tak aby wyświetlany był napis: "Ala ma kota"
# # z = 'Ala '
# # x = "ma "
# # y = "kota"
# # zdanie = z + x + y
# # print(zdanie)

# # 4. Wyświetl zdanie "Jestem a b mam c lat studiuję d",
# #  gdzie : a-imie, a-nazwisko, c-liczba, d-kierunek studiów są dowolne zmienne które podaje użytkownik (wczytywane z klawiatury)

# # a = input('Podaj imię:')
# # b = input('Podaj nazwisko:')
# # c = input( 'Podaj wiek:')
# # d = input('Podaj kierunek studiów:')
# # zdanie = f'Jestem {a} {b}, mam {c} lat i studiuję {d}'
# # print(zdanie)


# # 5. Sprawdź czy 1+2+10+20000001+4+347586970885 jest równa 321784560456434534646

# # if 1 + 2 + 10 + 20000001 + 4 + 347586970885 == 321784560456434534646:
# #     print("Wynik jest poprawny.")
# # else:
# #     print("Wynik jest niepoprawny.")

# # # 6. Sprawdź czy suma dowolnych dwóch liczb podanych przez użytkownika jest liczbą parzystą czy nieparzystą wyświetl właściwy komunikat

# # a = float(input('Podaj dowolną liczbę:'))
# # b = float(input('Podaj dowolną liczbę:'))

# # suma = a + b
# # if suma % 2 == 0:
# #     print(f"Suma {a} i {b} jest liczbą parzystą.")
# # else:
# #   print(f"Suma {a} i {b} jest liczbą nieparzystą.")


# # # 7. Utwórz prosty kalkulator dla 2 zmiennych podanych przez użytkownika, który obliczy: sumę, różnicę,# iloczyn, iloraz, potęgę tych liczb, nie zapo mnij o stosownych komentarzach informacyjnych dla użytkownika.

# # #    #najpierw prosimy o liczby
# # x = float(input('Podaj pierwszą liczbę:'))
# # y = float(input('Podaj drugą liczbę:'))

# # # #wyliczamy,określamy różnicę i sumę, iloczyn, iloraz, potege
# # suma = x + y
# # różnica = x - y


# #komunikat#

# # if y != 0:
# #   iloraz = x / y
# # else:
# #   iloraz = 'Nie dzielimy przez zero :)'
  
# # iloczyn = x * y
# # potęga = x ** y

# # # #wyniki
# # print(f"Suma {x} i {y} wynosi: {suma}")
# # print(f"Różnica {x} i {y} wynosi: {różnica}")
# # print(f"Iloczyn {x} i {y} wynosi: {iloczyn}")
# # print(f"Iloraz {x} i {y} wynosi: {iloraz}")
# # print(f"{x} do potęgi {y} wynosi: {potęga}")


# # 8. Oblicz wyrażenie: a = 3z-|2cos(x)sin(y)|, gdzie: x,y,z - dowolne liczby     (|x| to moduł z liczby z, użyj funkcji abs())
# # import math 
# # a= math.sin(30)
# # print(a)



# # 9. Wykonaj mini ankietę tj. poproś użytkownika o następujące informacje: imie, nazwisko, wiek, zadaj mu pytania: "Czy zdrowo się odżywiasz?",
# # , "Czy lubisz sport?" i dodatkowo 3 inne własne. Po uzyskaniu wszystkich odpowiedzi wyświetl ich podsumowanie.


# # #info
# # imie = input("Podaj swoje imię: ")
# # nazwisko = input("Podaj swoje nazwisko: ")
# # wiek = input("Podaj swój wiek: ")
# # zdrowie = input("Czy zdrowo się odżywiasz? (tak/nie): ")
# # sport = input("Czy lubisz sport? (tak/nie): ")
# # środowisko = input("Czy troszczysz się o środowisko? tak/nie")
# # mięso = input("Czy jesz mięso? tak/nie ")
# # zwierzę = input("Czy troszczysz się o zwierzęta? tak/nie")

# # podsumowanie
# # print(f"\nPodsumowanie ankiety:\nImię: {imie}\nNazwisko: {nazwisko}\nWiek: {wiek}\nZdrowie: {zdrowie}\nSport: {sport}\nŚrodowisko: {środowisko}\nMięso: {mięso}\nZwierzę: {zwierzę}")

# # 10. Twoim zadaniem jest przygotowanie uniwersalnego i profesjonalnego życiorysu, złożonego z 10-ciu zdań, które wyświetlisz na ekranie
# # # Użytkownik wpisuje tylko swoje imie, nazwisko, wiek, zawód, miejsce urodzenia, zainteresowania i ... życiorys jest gotowy.

# # imie = input("Podaj swoje imię: ")
# # nazwisko = input("Podaj swoje nazwisko: ")
# # wiek = input("Podaj swój wiek: ")
# # miejsce_urodzenia = input("Podaj miejsce swojego urodzenia: ")
# # wykształcenie =  input("Podaj swoje wykształcenie(wyższe, średnie, podstawowe): ")
# # zawod = input("Podaj swój zawód: ")
# # zainteresowania = input("Podaj swoje zainteresowania: ")
# # lubienie = input('Podaj 2 rzeczy, które bardzo lubisz:')
# # cechy = input("Podaj swoje 3 ważne cechy (w bezokoliczniku): ")
# # życie = input('Dokończ zdanie: Moje życie jest...:')

# # życiorys = f" Jestem {imie} {nazwisko}. Mam {wiek} lat. Urodziłam/em się w {miejsce_urodzenia}.Posiadam wykształcenie {wykształcenie}. Z zawodu jestem {zawod}.Interesuje mnie {zainteresowania}. Coś co bardzo też lubię to {lubienie}. Moimi ważnymi cechami charakteru są {cechy}. Moje życie jest {życie}."
# # print(życiorys) 

# # 11. Przygotuj dla dziecka, które uczy się czytać zestaw sylab do nauki, ale zrób to inteligentnie tj.
# # dziecko wpisuje na klawiaturze 1 spółgłoskę a Ty dodajesz do niej odpowiednie samogłoski i wyświetlasz całość na ekranie

# spolgloska = input("Podaj jedną spółgłoskę: ")

# samogloski = ['a', 'e', 'i', 'o', 'u', 'y']

# sylaby = [spolgloska + sam for sam in samogloski]

# print("Oto sylaby o:")
# print(sylaby)
# #12. Sprawdz wynik działań
# # 0 > 1
# # 0 <= 1
# # 0 >= 1
# # 1 == 0
# # 1 == 1
# # 1 != 0
# # 1 != 1
# #(x > 1 and x < 13) and x != 5  , dla x = 2
# # 13. Użytkownik podaje imie, sprawdź czy to imie to Janusz lub Grażyna
# # imie = input("Podaj swoje imię: ")

# # if imie.lower() == "janusz":
# #     print("Witaj Januszu!")
# # elif imie.lower() == "grażyna":
# #     print("Witaj Grażyno!")
# # else:
# #     print("Witaj! Cieszymy się, że jesteś z nami.")
# #print("#####################")