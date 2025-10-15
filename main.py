import requests
from bs4 import BeautifulSoup
from collections import deque
from urllib.parse import urljoin

# Intestazione per simulare un browser reale
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# --- FUNZIONI DI SUPPORTO (invariate) ---

def is_valid_wiki_link(href):
    """Controlla se un link è un articolo standard di Wikipedia, escludendo pagine speciali."""
    if not href or not href.startswith('/wiki/'):
        return False
    if '#' in href:
        return False
    excluded_prefixes = [
        '/wiki/Speciale:', '/wiki/Aiuto:', '/wiki/File:', '/wiki/Categoria:',
        '/wiki/Portale:', '/wiki/Template:', '/wiki/Discussione:', '/wiki/Progetto:'
    ]
    for prefix in excluded_prefixes:
        if href.startswith(prefix):
            return False
    return True

def get_page_title(soup):
    """Estrae il titolo H1 principale da una pagina BeautifulSoup."""
    title_tag = soup.find('h1', id='firstHeading')
    return title_tag.text.strip() if title_tag else "Titolo non trovato"

# --- FUNZIONE PRINCIPALE DELLO SPIDER (aggiornata per tracciare il percorso) ---

def find_path_to_page(start_url, destination_title, limit=500):
    """
    Cerca una pagina di destinazione e restituisce il percorso di link per arrivarci.
    """
    # MODIFICA: La coda ora contiene tuple (URL, percorso_fatto)
    # Il percorso è una lista di URL che ci ha portato a quello corrente.
    queue = deque([(start_url, [start_url])]) 
    visited_urls = {start_url}
    pages_visited_count = 0

    print(f"🏁 Inizio la ricerca dalla pagina: {start_url}")
    print(f"🎯 Destinazione da trovare: '{destination_title}'\n")

    while queue and pages_visited_count < limit:
        # MODIFICA: Estraiamo sia l'URL che il suo percorso
        current_url, path = queue.popleft()
        pages_visited_count += 1

        print(f"[{pages_visited_count}/{limit}] Visito: {current_url}")

        try:
            response = requests.get(current_url, headers=HEADERS, timeout=5)
            if response.status_code != 200:
                continue
            
            soup = BeautifulSoup(response.text, 'html.parser')
            current_title = get_page_title(soup)
            
            normalized_destination = destination_title.lower().replace('_', ' ')
            if normalized_destination in current_title.lower():
                print(f"\n🎉🎉🎉 Destinazione trovata! 🎉🎉🎉")
                # MODIFICA: Restituiamo l'intero percorso trovato
                return path

            content_div = soup.find('div', id='mw-content-text')
            if not content_div:
                continue

            for link_tag in content_div.find_all('a', href=True):
                href = link_tag['href']
                if is_valid_wiki_link(href):
                    absolute_url = urljoin('https://it.wikipedia.org', href)
                    if absolute_url not in visited_urls:
                        visited_urls.add(absolute_url)
                        # MODIFICA: Creiamo il nuovo percorso e lo aggiungiamo alla coda
                        new_path = path + [absolute_url]
                        queue.append((absolute_url, new_path))

        except requests.RequestException:
            continue

    print(f"\n❌ Ricerca terminata dopo {pages_visited_count} pagine. Destinazione non trovata.")
    return None

# --- ESECUZIONE DEL PROGRAMMA (aggiornata per stampare il percorso) ---

if __name__ == "__main__":
    start_page = input("Inserisci l'URL di partenza di Wikipedia: ")
    destination_page_title = input("Inserisci il titolo della pagina di destinazione: ")
    
    print("-" * 40)
    # MODIFICA: La funzione ora restituisce una lista (il percorso) o None
    found_path = find_path_to_page(start_page, destination_page_title)
    
    if found_path:
        print("\nPercorso trovato attraverso i seguenti link:")
        # Stampa il percorso in modo leggibile, con frecce
        print(" -> ".join([url.split('/')[-1] for url in found_path]))
        print(f"\nTotale passaggi: {len(found_path) - 1}")
    print("-" * 40)