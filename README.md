# Progetto Santoro Matteo

## Matricola 881608

![](/img/grafico.png)

# Come ho lavorato
Ho pensato di svolgere la prima traccia cercando di simulare il comportamento di un device che raccoglie informazioni durante la giornata e poi le invia producendo dei dati "randomici"
Ho utlizzato alcune librerie per poter simulare questi device, **datetime** per poter lavorare comodamente con le date e gli orari ai quali i dati vengono raccolti ed inviati quindi **timedelta**  per poter comodamente trascorrere giornate, **schedule** per poter inviare periodicamente i dati, io ho impostato come periodo alcuni secondi per testare il funzionamento dell'elaborato ma la libreria **schedule** permette di compiere una routine ogni giorno ad un orario specifico, ogni settimana e cosi' via

``pip install schedule``

# Test 

> per testare `python3 RunMe.py` oppure `./RunMe.py`

# IOTdevice 
IOTdevice.py e' una classe che modella un device generico, contente metodi utili a quest'ulitmi

`toString`

Classico metodo con il quale si puo' stampare ogni informazione sul device 

`connect` 

Attraverso il quale il device si connette al gateway e con un messaggio creato dal toString che contiente tutti i dati 

`init`

Con cui si inizializza, quando il device si accende legge ora e data, un nome e dati inziali

`updateData` 

Simula il passare di 24 ore e produce dati randomici entro standard reali  

`autentication`

Simile al toString pero utilizzato dal cloudServer per ottenere un output con le sole informazioni utlili e stamparle in console

# gateway

Il gateway riceve una volta al giorno i dati tramite una connessione UDP dai device, all' interno del ciclo pero' prima di poter trasmettere al successivo aspetta di ricevere idati da tutti e quattro i device, cosi da poter effettuare una sola trasmissione TCP

# cloudServer 

il cloud si occupa di ricevere i dati che sono stati trasmessi al gateway, utilizza un metodo della classe IOTdevice per poter formattare e stamapare in console i rilevamenti con i rispettivi orari e ip di provenienza e calcola il tempo di viaggio dei dati grazie a Datetime

> Sia gateway che cloudServer hanno una variabile DEBUG che puo tornare utile per poter verificarne il funzionamento, nello sviluppo le ho usate e ridotte nella consegna 

# RunMe 

Il file python RunMe va eseguito per poter comodamente far partire i vari device e server, hoscelto di usare i vari file Device*.py per poter simulare i singoli device, e per poi poter disattivare tutto comodamente ho preso i pid dei processi e li termino con il comando kill altrimenti i processi sarebbero rimasti attivi in background 
