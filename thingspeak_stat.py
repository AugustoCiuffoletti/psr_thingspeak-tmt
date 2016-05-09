import time;
import httplib, urllib #librerie per il protocollo HTTP
import psutil          #libreria per monitorare la macchina.
while True:
    body = urllib.urlencode (
      { "field1": psutil.cpu_percent(),                  # percentuale cpu occupata
        "field2": psutil.virtual_memory().percent,       # memoria usata
        "field3": psutil.net_io_counters().packets_sent, # pacchetti inviati
        "field4": psutil.net_io_counters().packets_recv, # pacchetti ricevuti
        "key":"copia qui la write key"}                        # WRITE KEY
        )
    print body
    headers = {
      "Content-type": "application/x-www-form-urlencoded"
      } 
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", body, headers)
        conn.close()
    except:
        print "Connessione fallita: dato non registrato." 
    time.sleep(60) 
