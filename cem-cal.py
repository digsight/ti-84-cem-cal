ELEMENT_MASSES = {
    "h": 1.008, "he": 4.003, "li": 6.94, "be": 9.012, "b": 10.81, "c": 12.011,
    "n": 14.007, "o": 15.999, "f": 18.998, "ne": 20.180, "na": 22.99, "mg": 24.305,
    "al": 26.982, "si": 28.085, "p": 30.974, "s": 32.06, "cl": 35.45, "ar": 39.948,
    "k": 39.098, "ca": 40.078, "sc": 44.956, "ti": 47.867, "v": 50.942, "cr": 51.996,
    "mn": 54.938, "fe": 55.845, "co": 58.933, "ni": 58.693, "cu": 63.546, "zn": 65.38,
    "ga": 69.723, "ge": 72.63, "as": 74.922, "se": 78.971, "br": 79.904, "kr": 83.798,
    "rb": 85.468, "sr": 87.62, "y": 88.906, "zr": 91.224, "nb": 92.906, "mo": 95.95,
    "tc": 98, "ru": 101.07, "rh": 102.91, "pd": 106.42, "ag": 107.87, "cd": 112.41,
    "in": 114.82, "sn": 118.71, "sb": 121.76, "te": 127.6, "i": 126.9, "xe": 131.29,
    "cs": 132.91, "ba": 137.33, "la": 138.91, "ce": 140.12, "pr": 140.91, "nd": 144.24,
    "pm": 145, "sm": 150.36, "eu": 151.96, "gd": 157.25, "tb": 158.93, "dy": 162.5,
    "ho": 164.93, "er": 167.26, "tm": 168.93, "yb": 173.05, "lu": 174.97, "hf": 178.49,
    "ta": 180.95, "w": 183.84, "re": 186.21, "os": 190.23, "ir": 192.22, "pt": 195.08,
    "au": 196.97, "hg": 200.59, "tl": 204.38, "pb": 207.2, "bi": 208.98, "po": 209,
    "at": 210, "rn": 222, "fr": 223, "ra": 226, "ac": 227, "th": 232.04,
    "pa": 231.04, "u": 238.03, "np": 237, "pu": 244, "am": 243, "cm": 247,
    "bk": 247, "cf": 251, "es": 252, "fm": 257, "md": 258, "no": 259,
    "lr": 262, "rf": 267, "db": 270, "sg": 271, "bh": 270, "hs": 277,
    "mt": 278, "ds": 281, "rg": 282, "cn": 285, "nh": 286, "fl": 289,
    "mc": 290, "lv": 293, "ts": 294, "og": 294
}

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Invalid number. Please try again.")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("Invalid integer. Please try again.")

def get_element_data():
    while True:
        symbol = input("Enter element symbol: ").strip().lower()
        if symbol not in ELEMENT_MASSES:
            print("Error: Element '" + symbol + "' not found. Try again or type 'exit' to cancel.")
            if symbol == 'exit':
                return None
            continue

        atoms = get_int("How many atoms of " + symbol + "? ")
        if atoms <= 0:
            print("Number of atoms must be positive.")
            continue

        return ELEMENT_MASSES[symbol], atoms

def calculate_molar_mass():
    print("\n--- Molar Mass Calculator ---")
    num_elements = get_int("How many elements in the compound? ")
    if num_elements <= 0:
        print("Number of elements must be positive.")
        return

    total_mass = 0.0
    for i in range(1, num_elements + 1):
        print("\nElement " + str(i) + ":")
        element_data = get_element_data()
        if element_data is None:
            return
        mass, atoms = element_data
        total_mass += mass * atoms

    if total_mass <= 0:
        print("Error: Total mass must be positive.")
        return

    mol = get_float("\nEnter number of moles: ")
    final_mass = total_mass * mol
    volume = mol * 22.4

    print("\n--- Results ---")
    print("Molar mass = " + str(round(total_mass, 3)) + " g/mol")
    print("Mass = " + str(round(final_mass, 3)) + " grams")
    print("Volume at STP = " + str(round(volume, 3)) + " L")

def calculate_mass_from_moles():
    print("\n--- Mass from Moles Calculator ---")
    molar_mass = get_float("Enter molar mass (g/mol): ")
    moles = get_float("Enter moles: ")
    print("\nMass = " + str(round(molar_mass * moles, 3)) + " grams")

def calculate_moles_from_mass():
    print("\n--- Moles from Mass Calculator ---")
    mass = get_float("Enter mass (grams): ")
    molar_mass = get_float("Enter molar mass (g/mol): ")
    if molar_mass == 0:
        print("Error: Molar mass cannot be zero.")
        return
    print("\nMoles = " + str(round(mass / molar_mass, 3)))

def calculate_volume_from_moles():
    print("\n--- Volume from Moles Calculator ---")
    moles = get_float("Enter moles: ")
    print("\nVolume at STP = " + str(round(moles * 22.4, 3)) + " L")

def calculate_moles_from_volume():
    print("\n--- Moles from Volume Calculator ---")
    volume = get_float("Enter volume (L): ")
    if volume <= 0:
        print("Volume must be positive.")
        return
    print("\nMoles = " + str(round(volume / 22.4, 3)))

def calculate_percent_composition():
    print("\n--- Percent Composition Calculator ---")
    print("Element 1:")
    element1 = get_element_data()
    if element1 is None:
        return
    mass1, atoms1 = element1

    print("\nElement 2:")
    element2 = get_element_data()
    if element2 is None:
        return
    mass2, atoms2 = element2

    total_mass = (mass1 * atoms1) + (mass2 * atoms2)
    if total_mass <= 0:
        print("Error: Total mass must be positive.")
        return

    pc1 = (mass1 * atoms1 / total_mass) * 100
    pc2 = (mass2 * atoms2 / total_mass) * 100

    print("\n--- Results ---")
    print("Percent Composition of Element 1 = " + str(round(pc1, 2)) + "%")
    print("Percent Composition of Element 2 = " + str(round(pc2, 2)) + "%")

def main():
    while True:
        print("\n=== Chemistry Calculator ===")
        print("1. Molar Mass Calculator")
        print("2. Mass from Moles")
        print("3. Moles from Mass")
        print("4. Volume from Moles (gas at STP)")
        print("5. Moles from Volume (gas at STP)")
        print("6. Percent Composition (2 elements)")
        print("7. Exit")

        choice = input("\nChoose an option (1-7): ").strip()

        if choice == "1":
            calculate_molar_mass()
        elif choice == "2":
            calculate_mass_from_moles()
        elif choice == "3":
            calculate_moles_from_mass()
        elif choice == "4":
            calculate_volume_from_moles()
        elif choice == "5":
            calculate_moles_from_volume()
        elif choice == "6":
            calculate_percent_composition()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-7.")

        if choice != "7":
            input("\nPress Enter to continue...")

main()
