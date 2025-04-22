elements = [
    ["h", 1.008], ["he", 4.003], ["li", 6.94], ["be", 9.012], ["b", 10.81], ["c", 12.011],
    ["n", 14.007], ["o", 15.999], ["f", 18.998], ["ne", 20.180], ["na", 22.99], ["mg", 24.305],
    ["al", 26.982], ["si", 28.085], ["p", 30.974], ["s", 32.06], ["cl", 35.45], ["ar", 39.948],
    ["k", 39.098], ["ca", 40.078], ["sc", 44.956], ["ti", 47.867], ["v", 50.942], ["cr", 51.996],
    ["mn", 54.938], ["fe", 55.845], ["co", 58.933], ["ni", 58.693], ["cu", 63.546], ["zn", 65.38],
    ["ga", 69.723], ["ge", 72.63], ["as", 74.922], ["se", 78.971], ["br", 79.904], ["kr", 83.798],
    ["rb", 85.468], ["sr", 87.62], ["y", 88.906], ["zr", 91.224], ["nb", 92.906], ["mo", 95.95],
    ["tc", 98], ["ru", 101.07], ["rh", 102.91], ["pd", 106.42], ["ag", 107.87], ["cd", 112.41],
    ["in", 114.82], ["sn", 118.71], ["sb", 121.76], ["te", 127.6], ["i", 126.9], ["xe", 131.29],
    ["cs", 132.91], ["ba", 137.33], ["la", 138.91], ["ce", 140.12], ["pr", 140.91], ["nd", 144.24],
    ["pm", 145], ["sm", 150.36], ["eu", 151.96], ["gd", 157.25], ["tb", 158.93], ["dy", 162.5],
    ["ho", 164.93], ["er", 167.26], ["tm", 168.93], ["yb", 173.05], ["lu", 174.97], ["hf", 178.49],
    ["ta", 180.95], ["w", 183.84], ["re", 186.21], ["os", 190.23], ["ir", 192.22], ["pt", 195.08],
    ["au", 196.97], ["hg", 200.59], ["tl", 204.38], ["pb", 207.2], ["bi", 208.98], ["po", 209],
    ["at", 210], ["rn", 222], ["fr", 223], ["ra", 226], ["ac", 227], ["th", 232.04],
    ["pa", 231.04], ["u", 238.03], ["np", 237], ["pu", 244], ["am", 243], ["cm", 247],
    ["bk", 247], ["cf", 251], ["es", 252], ["fm", 257], ["md", 258], ["no", 259],
    ["lr", 262], ["rf", 267], ["db", 270], ["sg", 271], ["bh", 270], ["hs", 277],
    ["mt", 278], ["ds", 281], ["rg", 282], ["cn", 285], ["nh", 286], ["fl", 289],
    ["mc", 290], ["lv", 293], ["ts", 294], ["og", 294]
]

# Function to find the atomic mass of an element by its symbol
def find_mass(symbol):
    for item in elements:
        if item[0] == symbol:
            return item[1]
    return None

# Function to parse formulas like H2O, C6H12O6, NaCl (no regex)
def parse_formula(formula):
    i = 0
    length = len(formula)
    composition = {}

    while i < length:
        # Get element symbol (1 or 2 characters)
        if i + 1 < length and formula[i+1].islower():
            symbol = formula[i] + formula[i+1]
            i += 2
        else:
            symbol = formula[i]
            i += 1
        symbol = symbol.lower()

        # Get the count if any
        count = ""
        while i < length and formula[i].isdigit():
            count += formula[i]
            i += 1
        count = int(count) if count else 1

        if symbol in composition:
            composition[symbol] += count
        else:
            composition[symbol] = count

    return composition

# Main loop for user interaction
while True:
    print("Choose a calculation:")
    print("1 - Molar Mass from Molecular Formula")
    print("2 - Mass from Moles")
    print("3 - Moles from Mass")
    print("4 - Volume from Moles (gas at STP)")
    print("5 - Moles from Volume (gas at STP)")
    print("6 - Percent Composition (2 elements)")

    choice = input("Enter option (1-6): ")

    if choice == "1":
        formula = input("Enter molecular formula (e.g., H2O, CO2, C6H12O6): ")
        composition = parse_formula(formula)

        total_mass = 0
        for element, count in composition.items():
            mass = find_mass(element)
            if mass is None:
                print(f"Element '{element}' not found.")
                break
            total_mass += mass * count
        else:
            try:
                mol = float(input("Enter the number of moles: "))
            except ValueError:
                print("Invalid input.")
                continue

            final_mass = total_mass * mol
            volume = mol * 22.4

            print("\n--- Results ---")
            print(f"Molecular formula: {formula}")
            print(f"Molar mass = {round(total_mass, 3)} g/mol")
            print(f"Mass = {round(final_mass, 3)} grams")
            print(f"Volume at STP = {round(volume, 3)} L")

    elif choice == "2":
        try:
            molar_mass = float(input("Enter molar mass: "))
            moles = float(input("Enter moles: "))
        except ValueError:
            print("Invalid input.")
            continue
        print(f"Mass = {molar_mass * moles} grams")

    elif choice == "3":
        try:
            mass = float(input("Enter mass (grams): "))
            molar_mass = float(input("Enter molar mass: "))
        except ValueError:
            print("Invalid input.")
            continue
        print(f"Moles = {mass / molar_mass}")

    elif choice == "4":
        try:
            moles = float(input("Enter moles: "))
        except ValueError:
            print("Invalid input.")
            continue
        print(f"Volume at STP = {moles * 22.4} L")

    elif choice == "5":
        try:
            volume = float(input("Enter volume (L): "))
        except ValueError:
            print("Invalid input.")
            continue
        print(f"Moles = {volume / 22.4}")

    elif choice == "6":
        try:
            mass1 = float(input("Enter mass of element 1: "))
            atoms1 = int(input("Enter number of atoms of element 1: "))
            mass2 = float(input("Enter mass of element 2: "))
            atoms2 = int(input("Enter number of atoms of element 2: "))
        except ValueError:
            print("Invalid input.")
            continue
        total_mass = mass1 * atoms1 + mass2 * atoms2
        pc1 = (mass1 * atoms1 / total_mass) * 100
        pc2 = (mass2 * atoms2 / total_mass) * 100
        print(f"Percent Composition of Element 1 = {round(pc1, 2)}%")
        print(f"Percent Composition of Element 2 = {round(pc2, 2)}%")

    else:
        print("Invalid choice.")

    again = input("Run again? (y/n): ")
    if again.lower() != "y":
        break
