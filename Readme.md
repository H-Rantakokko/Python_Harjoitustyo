Yleinen kuvaus:

Ohjelman tarkoituksena on pyörittää kahta eri peliä (Ristinollaa ja hirttopuuta) ja liikkua alusta loppuun, jos ohjelmiston käyttäjä niin haluaa.
Pelejä voi pelata useampaan kertaan, sillä ristinollassa tilanne alkaa aina alusta ja hirttopuussa arvattavia sanoja on useampia.
Tämä sopii hyvin ajanviettotavaksi vaikkapa jouluna.

Asennnusohjeet:

Voit ladata tietokoneellesi Harjoitustyo kansion ja avata sen Visual Studio Code kautta. 
Ohjelman voi avata myös esimerkiksi jupyter notebookin kautta, jos Visual Studio Codea ei koneella ole.

Miten ohjelma käynnistetään?
Lataa kansio Harjoitustyo ja avaa se esimerkiksi Visual Studio Coden kautta.
Ohjelma käynnistetään avaamalla start.py tiedosto, jonka kautta ohjelma lähtee pyörimään.
Eli Run start.py tiedosto aloittaaksesi pelaamisen.

Käyttöohjeet:

Voit valita alussa haluatko pelata ristinollaa vai hirsipuuta.
Vastaa kysymykseen joko "tic" jolloin pääset pelaamaan ristinollaa tai "hangman" jolloin pääset pelaamaan hirsipuuta.

Ohjeet ristinollan pelaamiseen:

Pelin tavoitteena on saada x tai o kolmen merkin riviin joko viistosti, vaakasuoraan tai pystysuoraan. 
Peli kysyy vuorotellen x ja o pelaajilta mihin merkki laitetaan. (Peliä on mahdollista pelata itseään vastaan tai kaverin kanssa.)
Vastaus on annettava muodossa 1 1 eli välilyönnillä erotettuna, jotta peli lukee vastauksen oikein.
Ensimmäinen annettu luku määrittelee sarakkeen ja toinen rivin. 
Myös toisen vastausten päälle on mahdollista vastata eli vaikka ruudussa olisi o pelaaja x voi korvata merkin omallaan.
Ennen pelaamista onkin hyvä sopia kaverin kanssa, halutaanko mahdollistaa toisen paikan "varastaminen".
Jos pelaaja saa 3 merkkiä peräkkäin hän voittaa, jos koko ruutu täytetään ennen kuin kumpikaan saa 3 merkkiä peräkkäin kyseessä on tasapeli.

Ohjeet hirsipuun pelaamiseen:

Hirsipuussa sinun pitää arvata sana ennen kuin hirsipuu ehditään rakentamaan loppuun asti. 
Tässä pelissä kone arpoo sinulle arvattavan sanan listasta, joten voit pelata peliä useamman kerran. 
Voit arvata jokaisella vuorolla yhden kirjaimen (Kirjoita kirjain pienellä!). Näet sanan pituuden _ merkeistä. 
Sanat ovat englanniksi ja pelissä on käytettävä englantilaisia aakkosia.

Miten voin pelata uudelleen?
Pelin lopussa voit valita joko "yes" tai "no".
Jos valitset "yes" pääset takaisin aloitussivulle ja voit valita pelaatko ristinollaa vai hirsipuuta.
Jos valitset "no" peli loppuu. 

Hauskoja pelihetkiä!

Koodin tekemiseen käytetyt lähteet:
Ristinollan teossa käytetty apuna https://geekflare.com/tic-tac-toe-python-code/
ja hirttopuun teossa apuna käytetty https://inventwithpython.com/invent4thed/chapter8.html
