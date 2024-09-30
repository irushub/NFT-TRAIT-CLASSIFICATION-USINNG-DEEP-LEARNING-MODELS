import os
import json
import requests
from concurrent.futures import ThreadPoolExecutor

def download_nft_images(nft_ids, eye_color):
    if not os.path.exists(eye_color):
        os.makedirs(eye_color)
    
    base_url = "https://madlads.s3.us-west-2.amazonaws.com/images/"
    for nft_id in nft_ids:
        if os.path.exists(os.path.join(eye_color, f"{nft_id}.png")):
            print(f"NFT ID {nft_id}.png already exists in {eye_color} folder. Skipping...")
            continue
        
        url = f"{base_url}{nft_id}.png"
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(eye_color, f"{nft_id}.png"), 'wb') as file:
                file.write(response.content)
            print(f"NFT ID {nft_id}.png downloaded and saved to {eye_color} folder.")
        else:
            print(f"Failed to download NFT ID {nft_id}.png")

metadata_folder = "metadata"

eye_colors = {
    "Blue": [],
    "Green": [],
    "Brown": [],
    "Closed": []
}

for filename in os.listdir(metadata_folder):
    if filename.endswith(".json"):
        filepath = os.path.join(metadata_folder, filename)
        with open(filepath, 'r') as file:

            metadata = json.load(file)
            
            for attribute in metadata.get('attributes', []):
                if attribute.get('trait_type') == 'Eyes':
                    eye_color = attribute.get('value')
                    nft_id = int(filename.split('.')[0])  
                    if eye_color == 'Blue':
                        eye_colors['Blue'].append(nft_id)
                    elif eye_color == 'Green':
                        eye_colors['Green'].append(nft_id)
                    elif eye_color == 'Brown':
                        eye_colors['Brown'].append(nft_id)
                    elif eye_color == 'Closed':
                        eye_colors['Closed'].append(nft_id)
                    break  

for color, nfts in eye_colors.items():
    print(f"IDs of NFTs with {color} eyes:", nfts)

with ThreadPoolExecutor(max_workers=25) as executor: 
    for color, nfts in eye_colors.items():
        executor.submit(download_nft_images, nfts, color)
