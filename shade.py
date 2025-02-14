import vlc
import time
import requests

# URL du flux de Shade 45
shade45_url = "http://streaming.radio.co/sb0e0a1a4a/listen"

# Essayer de récupérer le flux pour vérifier l'accès
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

response = requests.get(shade45_url, headers=headers)

if response.status_code == 200:
    # Créer un objet VLC
    instance = vlc.Instance()
    player = instance.media_player_new()

    # Charger le flux
    media = instance.media_new(shade45_url)
    player.set_media(media)

    # Démarrer la lecture
    player.play()

    print("Écoute de Shade 45. Appuyez sur 'q' pour quitter.")

    # Boucle d'attente pour garder le programme en cours d'exécution
    while True:
        command = input()
        if command.lower() == 'q':
            break

    # Arrêter la lecture
    player.stop()
    print("Lecture arrêtée.")
else:
    print(f"Erreur d'accès au flux : {response.status_code}")

