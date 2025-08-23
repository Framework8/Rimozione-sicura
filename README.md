# Rimozione Sicura

Questo progetto consiste in un sistema per eliminare in modo sicuro file su supporti di tipo HDD e SSD.

## Funzionalità principali

- selezione dei file tramite input da utente  
- spostamento dei file selezionati in una cartella temporanea grazie a `shutil.move()`  
- crittatura del/i file indicato/i  
- sovrascrittura del/i file 3 volte prima dell'eliminazione  

## Prerequisiti

- Python3 installato sul sistema  
- Librerie `cryptography` e `colorama` indicate nel file `requirements.txt`  
- g++ per compilare le parti in c++ in modo adatto per la propria macchia
- ⚠️ **<u>Il sistema di gestione dei percorsi nei file Python è pensato per filesystem Unix/Linux/macOS</u>**

## Installazione e utilizzo

- clonare la repository  
  ```bash
  git clone https://github.com/Framework8/Rimozione-sicura.git
  ```
- entrare nella cartella del progetto  
  ```bash
  cd Rimozione-sicura
  ```
- installare le dipendenze  
  ```bash
  pip install -r requirements.txt
  ```
- compilare le parti in c++  
  ```bash
  g++ elimina_file.cpp -o elimina_file
  g++ elimina_cartella.cpp -o elimina_cartella
  ```
- eseguire lo script python  
  ```bash
  python3 starter.py
  ```

## Sicurezza

- la chiave usata per crittare i file è casuale e cambia ad ogni crittatura grazie al richiamo alla funzione `chiave()` ogni volta che si esegue una crittatura dei dati.  
  <img width="233" height="83" alt="immagine" src="https://github.com/user-attachments/assets/d9cc5c23-5600-4b12-8888-39dfcbb6f8ac" />  

- se si vuole aumentare il numero di sovrascritture dei file lo si può fare modificando la funzione `void sovrascriviFileConDatiCasuali` all'inizio di entrambi i file cambiando `int passaggi = 3` con `int passaggi = (numero deiderato di passaggi)`.  
  <img width="634" height="48" alt="immagine" src="https://github.com/user-attachments/assets/29e60939-79d3-413a-8d8a-f5d67e93c1ff" />  

- sui supporti HDD è garantita una sicurezza quasi totale mentre sui dispositivi SSD il wear leveling può lasciare copie nascoste dei settori vecchi quindi non c'è certezza matematica che non rimanga nulla. Detto ciò il meccanismo di scrittatura con Fernet (AES) + sovrascrittura dei file il livello di protezione è molto alto dato che in caso si trovino tracce sarebbero crittate senza possibilità di risalire alla chiave.  
