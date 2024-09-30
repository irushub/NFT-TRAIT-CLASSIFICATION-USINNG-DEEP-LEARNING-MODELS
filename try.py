import os
import json
import requests
from concurrent.futures import ThreadPoolExecutor

# Function to download NFT images based on their ID and eye color
def download_nft_images(nft_ids, eye_color):
    # Create directory if not exists
    if not os.path.exists(eye_color):
        os.makedirs(eye_color)
    
    base_url = "https://madlads.s3.us-west-2.amazonaws.com/images/"
    for nft_id in nft_ids:
        # Check if the image already exists
        if os.path.exists(os.path.join(eye_color, f"{nft_id}.png")):
            print(f"NFT ID {nft_id}.png already exists in {eye_color} folder. Skipping...")
            continue
        
        url = f"{base_url}{nft_id}.png"
        response = requests.get(url)
        if response.status_code == 200:
            # Save image to the corresponding directory
            with open(os.path.join(eye_color, f"{nft_id}.png"), 'wb') as file:
                file.write(response.content)
            print(f"NFT ID {nft_id}.png downloaded and saved to {eye_color} folder.")
        else:
            print(f"Failed to download NFT ID {nft_id}.png")

# Function to fetch metadata from a given link
def fetch_metadata(link):
    response = requests.get(link)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch metadata.")
        return None

# Fetch metadata from the link for NFT IDs from 1 to 6001
metadata_link_template = "https://madlads.s3.us-west-2.amazonaws.com/json/{}.json"
eye_colors = {
    "Blue": [],
    "Green": [],
    "Brown": [],
    "Closed": []
}

for nft_id in range(1, 6002):
    metadata_link = metadata_link_template.format(nft_id)
    metadata = fetch_metadata(metadata_link)
    if metadata:
        # Extract eye color information
        for attribute in metadata.get('attributes', []):
            if attribute.get('trait_type') == 'Eyes':
                eye_color = attribute.get('value')
                # Check eye color and add NFT ID to the corresponding list
                if eye_color == 'Blue':
                    eye_colors['Blue'].append(nft_id)
                elif eye_color == 'Green':
                    eye_colors['Green'].append(nft_id)
                elif eye_color == 'Brown':
                    eye_colors['Brown'].append(nft_id)
                elif eye_color == 'Closed':
                    eye_colors['Closed'].append(nft_id)
                break  # Stop iterating through attributes once eye color is found

# Print the IDs of NFTs for each eye color
for color, nfts in eye_colors.items():
    print(f"IDs of NFTs with {color} eyes:", nfts)

# Download NFT images for each eye color using threading
with ThreadPoolExecutor(max_workers=25) as executor:  # Increase max_workers value as needed
    for color, nfts in eye_colors.items():
        executor.submit(download_nft_images, nfts, color)
