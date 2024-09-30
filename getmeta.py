import os
import requests
from concurrent.futures import ThreadPoolExecutor

def download_metadata(nft_id):
    url = f"https://madlads.s3.us-west-2.amazonaws.com/json/{nft_id}.json"
    response = requests.get(url)
    if response.status_code == 200:
        filename = f"{metadata_folder}/{nft_id}.json"
        with open(filename, 'w') as file:
            file.write(response.text)
        print(f"Metadata saved for NFT ID: {nft_id}")
    else:
        print(f"Failed to fetch metadata for NFT ID: {nft_id}")

metadata_folder = "metadata"
if not os.path.exists(metadata_folder):
    os.makedirs(metadata_folder)

max_threads = 15  # You can adjust this based on your system's capabilities

with ThreadPoolExecutor(max_workers=max_threads) as executor:

    for nft_id in range(4001,6001):
        executor.submit(download_metadata, nft_id)

print("All metadata downloaded and saved.")
