#%% LAB 4  ENCMP 100 Computer Programming for Engineers
#
# Student name: Savva Kosse
# Student CCID: kosse
# Others:
#       Savva Kosse 100%
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
#%% DECODE  Steganography, Detecting and Decoding a Secret Message
#
# Steganography has been used over millennia to hide information in
# plain sight. This assignment concerns the determination of a secret
# message, about an international rescue, from a list of university
# phone numbers. Each student writes a script to detect if a number
# likely represents a message and, if so, to decode the secret.
#
# Copyright (c) 2024, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
#%%

import scipy.io as io
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

def load_tsp_data():
    """
    Loads TSP data from tspData.mat file.
    
    Returns:
        list: TSP database if successful
    
    Side effects:
        - Prints error message and exits if file not found or loading fails
    """
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'tspData.mat')
        tsp = io.loadmat(file_path, squeeze_me=True)
        return np.ndarray.tolist(tsp['tsp'])
    except FileNotFoundError:
        print("Error: 'tspData.mat' file not found. Make sure it's in the same directory as this script.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        sys.exit(1)

def print_about():
    """
    Prints contents of tspAbout.txt file.
    
    Side effects:
        - Prints file contents or error message to console
    """
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'tspAbout.txt')
        with open(file_path, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("Error: 'tspAbout.txt' file not found.")
    except Exception as e:
        print(f"An error occurred while reading the about file: {e}")
    print()

def menu():
    """
    Displays main menu and gets user choice.
    
    Returns:
        int: User's menu choice (0-3)
    
    Side effects:
        - Prints menu options
        - Prompts for user input
    """
    print("MAIN MENU")
    print("0. Exit program")
    print("1. Print database")
    print("2. Limit dimension")
    print("3. Plot one tour")
    print()
    
    while True:
        try:
            choice = int(input("Choice (0-3)? "))
            if 0 <= choice <= 3:
                return choice
            print("Please enter a number between 0 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def tspPrint(tsp):
    """
    Prints the TSP database contents.
    
    Args:
        tsp (list): The TSP database
    
    Side effects:
        - Prints formatted database information to console
    """
    print("\nNUM  FILE NAME  EDGE TYPE  DIMENSION  COMMENT")
    for k in range(1, len(tsp)):
        name = tsp[k][0]
        edge = tsp[k][5]
        dimension = tsp[k][3]
        comment = tsp[k][2]
        print("%3d  %-9.9s  %-9.9s  %9d  %s"
              % (k, name, edge, dimension, comment))

def tspMinMax(tsp):
    """
    Calculates the minimum and maximum dimensions in the TSP database.
    
    Args:
        tsp (list): The TSP database
    
    Returns:
        tuple: (min_dimension, max_dimension)
    """
    dimensions = [record[3] for record in tsp[1:]]  # Skip header
    return min(dimensions), max(dimensions)

def tspLimit(tsp):
    """
    Filters the TSP database based on a user-specified dimension limit.
    
    Args:
        tsp (list): The TSP database (passed by reference)
    
    Side effects:
        - Prints min/max dimensions
        - Prompts for user input
        - Modifies tsp list by removing records exceeding limit
    """
    min_dim, max_dim = tspMinMax(tsp)
    print(f"Min dimension: {min_dim}")
    print(f"Max dimension: {max_dim}")
    
    while True:
        try:
            limit = int(input("Limit value? "))
            if min_dim <= limit <= max_dim:
                break
            print(f"Please enter a value between {min_dim} and {max_dim}")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Keep header and filter records
    tsp[:] = [tsp[0]] + [record for record in tsp[1:] if record[3] <= limit]

def plotEuc2D(coord, comment, name):
    """
    Creates a plot for a EUC_2D type TSP tour.
    
    Args:
        coord (ndarray): Coordinates of cities
        comment (str): Tour comment for title
        name (str): Tour name for legend
    
    Side effects:
        - Creates and displays plot
        - Saves plot to tspPlot.png
    """
    x = coord[:, 0]
    y = coord[:, 1]

    plt.figure(figsize=(10, 10))
    
    # Plot points and connecting lines
    plt.scatter(x, y, c='blue', s=50, zorder=2)
    for i in range(len(x) - 1):
        plt.plot([x[i], x[i+1]], [y[i], y[i+1]], c='blue', zorder=1)
    
    # Plot final connection in red
    plt.plot([x[-1], x[0]], [y[-1], y[0]], c='red', zorder=1)
    
    plt.title(comment)
    plt.plot([], [], c='blue', label=name)
    plt.scatter([], [], c='blue', s=5, label='')
    
    # Use automatic legend placement
    plt.legend(loc='best', framealpha=0.9, edgecolor='black')
    
    plt.xlabel('x-Coordinate')
    plt.ylabel('y-Coordinate')
  
    
    plt.savefig('tspPlot.png', bbox_inches='tight', dpi=300)
    plt.show()
    plt.close()
    print("See tspPlot.png")

def tspPlot(tsp):
    """
    Handles the plotting of a selected tour.
    
    Args: tsp (list): The TSP database
    
    Side effects:
        - Prompts for user input
        - Calls plotEuc2D for EUC_2D type tours
    """
    while True:
        try:
            num = int(input("Number (EUC_2D)? "))
            if 1 <= num < len(tsp):
                break
            print(f"Please enter a number between 1 and {len(tsp)-1}")
        except ValueError:
            print("Invalid input. Please enter a number.")

    tour = tsp[num]
    if tour[5] != 'EUC_2D':
        print(f"Invalid ({tour[5]})!!!")
        return
    
    plotEuc2D(tour[10], tour[2], tour[0])

def main():
    tsp = load_tsp_data()
    print_about()
    
    while True:
        choice = menu()
        if choice == 0:
            break
        elif choice == 1:
            tspPrint(tsp)
        elif choice == 2:
            tspLimit(tsp)
        elif choice == 3:
            tspPlot(tsp)
        print()

if __name__ == "__main__":
    main()