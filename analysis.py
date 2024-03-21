import json
import glob
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", help="station name", required=True)
    args = parser.parse_args()
    station_name = args.name

    json_files = glob.glob(f"downloaded/taipei*.json")
    json_files.sort()

    for file in json_files:
        try:
            with open(file, "r") as f:
                data = json.load(f)
                station = [x for x in data if station_name in x["sna"]]
                if len(station) == 0:
                    raise Exception("Station Name Not Found")
                station = station[0]
                print(station["sna"], end="")
                print(",", end="")
                print(station["srcUpdateTime"], end="")
                print(",", end="")
                print(station["tot"], end="")
                print(",", end="")
                print(station["sbi"], end="")
                print()
        except FileNotFoundError:
            print(f"Error: File '{file}' not found.")
        except Exception as e:
            print(e)
            #break
