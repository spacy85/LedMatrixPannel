# LedMatrixPannel
Image management of an ArcadeMarquee

In giro di cabinati Arcade se ne vedono tanti, di modificati o costruiti da zero, ma una delle caratteristiche più interessanti è il "Marquee" digitale.
Per coloro che non sanno cos'è un "marquee", è l'ampia finestra rettangolare che si trova nella parte superiore di un cabinato arcade che di solito mostra il nome del gioco a cui stai giocando. I cabinati Mame a volte mostrano semplicemente MAME o qualcosa  che generalmente dice "Arcade" e non sono digitali.
Quando abbiamo iniziato a costruire il nostro cabinato volevamo un marquee digitale e di farlo cambiare dinamicamente per ogni gioco.
Le opzioni in rete ne sono tante, alcune più complicate e costose altre troppo semplici.
Nella ricerca ci siamo imbattuti nei Led Marquee della Pixelcade e ce ne siamo innamorati.
Volendo preplicarli abbiamo trovato i pannelli led-matrix dell'Adafruit che facevano proprio al caso nostro in quanto, oltre ad avere un aspetto retrò, questi display sono modulari e possono adattarsi a quasi qualsiasi cosa.
Abbiamo quindi preso due pannelli da 63x32 e un Rasperry Pi3.

![20191002_192631](https://user-images.githubusercontent.com/57826009/136056518-9ba12d80-026c-43fd-a299-cd2f961cc67a.jpg)

Fin qui tutto semplice.
Ma entriamo nei dettagli.
La nostra macchina arcade gira su Retropie installato su un altro Raspberry Pi3.
Dato che i due Raspberry non sono fisicamente collegati tra loro, l'unico modo per farli comunicare era via rete.
All'intero della cartella Rom di Retropie, viene creato un file di testo che viene condiviso, via samba, con il Raspberry che gestisce il marquee.

_IP=$(hostname -I) || true
if [ "$_IP" ]; then
    printf "My IP address is %s\n" "$_IP"
sudo python3 ./home/pi/rpi-led-matrix/bindings/python/animate.py /home/pi/marquee/start.gif
sudo mount -a
sudo python3 ./home/pi/rpi-led-matrix/bindings/python/so.py &
fi
exit 0


Il programma, so.py, va a leggere il file di testo sul qualke è indicato, ogni volta, quale gioco (rom) ed emulatore(station) è in esecuzione.
Una volta letto la "rom" e la "station", il programma va a ricercare i file png associati ad essi, visualizzando sul pannello prima la rom, se non c0è la station, altrimenti l'immagine di default del cabinato.
Per la gestione del pannello ho utilizzato le seguenti librerie di Hzeller:
https://github.com/hzeller/rpi-rgb-led-matrix

n.b: il file animate.py permette la riproduzione di gif animate.
![IMG_20191211_195437](https://user-images.githubusercontent.com/57826009/136056525-e69dd688-3455-419d-aa2b-361b191004b8.jpg)
![IMG_20200113_190311](https://user-images.githubusercontent.com/57826009/136056526-a5f56118-0aca-4370-a9d5-bc90b2104bb1.jpg)
