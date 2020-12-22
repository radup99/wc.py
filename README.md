# wc.py
WC - Proiect categoria C, ID 12

Instructiuni:

Se executa fisierul wc.py, adaugand ca argumente in linia de comanda optiunile dorite si numele fisierelor. Daca nu sunt specificate optiuni, va afisa implicit numarul de 
caractere newline, cuvinte si bytes ale fisierelor cerute. Daca nu sunt date fisiere ca argumente, se va citi de la tastatura un text pana la citirea caracterului EOF.

Exemplu:
- python wc.py -c -l fisier1.txt fisier2.txt

Optiuni:
- -c, --bytes: afiseaza numarul de bytes;
- -m, --chars: afiseaza numarul de caractere;
- -l, --lines: afiseaza numarul de caractere newline existente;
- --files0-from=F: selecteaza numele fisierelor scrise in fisierul F
- -L, --max-line-length: afiseaza lungimea maxima a liniilor
- -w, --words: afiseaza numarul de cuvinte;
