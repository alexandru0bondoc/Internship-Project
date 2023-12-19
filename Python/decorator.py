# DECORATOR de verificare format
def validateCNP(func):
    def wrapper(cnp):
        if len(cnp) != 13 or not cnp.isdigit():
            raise ValueError("Invalid CNP format. CNP must be only 13 digits long")
        return func(cnp)

    return wrapper


@validateCNP
def structure_cnp(cnp):
    # SAALLZZJJNNNC
    # S - sex, secol, rezidentiat
    # AA- ultimele 2 cifre ale anului de nastere
    # LL- luna de nastere valori intre 01 - 12
    # ZZ- ziua de nastere
    # JJ- judetul sau sectorul de nastere / domiciliu , resedinta in momentul acordarii CNP

    # NNN-numar secvential (001-999) repartizat pe puncte de atribuire, prin care se diferențiază
    # persoanele de același sex, născute în același loc și cu aceeași dată de naștere

    # C - cifra de control care permite depistarea eventualelor erori de înlocuire sau
    # inversare a cifrelor din componența C.N.P.

    # For CNP cases that begin with 7 and 8 (addressing residents)
    born_Here = True

    # All the regions
    rList = ["Alba", "Arad", "Argeș", "Bacău", "Bihor", "Bistrița-Năsăud",
             "Botoșani", "Brașov", "Brăila", "Buzău", "Caraș-Severin", "Cluj",
             "Constanța", "Covasna", "Dâmbovița", "Dolj", "Galați", "Gorj",
             "Harghita", "Hunedoara", "Ialomița", "Iași", "Ilfov", "Maramureș",
             "Mehedinți", "Mureș", "Neamț", "Olt", "Prahova", "Satu Mare",
             "Sălaj", "Sibiu", "Suceava", "Teleorman", "Timiș", "Tulcea",
             "Vaslui", "Vâlcea", "Vrancea", "București", "București - Sector 1",
             "București - Sector 2", "București - Sector 3", "București - Sector 4",
             "București - Sector 5", "București - Sector 6", "Călărași", "Giurgiu"]

    # List with the codes for the regions
    rACodeLZ = [f"{num:02d}" for num in range(1, 47)]
    rACodeLZ.append("51")
    rACodeLZ.append("52")

    # Dictionary for region code and region name
    region_dict = dict(zip(rACodeLZ, rList))

    genders = int(cnp[0])  # S
    b_year = int(cnp[1:3])  # AA
    b_month = int(cnp[3:5])  # LL
    b_day = int(cnp[5:7])  # ZZ
    rCode = f"{int(cnp[7:9]):02d}"  # JJ
    # seq = int(cnp[9:12])     # NNN
    # cControl = int(cnp[12])  # C

    # Setting the birth year full not just the last 2 digits
    if genders in [1, 2]:
        b_year += 1900
    elif genders in [3, 4]:
        b_year += 1800
    elif genders in [5, 6]:
        b_year += 2000
    elif genders in [7, 8]:
        born_Here = False
    else:
        # Handling the error for other values
        raise ValueError("Invalid CNP format. S component should be from 1 to 8")

    # Getting the gender
    if genders % 2 == 1:
        gender = "Male"
    else:
        gender = "Female"

    # Getting the format for the birthday date
    b_date = f"{b_day:02d}-{b_month:02d}-{b_year}"

    # Getting the exact region on the CNP
    region = region_dict.get(rCode, "Unknown")

    return {
        "Gender": gender,
        "Birth Date": b_date,
        "Region": region,
        "Born in this country": born_Here
    }


@validateCNP
def cValid(cnp):
    # the constant used for the following computation
    CONSTANTA = "279146358279"

    control_sum = sum(int(cnp[i]) * int(CONSTANTA[i]) for i in range(12))
    computed_control = control_sum % 11

    if computed_control == 10:
        computed_control = 1

    return computed_control == int(cnp[12])


cnp_example = "1880106028331"
structure = structure_cnp(cnp_example)
valid = cValid(cnp_example)

print("Structura CNP:", structure)
print("CNP valid:", valid)
