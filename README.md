I completed two Python challenges named PyBank and PyPoll, using the concepts and knowledge from lectures and activities in Module 3 of UPENN Data Science Bootcamp. For this project, I created a new repository called "Python-Challenge". Inside each folder, there is a Python scripting file named "main.py" to run each analysis, along with two sub-folders named Resources (which contain the Data CSV file) and Analysis (which contain the outcomes). 
I collaborated with my colleague in the study group, and I also used certain parts of code from this repository https://github.com/svafaeva93/python-challenge/tree/main to develop my algorithm and codes. Finally, I sought assistance from ChatGPT to make my code more descriptive and easier to understand.

Note for resubmission: I have modified the way of reading the CSV file by using the OS library instead of hardcoding the complete path. This was done as per the suggestion of the grader and Jake Byford. I highly appreciate their help!

A.	PyBank - Algorithm:
Step 1: Import modules for operating system and reading CSV file, by using “import os, import csv”
Step 2: Locate the Data CSV file by providing the csv_path either by csv_path = “/User/...” or csv_path = os.path.join(‘/User/…’)
Step 3: Define a function named analyze_budget_data() to analyze the budget
Inside the function 'analyze_budget_data()', please ensure the following tasks are performed:
Step 3.1: Initialize variables: Month_Count = 0, Total_Revenue = 0, Previous_Revenue = 0, Total_Revenue_Change = 0. Create empty lists Revenue_Change_List and Month_Change_List.
Step 3.1: Read the Data CSV file, skip the first row of the CSV file if it contains the header
Step 3.2: Use a FOR-loop to iterate through rows of data, updating the Month_Count and retrieving the Current_Revenue for each row, then calculate Total_Revenue by adding Current_Revenue to it.
Step 3.3: In each row, if Previous_Revenue isn’t zero, calculate the revenue change as the difference between Current_Revenue and Previous_Revenue. Then, update Revenue_Change_List and Month_Change_List. Calculate Total_Revenue_Change by adding Current_Revenue. Finally, update Previous_Revenue with the value of Current_Revenue for the next iteration.
Step 3.4: Outside of the FOR-loop, calculate the average change
Step 3.5: Find max increase and max decrease in profits/loses
Step 3.6: Generate the summary table
Step 3.7: Write the summary table into an output file
Step 4: Call the function analyze_budget_data() to analyze the budget
B.	PyPoll Algorithm: 
Step 1: Import modules for operating system and reading CSV file, by using “import os, import csv”
Step 2: Locate the Data CSV file by providing the csv_path either by csv_path = “/User/...” or csv_path = os.path.join(‘/User/…’)
Step 3: Initialize dictionaries to store the candidate's name, number of votes, and percentages. Also, initialize the Total_Votes
Step 4: Open and retrieve data from file with csv_path
Step 5: Using the 1st FOR-loop to iterate through rows of data from the header
	Step 5.1: Increase the total votes by 1 for each candidate in the row and record their names.
	Step 5.2: Check if the candidate’s name is in the Candidate_Votes dictionary. If yes, add 1 to Candidate_Votes. If no, set Candidate_Votes to 1.
Step 6: Using the 2nd FOR-loop to calculate and store candidate’s percentage, round the percentage to 3 decimal places
Step 7: Find the winner by using function max()
Step 7: Write the outcome into an output file

