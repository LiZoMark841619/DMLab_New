# DMLab_New

# Adatok beszerzése egy publikus forrásból:

Használj egy nyilvánosan elérhető API-t vagy egy könnyen scrape-elhető weboldalt. Gyűjtsd az adatokat egy SQL vagy noSQL adatbázisba, amely jobban illik a kiválasztott adatszerkezethez. Az adatok lehetnek például tőzsdei árak, piactér hirdetések, helyi éttermek ebédmenüi – olyan forrást válassz, ami üzleti szempontból releváns. Tipp: kérlek, ne használj SQLite-ot, mert a megoldásod kiértékelését megnehezíti. Köszönjük.
Adatok feldolgozása: Végezz az adatokon valamilyen hasznos műveletet, ami üzleti értékkel bírhat. Nem szükséges gépi tanulási modellt építened; inkább arra vagyunk kíváncsiak, hogyan elemzed a nyers adatokat és milyen információkat tudsz kinyerni belőlük. Például vizsgálhatod az árváltozásokat, trendeket vagy egy adott termékkategória keresleti ingadozásait.
A megoldás publikálása: A megoldásod tedd lokálisan használhatóvá frontend alkalmazás vagy REST API formájában, ahol az eredmények könnyen hozzáférhetők. A frontend lehet egy egyszerű dashboard vagy interaktív webes felület, míg az API biztosítson lehetőséget a feldolgozott adatok lekérdezésére és az eredmények visszaadására.


# Technikai követelmények:

Programozási nyelv: A feladatot olyan programozási nyelven oldd meg, amelyben komfortosan dolgozol. Tipp: a Python előnyt jelent számunkra.
Architektúra: A megoldás alapja legyen microservice architektúra, amely modularizálja az adatgyűjtési, feldolgozási és publikálási lépéseket.
Kipróbálhatóság: Fontos feltétel, hogy az elkészült kódod lokálisan kipróbálható legyen. Kérjük, biztosítsd, hogy minden szükséges leírás és konfiguráció elérhető legyen a GitHub-on. Tipp: használd a Dockert, hogy a megoldásodat mi is könnyen ki tudjuk próbálni. Ha a feladat megoldása során a deploy-ra már nem jutott időd, akkor a Readme-ben emlékezz meg arról, hogyan is csinálnád azt meg.
Dokumentálás. Kérünk, hogy a munkád alapszinten dokumentáld. Néhány szóban írd le, hogy miért az adott probléma megoldását választottad, miért az adott technológiákkal dolgoztál, a megoldásod főbb részeinek működését.


# Példák lehetséges megoldásokra:

Ebédmenük összegyűjtése és megjelenítése egy adott lokáció környékén: Keresd meg, hogy a helyi éttermek milyen ebédmenüket kínálnak, és jelenítsd meg egy felületen a napi kínálatot.
Tőzsdei (energia-, részvény- vagy nyersanyag-) árak elemzése: API segítségével gyűjts adatokat egy adott tőzsdei termékről, és mutasd meg az árváltozások trendjeit.
Piactérárak követése: Egy adott termékkategóriában (pl. ingatlanok, használt autók) figyeld meg a hirdetési árak alakulását. Ez segíthet megérteni az ármozgások trendjeit az adott termékcsoportban.
Sportesemények statisztikáinak gyűjtése és elemzése: Gyűjts adatokat egy népszerű sportágról, és mutasd be, hogyan alakulnak a csapatok vagy játékosok statisztikái.
Időjárás-előrejelzés és tényadatok elemzése és megjelenítése: Gyűjts időjárás előrejelzési és tény adatokat és jelenítsd meg azokat vizuálisan, akár egy városra koncentrálva.
