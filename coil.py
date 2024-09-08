import math

def compute_coil_outer_diameter(L, iD, T):
    outer_diameter = round((math.sqrt((L * T) / math.pi + (iD / 2) ** 2) * 2) * 100) / 100
    return outer_diameter

def compute_coil_length(oD, iD, T):
    length = round(((math.pi * (oD**2 - iD**2)) / (4 * T)) * 100) / 100
    return length

def convert_to_imperial(value, from_metric=True):
    """ Convert between metric (mm) and imperial (inches) """
    if from_metric:
        return value / 25.4
    else:
        return value * 25.4

def main():
    unit_system = input("Do you want to use 'metric' (mm) or 'imperial' (inches)? Enter 'M' for metric or 'I' for imperial: ").strip().upper()

    operation = input("Do you want to calculate 'length' or 'outer diameter'? Enter 'L' for length, 'OD' for outer diameter: ").strip().upper()

    if unit_system.upper() == 'M':
        unit = "mm"
        conversion_needed = True
    elif unit_system.upper() == 'I':
        unit = "inches"
        conversion_needed = False
    else:
        print("Invalid unit system. Please enter 'M' for metric or 'I' for imperial.")
        return

    if operation.upper() == 'OD':
        L = float(input(f"Enter the coil length (L) in {unit}: "))
        iD = float(input(f"Enter the inner diameter (iD) in {unit}: "))
        T = float(input(f"Enter the coil thickness (T) in {unit}: "))

        if conversion_needed:
            L = convert_to_imperial(L, from_metric=True)
            iD = convert_to_imperial(iD, from_metric=True)
            T = convert_to_imperial(T, from_metric=True)

        outer_diameter = compute_coil_outer_diameter(L, iD, T)

        if conversion_needed:
            outer_diameter = convert_to_imperial(outer_diameter, from_metric=False)

        print(f"The outer diameter of the coil is: {outer_diameter} {unit}")

    elif operation.upper() == 'L':
        oD = float(input(f"Enter the outer diameter (oD) in {unit}: "))
        iD = float(input(f"Enter the inner diameter (iD) in {unit}: "))
        T = float(input(f"Enter the coil thickness (T) in {unit}: "))

        if conversion_needed:
            oD = convert_to_imperial(oD, from_metric=True)
            iD = convert_to_imperial(iD, from_metric=True)
            T = convert_to_imperial(T, from_metric=True)

        length = compute_coil_length(oD, iD, T)

        if conversion_needed:
            length = convert_to_imperial(length, from_metric=False)

        print(f"The coil length is: {length} {unit}")

    else:
        print("Invalid operation. Please enter 'L' for length or 'OD' for outer diameter.")

if __name__ == "__main__":
    main()