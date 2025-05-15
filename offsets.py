import requests
import os
from datetime import datetime

# URLs of the files to download
urls = [
    "https://offsets.ntgetwritewatch.workers.dev/offsets.hpp",
    "https://offsets.ntgetwritewatch.workers.dev/offsets.json",
    "https://offsets.ntgetwritewatch.workers.dev/version"
]

# Create a folder with the current date (YYYY-MM-DD)
current_date = datetime.now().strftime("%Y-%m-%d")
os.makedirs(current_date, exist_ok=True)

# Download and save each file
for url in urls:
    try:
        # Get the file name from the URL
        file_name = os.path.basename(url)
        # Define the full path for saving the file
        file_path = os.path.join(current_date, file_name)
        
        # Download the file
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        
        # Save the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"Successfully downloaded and saved {file_name} to {file_path}")
    
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")