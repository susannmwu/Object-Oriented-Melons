############
# Part 1   #
############
# objects to define in tic tac toe game 
# player
# move
# board 
# game


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, name, first_harvest, color, is_seedless, is_bestseller,
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.name = name
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType(
        "musk",
        "Muskmelon",
        1998, 
        "green",
        True,
        True
    )
    musk.add_pairing("mint")
    
    # add musk to the list of melon types
    all_melon_types.append(musk)

    cas = MelonType(
        "cas",
        "Casaba",
        2003,
        "orange",
        False,
        False
    )
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")

    # adds cas to list of all melon types 
    all_melon_types.append(cas)

    cren = MelonType(
        "cren",
        "Casaba",
        1996, 
        "green",
        False, 
        False
    )

    cren.add_pairing("prosciutto")

    all_melon_types.append(cren)

    yw = MelonType(
        "yw",
        "Yellow Watermelon",
        2013, 
        "yellow",
        False,
        True
    )

    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types



def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name} pairs with:")
        for pairing in melon.pairings:
            print(f" - {pairing}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    # create an empty dictionary 
    melon_by_code = {}

    for melon in melon_types:
        if melon.code not in melon_by_code:
            melon_by_code[melon.code] = melon
    return melon_by_code

all_melon_types = make_melon_types()
print_pairing_info(all_melon_types)

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(
            self, code, shape_rating, color_rating, harvested_from_field, harvested_by
    ):
        "initialize a melon harvested"
        
        self.code = code 
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from_field = harvested_from_field
        self.harvested_by = harvested_by
    #Create a function to determine melon salablility. Melons are salable if shape and color ratings > 5 and does not come from field3 
    
    def is_melon_salable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.harvested_from_field != 3:
            return True 
        else:
            return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    melon_by_code = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melon_by_code["yw"], 8, 7, 2, "Sheila")
    melon_2 = Melon(melon_by_code["yw"], 3, 4, 2, "Sheila")
    melon_3 = Melon(melon_by_code["yw"], 9, 8, 3, "Sheila")
    melon_4 = Melon(melon_by_code["cas"], 10, 6, 35,"Sheila")
    melon_5 = Melon(melon_by_code["cren"],8, 9, 35, "Michael")
    melon_6 = Melon(melon_by_code["cren"], 2, 3, 4, "Michael")
    melon_7 = Melon(melon_by_code["cren"], 2, 3, 4, "Michael")
    melon_8 = Melon(melon_by_code["musk"], 6, 7, 4, "Michael")
    melon_9 = Melon(melon_by_code["yw"], 7, 10, 3, "Sheila")

    # Create a list of melons
    melons = [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9]

    return melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
    for melon in melons:
        harvested_by = f"Harvested by {melon.harvested_by}"
        harvested_from_field = f"Field # {melon.harvested_from_field}"
        salability = "CAN BE SOLD" if melon.is_melon_salable() else "NOT SALABLE"

    print(f"{harvested_by} from {harvested_from_field} {salability}")


get_sellability_report(make_melons)