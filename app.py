import argparse
from utils import read_json, filter_exclusives, set_profits, info_motoboy


def main():
    # Parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--motoboy",
        help="Display information about a single motoboy",
        type=str,
    )
    args = parser.parse_args()
    motoboy = getattr(args, "motoboy", None)

    # Load the motoboys and shops informations
    motoboys = read_json("motoboys.json")
    shops = read_json("shops.json")

    # Calculate the profits and orders for each motoboy
    non_priority = filter_exclusives(motoboys, shops)
    set_profits(motoboys, shops, non_priority)

    # Print the information of the specified motoboy or for each one
    print("\nMotoboys informations:")
    print(f"{'-' * 28}\n")
    if motoboy:
        try:
            info_motoboy(motoboy, motoboys[motoboy])
        except KeyError:
            print("Motoboy not found!")
    else:
        for id_motoboy, motoboy in motoboys.items():
            info_motoboy(id_motoboy, motoboy)


if __name__ == "__main__":
    main()
