#Loop for getting rainfall for months and totals
def get_rainfall():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
#Get the number of years
    years = int(input("Enter the number of years: "))
    total_rainfall = 0
    total_months = years * 12
#Loop through each year and month
    for year in range(1, years + 1):
        print(f"\nFor year {year}:")
        for month in months:
            while True:
                try:
                    rainfall = float(input(f"Enter the rainfall amount for {month}: "))
                    if rainfall < 0:
                        print("Rainfall cannot be negative. Please enter a valid amount.")
                        continue
                    total_rainfall += rainfall
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
#Calculate average monthly rainfall
    average_rainfall = total_rainfall / total_months
#Display results
    print(f"\nFor {total_months} months:")
    print(f"Total rainfall: {total_rainfall:.2f} inches")
    print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
#Call back to function
get_rainfall()