import os
import sys


def inputs():

    hwh_price = float(input("How much does it cost per kWh ? (ex: 0.1121) "))
    played_hours = int(input("How many hour(s) you played ? "))
    watts_small_pieces = float(input("What is the consumption of your small components? (SSD, RAM, Wi-Fi Card, etc... --> NOT GPU OR CPU!) "))
    print("How much does your CPU and GPU consume?")
    cpu = float(input("CPU (Processor): "))
    gpu = float(input("GPU (Graphic Card): "))
    psu_quality = input('What is your PSU label? ("80+ Bronze", "80+ Silver", "80+ Gold", "80+ Platinum", "80+ Titanium"): ').lower()

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
            psu_percentage = round(psu_percentage, 2)
            break
        else:
            psu_quality = input('Invalid input. Please enter a valid PSU label: ').lower()

    return hwh_price, watts_small_pieces, cpu, gpu, psu_percentage, played_hours

def start_hwinfo():
    print("To calculate your GPU and CPU consumption, you need to start HWInfo.")
    start = input('Start it? (y/n) ').lower()
    if start == 'y':
        try:
            os.startfile("HWiNFO64.exe")
            print(
                "You need to play 45 mins at your favourite game\n"
                "And you take the maximum value of consummate of your CPU and GPU"
            )
        except OSError:
            print('You need to agree the admin privilege')
            sys.exit()
    elif start == 'n':
        print("The software has not started.")

def calculate_price():
    hwh_price, watts_small_pieces, cpu, gpu, psu_percentage, played_hour = inputs()
    total = watts_small_pieces + cpu + gpu
    with_loss = total * psu_percentage
    with_loss = int(round(with_loss, 0))

    convertion = with_loss / 1000

    print(f"Your PC consumes ≈ {with_loss} Watts or {convertion} kWH")

    price = convertion * hwh_price
    price = round(price, 2)

    print(f"You paid {price}€ / kWH")
    return price, with_loss, played_hour

def run():
    start_hwinfo()
    price, with_loss, played_hours = calculate_price()
    see_more = input("You want to see more ? (y/n) ").lower()
    if see_more == "y":
        print(
            f"{with_loss}W by {played_hours} hour : {price * played_hours}€\n"
            f"{with_loss}W by {played_hours} hour by a week : {(price * played_hours) * 7}€\n"
            f"{with_loss}W by {played_hours} hour by an year : {(price * played_hours) * 365}€"
        )
    else:
        sys.exit()

if __name__ == '__main__':
    run()
    input()
