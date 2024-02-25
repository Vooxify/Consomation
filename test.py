psu_quality = input(
    'What is your PSU label? ("80+ Bronze", "80+ Silver", "80+ Gold", "80+ Platinum", "80+ Titanium"): ').lower()

while True:
    labels = {
        "80+ Bronze".lower(): 88,
        "80+ Silver".lower(): 90,
        "80+ Gold".lower(): 92,
        "80+ Platinum".lower(): 94,
        "80+ Titanium".lower(): 96,
    }

    if psu_quality in labels:
        psu_percentage = (labels[psu_quality] / 100 - 1) * (-1) + 1
        print(round(psu_percentage, 2))
        break
    else:
        psu_quality = input('Invalid input. Please enter a valid PSU label: ').lower()
