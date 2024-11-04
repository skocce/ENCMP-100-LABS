#%% LAB 3  ENCMP 100 Computer Programming for Engineers
#
# Student name:Savva Kosse
# Student CCID: 1863937
# Others:
#    Savva Kosse 100%
#
# To avoid plagiarism, list the names of others, Version 0 author(s)
# aside, whose code, words, ideas, images, or data you incorporated.
# To avoid unauthorized collaboration, list all others, excluding
# lab instructor and TAs, who gave compositional assistance.
#
# After each name, including your own name, enter in parentheses an
# estimate of the source's contributions in percent. Supply these
# numbers, which must add to 100%, to receive a nonzero mark.
#
# For obscure and anonymous or known and non-human sources, enter
# pseudonyms or names in uppercase, e.g., DARKWEB or CHATGPT, followed
# by percentages. Send one email to the lab instructor with copies of
# obscure and anonymous sources when you submit your assignment.
#
# Copyright (c) 2024, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
import matplotlib.pyplot as plt
import numpy as np
#%% Version 2
# User input section
initial_savings = float(input("Please enter the initial savings amount :"))
monthly_contribution = float(input("Please enter the monthly contribution :"))
annual_interest_rate = float(input("Please enter the annual savings interest rate :"))

# User Input Section
program_choice = int(input("Select a University program: 1 = Arts, 2 = Science, 3 = Engineering: "))


# Assign tuition cost based on user's choice
if program_choice == 1:
    initial_tuition = 5550  # Arts tuition
    faculty="Arts"
elif program_choice == 2:
    initial_tuition = 6150  # Science tuition
    faculty="Science"
elif program_choice == 3:
    initial_tuition = 6550  # Engineering tuition
    faculty="Engineering"
else:
    print('Input 1 or 2 or 3')
    
inetrest_rate = annual_interest_rate /100
monthly_interest_rate = inetrest_rate / 12  # monthly interest rate
years = 18
months = years * 12  # total number of months for 18 years
tuition_increase_rate = 0.07  # 7% annual tuition increase

# List to store savings at the end of each month
savings_balance = []

# Resetting the balance for recalculation
current_balance = initial_savings

# Calculate savings growth month by month
for month in range(1, months):
    interest_gained = current_balance * monthly_interest_rate  # explicitly calculate interest
    current_balance += interest_gained + monthly_contribution  # update balance
    savings_balance.append(current_balance)
    

# Calculate the tuition cost at year 18 to 21
tuition_fee = initial_tuition

for year in range(18):
    tuition_fee += tuition_fee * tuition_increase_rate  # Compounded annually

total_tuition_cost = 0
for year in range(4):  # Calculate for the 4-year program (years 18 to 21)
    total_tuition_cost += tuition_fee
    tuition_fee += tuition_fee * tuition_increase_rate  # Increase every year


# Output results for savings and tuition
print(f"The amount saved is ${current_balance:.2f}")

print(f"The cost of the {faculty} program is: ${total_tuition_cost:.2f}")

#%% Chech for got enouh money or not and output coorect gragh

# Check if the savings balance is enough to cover tuition
if current_balance >= total_tuition_cost:
    print("Congratulations!!! You have enough saved for the program.")
    # Plotting Section
    years_range = np.linspace(0, years, len(savings_balance))  # years on x-axis
    plt.plot(years_range, savings_balance, label="Savings Balance")
    plt.axhline(y=total_tuition_cost, color='orange', label=faculty)

    # Annotating the plot
    plt.title('Savings vs Tuition')
    plt.xlabel('Years')
    plt.ylabel('Amount $')
    plt.legend()
    plt.xticks(range(0,19))
    # Display the plot
    plt.show()
else:
    print(f"Unfortunately!!! You do not have enough saved for the {faculty} program.")
    
    # Calculate optimal monthly contribution if savings are not enough
    optimal_contribution = 1  # Start with $1 monthly contribution
    new_savings_balance = initial_savings
    new_savings_balance_list = []

    # Instead of break, control the loop using the condition itself
    while new_savings_balance < total_tuition_cost:
        # Reset savings balance for the new calculation
        new_savings_balance = initial_savings
        new_savings_balance_list = []  # Reset the list for recalculation
        
        # Recalculate savings for 18 years with the current 'optimal_contribution'
        for month in range(1, months):  # 18 years, 12 months each
            new_savings_balance += new_savings_balance * monthly_interest_rate + optimal_contribution
            new_savings_balance_list.append(new_savings_balance)
        
        # Only increment optimal_contribution if not enough savings yet
        if new_savings_balance < total_tuition_cost:
            optimal_contribution += 1

        
    # Output the optimal monthly contribution
    print(f"The optimal monthly contribution amount is ${optimal_contribution}.")
    
    # (Plotting code here remains unchanged)


    # Plotting Section
    years_range = np.linspace(0, years, len(savings_balance))  # years on x-axis
    plt.plot(years_range, savings_balance, label="Savings Balance")
    plt.plot(years_range, new_savings_balance_list,color='green' ,label="Updated Saving Balance")  # Use the updated list here
    plt.axhline(y=total_tuition_cost, color='orange', label=faculty)
    
    
    # Annotating the plot
    plt.title('Savings vs Tuition')
    plt.xlabel('Years')
    plt.ylabel('Amount $')
    plt.legend()
    plt.xticks(range(0,19))
    # Display the plot
    plt.show()