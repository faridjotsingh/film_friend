import json

def load_theaters():
    try:
        with open("data/theaters.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data["theaters"]
    except FileNotFoundError:
        print("File not found")
        return []
    except json.JSONDecodeError:
        print("File is broken JSON")
        return []

def get_theater(theater_id):
    theaters = load_theaters()
    for theater in theaters:
        if theater["id"] == theater_id:
            return theater
    return None

print(get_theater(1)["name"])    
print(get_theater(999)) 