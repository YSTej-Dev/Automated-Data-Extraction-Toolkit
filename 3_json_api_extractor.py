import requests
import csv

print("=== JSON API DATA MINER ===")
print("Compiling target list...")

# Target queries
targets = ["pikachu", "charizard", "snorlax"]

with open('api_dataset.csv', mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Entity Name', 'Weight Parameter', 'Base Experience'])
    
    print("Initiating server requests...")
    for target in targets:
        # Dynamic API endpoint integration
        url = f"https://pokeapi.co/api/v2/pokemon/{target}"
        response = requests.get(url)
        
        if response.status_code == 200:
            # Parse raw JSON response into a Python dictionary
            data = response.json()
            
            name = data['name'].capitalize()
            weight = data['weight']
            xp = data['base_experience']
            
            writer.writerow([name, weight, xp])
            print(f"Data acquired for: {name}")
        else:
            print(f"Target not found: {target}")

print("✅ PROCESS COMPLETE: Data structured and saved to api_dataset.csv")