# Čtenářský deník

## Flask, SQLAlchemy

Aplikace slouží k evidenci přečtených knih. Můžeme v ní evidovat nově přečtené knihy, upravovat nebo mazat již zaevidované knihy.

Aplikace obsahuje úvodní stranu (soubor index.html) s rozcestníkem.
Prostřednictvím formuláře (v souboru new_book.html) zadáme novou knihu. Je zapotřebí vyplnit autora, název, stručný obsah, počet stran a ISBN (pokud jej kniha má).
Zadaná kniha se pak uloží do databáze (books.db).
Z databáze pak uložené knihy zobrazujeme (v souboru books.html). Můžeme je odtud také smazat nebo upravit (v tom případě se proklikneme do editačního formuláře v souboru edit.html).
V celé aplikaci se nachází v horní části navigační menu pro vstup do požadované sekce.

