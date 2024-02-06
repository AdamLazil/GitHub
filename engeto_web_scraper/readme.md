## Election Scraper

Finální pro peojekt v Engeto akademii

## Popis projektu

Cílem je vytvořit script který automaticky stáhne volební data z roku 2017 pro zvolený okres a uloží je do .csv souboru

## Instalace knihoven

Instalované knihovny jsou uloženy v souboru requirements.txt

## Spuštění scriptu

Script se spouští s příkazového řádku zadáním dvou argumentů, a to odkazu a názvu výstupního souboru.
Ukázka: E:\PROGRAMOVÁNÍ\Python\engeto_web_scraper> python web_scrapper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7204" "Zlin_data.csv"

# Ukázka projektu

E:\PROGRAMOVÁNÍ\Python\engeto_web_scraper> python web_scrapper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7204" "Zlin_data.csv"
Downloading the data from https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7204
Downloading the data from https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=13&xobec=588318&xvyber=7204
Downloading the data from https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=13&xobec=588318&xvyber=7204
Downloading the data from https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=13&xobec=585076&xvyber=7204
Downloading the data from https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=13&xobec=557102&xvyber=7204
Downloading the data from https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=13&xobec=585092&xvyber=7204
Downloading the data from https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=13&xobec=585106&xvyber=7204
........
Data saved in to the file: Zlin_data.csv
Process completed: web_scrapper.py

částečný výstup:
K�d obce,N�zev obce,Voli�i v seznamu,Vydan� ob�lky,Platn� hlasy,Ob�ansk� demokratick� strana,��d n�roda - Vlasteneck� unie,CESTA ODPOV�DN� SPOLE�NOSTI,�esk� str.soci�ln� demokrat.,Radostn� �esko,STAROSTOV� A NEZ�VISL�,Komunistick� str.�ech a Moravy,Strana zelen�ch,"ROZUMN�-stop migraci,dikt�t.EU",Strana svobodn�ch ob�an�,Blok proti islam.-Obran.domova,Ob�ansk� demokratick� aliance,�esk� pir�tsk� strana,Referendum o Evropsk� unii,TOP 09,ANO 2011,Dobr� volba 2016,SPR-Republ.str.�sl. M.Sl�dka,K�es�.demokr.unie-�s.str.lid.,REALIST�,SPORTOVCI,D�lnic.str.soci�ln� spravedl.,Svob.a p�.dem.-T.Okamura (SPD),Strana Pr�v Ob�an�
588318,B�lov,257,174,174,25,0,0,8,0,14,20,1,0,2,0,0,14,0,6,51,0,0,9,4,0,0,20,0
585076,Biskupice,564,314,314,17,1,0,16,0,15,34,2,6,15,0,0,16,0,1,102,0,1,38,2,0,2,42,4
557102,Bohuslavice nad Vl���,315,201,201,19,1,0,24,1,8,13,2,3,1,1,0,16,0,2,65,1,0,22,0,0,3,18,1
