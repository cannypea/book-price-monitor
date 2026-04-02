import requests
import os

def download_image(image_url, category, upc):
    # Create category folder
    folder_path = os.path.join("images", category)
    os.makedirs(folder_path, exist_ok=True)

    # Image filename
    file_path = os.path.join(folder_path, f"{upc}.jpg")

    try:
        response = requests.get(image_url)
        with open(file_path, "wb") as f:
            f.write(response.content)
    except Exception as e:
        print(f"Failed to download image: {e}")