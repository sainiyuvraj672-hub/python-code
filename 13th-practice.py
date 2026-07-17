#compound intrest calculator

principle = 0
rate = 0
time =0

while principle <=0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("principle can't be negative or zero")

while rate <=0:
    rate = float(input("Enter the Intrest rate amount: "))
    if rate <= 0:
        print("Intrest rate can't be negative or zero")

while time <=0:
    time = int(input("Enter the time: "))
    if time <= 0:
        print("time can't be negative or zero")

print(principle)

print(rate)

print(time)

total = principle * pow(1 + rate/100 ,time)

print(f"Balance after {time} year/s: ${total:.2f}")
