COLOUR_TO_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                   "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                   "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                   "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                   "aquamarine4": "#458b74", "azure1": "#f0ffff",
                   "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b",
                   "beige": "#f5f5dc", "bisque1": "#ffe4c4"}

COLOUR_TO_CODES = {k.lower(): v for k, v in COLOUR_TO_CODES.items()}  # Converts all keys to lower case

colour_name = input("Enter the colour name: ").lower()
while colour_name != "":
    try:
        print(f"The code for {colour_name} is {COLOUR_TO_CODES.get(colour_name)}")
        colour_name = input("Enter the colour name: ").lower()
    except AttributeError:
        print("Not a valid input")
        colour_name = input("Enter the colour name: ").lower()
