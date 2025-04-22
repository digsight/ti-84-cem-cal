#V2
element_masses = {
    "H": 1.008, "He": 4.003, "Li": 6.94, "Be": 9.012, "B": 10.81, "C": 12.011,
    "N": 14.007, "O": 15.999, "F": 18.998, "Ne": 20.180, "Na": 22.99, "Mg": 24.305,
    "Al": 26.982, "Si": 28.085, "P": 30.974, "S": 32.06, "Cl": 35.45, "Ar": 39.948,
    "K": 39.098, "Ca": 40.078, "Sc": 44.956, "Ti": 47.867, "V": 50.942, "Cr": 51.996,
    "Mn": 54.938, "Fe": 55.845, "Co": 58.933, "Ni": 58.693, "Cu": 63.546, "Zn": 65.38,
    "Ga": 69.723, "Ge": 72.63, "As": 74.922, "Se": 78.971, "Br": 79.904, "Kr": 83.798,
    "Rb": 85.468, "Sr": 87.62, "Y": 88.906, "Zr": 91.224, "Nb": 92.906, "Mo": 95.95,
    "Tc": 98, "Ru": 101.07, "Rh": 102.91, "Pd": 106.42, "Ag": 107.87, "Cd": 112.41,
    "In": 114.82, "Sn": 118.71, "Sb": 121.76, "Te": 127.6, "I": 126.9, "Xe": 131.29,
    "Cs": 132.91, "Ba": 137.33, "La": 138.91, "Ce": 140.12, "Pr": 140.91, "Nd": 144.24,
    "Pm": 145, "Sm": 150.36, "Eu": 151.96, "Gd": 157.25, "Tb": 158.93, "Dy": 162.5,
    "Ho": 164.93, "Er": 167.26, "Tm": 168.93, "Yb": 173.05, "Lu": 174.97, "Hf": 178.49,
    "Ta": 180.95, "W": 183.84, "Re": 186.21, "Os": 190.23, "Ir": 192.22, "Pt": 195.08,
    "Au": 196.97, "Hg": 200.59, "Tl": 204.38, "Pb": 207.2, "Bi": 208.98, "Po": 209,
    "At": 210, "Rn": 222, "Fr": 223, "Ra": 226, "Ac": 227, "Th": 232.04,
    "Pa": 231.04, "U": 238.03, "Np": 237, "Pu": 244, "Am": 243, "Cm": 247,
    "Bk": 247, "Cf": 251, "Es": 252, "Fm": 257, "Md": 258, "No": 259,
    "Lr": 262, "Rf": 267, "Db": 270, "Sg": 271, "Bh": 270, "Hs": 277,
    "Mt": 278, "Ds": 281, "Rg": 282, "Cn": 285, "Nh": 286, "Fl": 289,
    "Mc": 290, "Lv": 293, "Ts": 294, "Og": 294
}

def find_mass(symbol):
    return element_masses.get(symbol, None)

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Try again.")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer. Try again.")

def get_element(prompt):
    symbol = input(prompt)
    mass = find_mass(symbol)
    if mass is None:
        print("Element not found.")
        return None, None
    atoms = get_int("How many atoms of " + symbol + "? ")
    return mass, atoms

def molar_mass_calc():
    total_mass = 0
    num_elements = get_int("How many elements? (1 or 2): ")
    if num_elements not in [1, 2]:
        print("Only 1 or 2 elements supported.")
        return
    for i in range(num_elements):
        mass, atoms = get_element("Enter symbol for element " + str(i + 1) + ": ")
        if mass is None:
            return
        total_mass += mass * atoms
    mol = get_float("Enter number of moles: ")
    final_mass = total_mass * mol
    volume = mol * 22.4
    print("")
    print("--- Results ---")
    print("Molar mass = " + str(round(total_mass, 3)) + " g/mol")
    print("Mass = " + str(round(final_mass, 3)) + " grams")
    print("Volume at STP = " + str(round(volume, 3)) + " L")

def mass_from_moles():
    molar_mass = get_float("Enter molar mass: ")
    moles = get_float("Enter moles: ")
    print("Mass = " + str(round(molar_mass * moles, 3)) + " grams")

def moles_from_mass():
    mass = get_float("Enter mass (grams): ")
    molar_mass = get_float("Enter molar mass: ")
    print("Moles = " + str(round(mass / molar_mass, 3)))

def volume_from_moles():
    moles = get_float("Enter moles: ")
    print("Volume at STP = " + str(round(moles * 22.4, 3)) + " L")

def moles_from_volume():
    volume = get_float("Enter volume (L): ")
    print("Moles = " + str(round(volume / 22.4, 3)))

def percent_composition():
    mass1 = get_float("Enter mass of element 1: ")
    atoms1 = get_int("Enter number of atoms of element 1: ")
    mass2 = get_float("Enter mass of element 2: ")
    atoms2 = get_int("Enter number of atoms of element 2: ")
    total_mass = mass1 * atoms1 + mass2 * atoms2
    pc1 = (mass1 * atoms1 / total_mass) * 100
    pc2 = (mass2 * atoms2 / total_mass) * 100
    print("Percent Composition of Element 1 = " + str(round(pc1, 2)) + " %")
    print("Percent Composition of Element 2 = " + str(round(pc2, 2)) + " %")

def main():
    while True:
        print("")
        print("--- Chemistry Calculator ---")
        print("1 - Molar Mass from 1-2 elements")
        print("2 - Mass from Moles")
        print("3 - Moles from Mass")
        print("4 - Volume from Moles (gas at STP)")
        print("5 - Moles from Volume (gas at STP)")
        print("6 - Percent Composition (2 elements)")
        choice = input("Choose an option (1-6): ")
        if choice == "1":
            molar_mass_calc()
        elif choice == "2":
            mass_from_moles()
        elif choice == "3":
            moles_from_mass()
        elif choice == "4":
            volume_from_moles()
        elif choice == "5":
            moles_from_volume()
        elif choice == "6":
            percent_composition()
        else:
            print("Invalid option.")
        again = input("Run another calculation? (y/n): ")
        if again != "y":
            break

main()
