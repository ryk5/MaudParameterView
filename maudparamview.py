from tabulate import tabulate
import pandas as pd
def main():
    filename = input("Name of text file (with .txt): ")
    num = int(input("How many phases are you analyzing?: "))
    names = []
    lattices = []
    latticerrors = []
    crystalsizes = []
    crystalerrors = []
    microstrains = []
    microerrors = []
    fractions = []
    fracerrors = []
    for i in range(num):
        temp = input("Name of element #" + str(i) + ": ")
        names.append(temp)
    r = open('filename')
    for n in r.readlines():
        if "_pd_phase_atom_%" in n:
            arr = n.split()
            fractions.append(arr[1])
            fracerrors.append(arr[4])
        elif "_cell_length_a" in n:
            arr = n.split()
            lattices.append(arr[1])
            latticerrors.append(arr[4])
        elif "_riet_par_cryst_size" in n:
            arr = n.split()
            crystalsizes.append(arr[1])
            crystalerrors.append(arr[4])
        elif "_riet_par_rs_microstrain" in n:
            arr = n.split()
            microstrains.append(arr[1])
            microerrors.append(arr[4])
        

    dict = {'Name':names,
        'Lattice':lattices,
        'Lattice Error':latticerrors,
        'Crystal Size':crystalsizes,
        'Crystal Error': crystalerrors,
        'Microstrain': microstrains,
        'Micro Error': microerrors,
        'Fraction': fractions,
        'Fraction Error': fracerrors}
    df = pd.DataFrame(dict)
    print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
    
if __name__ == "__main__":
    main()