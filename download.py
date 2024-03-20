import datetime
import requests
import os

cwd = os.getcwd()


url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"

response = requests.get(url)
if response.status_code == 200:
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    print(cwd)

    filename = f"downloaded/taipei_youbike_immediate_{now}.json"
    with open(filename, "wb") as f:
        f.write(response.content)
        print(f"Saved {filename} to local disk.")
else:
    print(f"Failed to get {url}, status code: {response.status_code}")
