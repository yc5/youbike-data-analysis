import json
import glob
import argparse


def percentage_str(percentage, str_len):
    return ("*" * int(percentage * str_len)).ljust(str_len, "-")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", help="station name", required=True)
    parser.add_argument("-c", "--control", help="control station name")
    args = parser.parse_args()

    json_files = glob.glob(f"downloaded/taipei*.json")
    json_files.sort()

    for file in json_files:
        try:
            with open(file, "r") as f:
                data = json.load(f)
                station = [x for x in data if args.name in x["sna"]]
                if len(station) == 0:
                    raise Exception("Station Name Not Found")
                station = station[0]
                if not args.control:
                    print(station["sna"], end="")
                    print(",", end="")
                print(station["srcUpdateTime"], end="")
                print(",", end="")
                print(percentage_str(station["sbi"] / station["tot"], 50), end="")
                if not args.control:
                    print(",", end="")
                    print(station["tot"], end="")
                    print(",", end="")
                    print(station["sbi"], end="")
                else:
                    station = [x for x in data if args.control in x["sna"]]
                    if len(station) == 0:
                        raise Exception("Station Name Not Found")
                    station = station[0]
                    print(
                        "," + percentage_str(station["sbi"] / station["tot"], 50),
                        end="",
                    )

                print()
        except FileNotFoundError:
            print(f"Error: File '{file}' not found.")
        except Exception as e:
            print(e)
            # break
