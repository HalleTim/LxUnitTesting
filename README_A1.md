# Grundlagen Unittests
In der Datei [calculator.py](./CodeToTest/calculator.py) findest du einige Grundlegende Methoden für die Erstellung eines Taschenrechners. Beginne anhand der nachfolgenden Aufgaben diese zunächst auf ihre Funktionalität hin zu testen und im Anschluss die bestehende  Methoden zu erweitern und weitere Testfälle zu erstellen. 

Aufgabe 1
---------
Implementiere mindestens drei Testmethoden in der Datei [test_calculator.py](./test/test_calculator.py) für die Funktion add mit unterschiedlichen Eingabewerten (z. B. positive Zahlen, negative Zahlen, Null). Passe ggf. den Code für einen erfolgreichen Test an!

Aufgabe 2
---------
Implementiere mindestens drei Testmethoden in der Datei [test_calculator.py](./test/test_calculator.py) für die Funktion subtract mit unterschiedlichen Eingabewerten.
Führe die Tests aus und stelle sicher, dass alle Tests erfolgreich sind.

Aufgabe 3
---------
Ergänze [calculator.py](./CodeToTest/calculator.py) um Funktionen für das Multplizieren und Dividieren von zwei Parametern.

Aufgabe 4
---------
Schreibe Tests, welche mindestens nachfolgende Edge Cases abdecken:
- [ ] Multiplikation mit Nullwerten
- [ ] Division von Nullwerten
- [ ] Division durch Eins
- [ ] Division durch 0
- [ ] Multiplikation mit unendlich

Aufgabe 5
---------
Erweitere den Testcase der Division durch Null so, dass ein ZeroDivisionError erwartet wird. (Hinweis: assertRaises)

Aufgabe 6
---------
Erstelle einen Pull Request in den main Branche und versuche die Ergebnisse zusammenzuführen.
