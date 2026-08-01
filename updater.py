import json

DB_FILE = "database.json"

def update_database():
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Pulizia base dei dati
        for player in data:
            player["nome"] = player["nome"].strip()
            player["squadra"] = player["squadra"].strip()

        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print("Database sincronizzato con successo!")
    except Exception as e:
        print(f"Errore durante l'aggiornamento: {e}")

if __name__ == "__main__":
    update_database()
