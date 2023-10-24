def combine_formworks(width, height, formworks):
    def recursive_search(w, h, combination):
        if w == 0 and h == 0:
            return [combination]

        if w < 0 or h < 0:
            return []

        combinations = []
        for formwork, (formwork_width, formwork_height) in formworks.items():
            new_combination = combination.copy()
            temp_w, temp_h = w, h
            
            # Try to use the formwork as many times as possible until it exceeds the height or width
            while temp_w >= formwork_width and temp_h >= formwork_height:
                temp_w -= formwork_width
                temp_h -= formwork_height
                new_combination[formwork] = new_combination.get(formwork, 0) + 1
                combinations.extend(recursive_search(temp_w, temp_h, new_combination))

        return combinations

    return recursive_search(width, height, {})

formworks = {
    'T1': (2.5, 3.5),
    'T2': (1.25, 3.5),
    'T3': (1.0, 3.5),
    'T4': (0.75, 3.5),
    'T5': (0.5, 3.5),
    'T6': (0.25, 3.5),
    'T7': (2.5, 3.0),
    'T8': (1.25, 3.0),
    'T9': (1.0, 3.0),
    'T10': (0.75, 3.0),
    'T11': (0.5, 3.0),
    'T12': (0.25, 3.0),
    'T13': (2.5, 1.25),
    'T14': (1.25, 1.25),
    'T15': (1.0, 1.25),
    'T16': (0.75, 1.25),
    'T17': (0.5, 1.25),
    'T18': (0.25, 1.25),
    'T19': (2.5, 1.0),
    'T20': (1.25, 1.0),
    'T21': (2.5, 0.75),
    'T22': (1.25, 0.75),
    'T23': (2.5, 0.5),
    'T24': (1.25, 0.5),
    'T25': (2.5, 0.25),
    'T26': (1.25, 0.25)
}

if __name__ == '__main__':
    width = float(input("Please enter the wall's width in meters: "))
    height = float(input("Please enter the wall's height in meters: "))

    combinations = combine_formworks(width, height, formworks)
    
    if not combinations:
        print("There are no possible formwork combinations for this wall size.")
        exit()

    # Sort combinations by the number of formwork pieces
    best_combinations = sorted(combinations, key=lambda x: sum(x.values()))

    for idx, combination in enumerate(best_combinations[:3], 1):  # The first 3 combinations
        print(f"\nOption {idx}:")
        for formwork, quantity in combination.items():
            print(f"Formwork: {formwork}, Quantity: {quantity}")

