# Ohjelmistotuotannon miniprojekti - Lukuvinkkisovellus
Sovelluksen avulla käyttäjä voi selata omia ja muiden käyttäjien lisäämiä lukuvinkkejä.
## Käyttöohje
### PostgreSQL-tietokannan asennus
Sovellus toimii tällä hetkellä vain paikallisesti käyttäjän omalla koneella. Käyttääksesi sovellusta on sinulla oltava asennettuna PostgreSQL-tietokanta. Voit asentaa PostgreSQL:n esimerkiksi [Tietokantasovellus-kurssin ohjeen](https://hy-tsoha.github.io/materiaali/osa-2/#tietokannan-k%C3%A4ytt%C3%A4minen) tai PostgreSQL:n omilta sivuilta löytyvien [ohjeiden](https://www.postgresql.org/download/) avulla.

### Sovelluksen käyttöönotto
Kun olet asentanut PostgreSQL:n, saat sovelluksen käyttöön seuraavilla ohjeilla:
1. Asenna sovelluksen tarvitsemat riippuvuudet syöttämällä sovelluksen juurihakemistossa komento `poetry install`.
2. Luo sovelluksen juurihakemistoon tiedosto `.env` ja kopioi sen sisällöksi
```
DATABASE_URL=postgresql://<user>
SECRET_KEY=
```
3. Korvaa tietokannan osoitteessa `<user>` omalla käyttäjänimelläsi. Ennen sitä kannattaa kokeilla, että saat tietokantaan yhteyden syöttämällä komennon `psql <database_url>`, missä `<database_url>` on edellä mainitun mukainen (eli muotoa `postgresql://...`).
4. Anna kohdan `SECRET_KEY` arvoksi jokin satunnainen n. 16 kirjaimen ja numeron yhdistelmä.
5. Alusta sovelluksen tietokanta komennolla
```
poetry run python3 src/initialize_database.py
```
7. Nyt voit käynnistää sovelluksen komennolla
```
poetry run python3 src/index.py
```

