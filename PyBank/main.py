import os
import csv

# Locate the CSV file
csv_path = os.path.join("Resources", "budget_data.csv")

# Output file path
output_file = os.path.join("Analysis", "result.txt")

# -------- Subroutine to analyze the budget data ------------
def analyze_budget_data(csv_path):
    # Initialize variables
    Month_Count = 0
    Total_Revenue = 0
    Previous_Revenue = 0
    Total_Revenue_Change = 0
    Revenue_Change_List = []
    Month_Change_List = []
    
    # Read CSV file
    with open(csv_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)
        
        # Iterate through rows of data after the header
        for row in csvreader:
            Month_Count += 1
            Current_Revenue = int(row[1])
            Total_Revenue += Current_Revenue

            # Calculate revenue change. Must check whether the previous revenue is ZERO or not
            if Previous_Revenue != 0:
                Revenue_Change = Current_Revenue - Previous_Revenue
                Revenue_Change_List.append(Revenue_Change)
                Month_Change_List.append(row[0])
                Total_Revenue_Change += Revenue_Change

            # Update previous revenue for the next iteration
            Previous_Revenue = Current_Revenue

        # Calculate average change
        Avg_Change = Total_Revenue_Change / (Month_Count - 1)

        # Find maximum increase and decrease in Profists/Losts
        Max_Increase = max(Revenue_Change_List)
        Max_Increase_Month = Month_Change_List[Revenue_Change_List.index(Max_Increase)]
        Max_Decrease = min(Revenue_Change_List)
        Max_Decrease_Month = Month_Change_List[Revenue_Change_List.index(Max_Decrease)]

    # Generate Summary Table 
    Summary_Table = (
        f"\nFinancial Analysis\n"
        f"--------------------------------------------------------------------\n"
        f"Total Months: {Month_Count}\n"
        f"Total: ${Total_Revenue}\n"
        f"Average Change: ${Avg_Change:.2f}\n"
        f"Greatest Increase in Profits: {Max_Increase_Month} (${Max_Increase})\n"
        f"Greatest Decrease in Profits: {Max_Decrease_Month} (${Max_Decrease})\n"
    )
    # Print output to the screen
    #print(Summary_Table)

    # Write Summary Table to an output file
    with open(output_file, "w") as resultfile:
        resultfile.write(Summary_Table)

# Call a function analyze_budget_data() to analyze the budget data
analyze_budget_data(csv_path)  
