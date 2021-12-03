import json
from json import JSONDecodeError


class ListIterator:
    """
    Custom iterator to reset the index

    Parameters
    ----
    ls: list
        The list to iterate over
    """
    def __init__(self, ls):
        self.ls = ls
        self.idx = 0
    def __iter__(self):
        return self
    def rewind(self):
        self.idx = 0
    def __next__(self):
        try:
            return self.ls[self.idx]
        except IndexError:
            raise StopIteration
        finally:
            self.idx += 1

def filter_exclusives(motoboys: dict, shops: dict) -> list:
    """
    Filters the exclusive motoboys each to a shop and returns the non exclusive motoboys
    
    Parameters
    ----
    motoboys : dict
        Motoboys data structure
    shops : str
        Shops data structure
    
    Returns
    ----
    list
        List of motoboys that are not exclusive
    """
    non_priority = []
    for motoboy in motoboys:
        # If the motoboy is exclusive add it to the shop 
        # else add it to the non priority list
        if "exclusive" in motoboys[motoboy]:
            if motoboys[motoboy]["exclusive"] in shops:
                try:
                    shops[motoboys[motoboy]["exclusive"]]["priority"].append(motoboy)
                except KeyError:
                    shops[motoboys[motoboy]["exclusive"]]["priority"] = [motoboy]
        else:
            non_priority.append(motoboy)
    return non_priority

def set_profits(motoboys: dict, shops: dict, non_priority: list) -> None:
    """
    Sets the profits of each motoboy for each shop

    Parameters
    ----
    motoboys : dict
        Motoboys data structure
    shops : dict
        Shops data structure
    non_priority : list
        List of motoboys that are not exclusive
    """
    temp_iter = None
    all_motoboys = ListIterator(non_priority) if non_priority else None
    for shop in shops:
        priority_motoboys = None
        current_motoboys = all_motoboys
        # If the shop has priority motoboys always start with them
        if "priority" in shops[shop]:
            priority_motoboys = ListIterator(shops[shop]["priority"])
            current_motoboys = priority_motoboys
        next_motoboys = all_motoboys if all_motoboys else priority_motoboys
        # When there is no motoboy to be assigned to the shop continue to next shop
        if not current_motoboys:
            continue
        # Calculate the profits for each motoboy
        for order in shops[shop]["orders"]:
            try:
                motoboy = next(current_motoboys)
            except StopIteration:
                # If there are no more motoboys in the iterator 
                # switch to the other list and reset the iterator
                temp_iter = current_motoboys
                current_motoboys = next_motoboys
                next_motoboys = temp_iter
                next_motoboys.rewind()
                motoboy = next(current_motoboys)
            # Calculate the profit for the motoboy and build the profits list
            profit = (order * shops[shop]["fee"]) + motoboys[motoboy]["cost"]
            try:
                motoboys[motoboy]["profits"][shop].append(profit)
            except KeyError:
                motoboys[motoboy]["profits"][shop] = [profit]

def info_motoboy(id_motoboy: str, motoboy: dict) -> None:
    """
    Prints the information of a motoboy

    Parameters
    ----
    id_motoboy : str
        Motoboy id
    motoboy : dict
        Motoboy data structure
    """
    print(f"Profits and orders motoboy {id_motoboy}\n")
    total_profit = 0
    total_orders = 0
    # Print the profits and orders for each shop
    # and calculate the total profit and orders
    for shop in motoboy["profits"]:
        profit = sum(motoboy['profits'][shop])
        orders = len(motoboy['profits'][shop])
        total_profit += profit
        total_orders += orders
        print(f"SHOP {shop}:")
        print("\tProfit: R${:.2f}".format(profit))
        print(f"\t{orders} order(s)")
    print("\nTotal profit: R${:.2f}".format(total_profit))
    print(f"Total order(s): {total_orders}")
    print(f"\n{'-' * 28}\n")

def read_json(file_name: str) -> dict:
    """
    Reads the json file and returns the data structure

    Parameters
    ----
    file_name : str
        File name to be read
    
    Returns
    ----
    dict
        Data structure of the json file
    """
    try:
        with open(file_name, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {file_name} not found")
        return {}
    except JSONDecodeError:
        print(f"Invalid json file {file_name}")
        return {}
