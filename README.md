# LedMatrixPannel
Image management of an ArcadeMarquee

In giro di cabinari Arcade se ne vedono tanti, di modificati o costruiti da zero, ma una delle caratteristiche più interessanti è il "Marquee" digitale.
Per coloro che non sanno cos'è un "marquee", è l'ampia finestra rettangolare che si trova nella parte superiore di un cabinato arcade che di solito mostra il nome del gioco a cui stai giocando. I cabinati Mame a volte mostrano semplicemente MAME o qualcosa  che generalmente dice "Arcade" e non sono digitali.
Quando abbiamo iniziato a costruire il nostro cabinato volevamo un marquee digitale e di farlo cambiare dinamicamente per ogni gioco.
Le opzioni in rete ne sono tante, alcune più complicate e costose altre troppo semplici.
Nella ricerca ci siamo imbattuti nei Led Marquee della Pixelcade e ce ne siamo innamorati.
Volendo preplicarli abbiamo trovato i pannelli led-matrix dell'Adafruit che facevano proprio al caso nostro in quanto, oltre ad avere un aspetto retrò, questi display sono modulari e possono adattarsi a quasi qualsiasi cosa.
Abbiamo quindi preso due pannelli da 63x32 e un rasperry pi3.
Fin qui tutto semplice.
Il problema nasce dopo, dovendo fare comunicare i due raspberry, ovvero il raspberry su cui gira Retropie con il raspberry che gestisce il marquee.
Ho scritto quindi questo programma che gestisce i due pannelli led.
Questo programma va a leggere su un file di testo, che crea Retropie, sul quale è indicato quale gioco è avviato e su che tipo di macchina.
Una volta letto il file va a ricercare il file png associato al gioco, se c'è lo riproduce, altrimenti riproduce quello della macchina virtuale. Se anche questa non c'è allora riproduce la schermata principale di default.


