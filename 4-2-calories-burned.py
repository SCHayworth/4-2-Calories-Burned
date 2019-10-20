# Program 4-2 Calories Burned
# Shaun Hayworth
# CIS 2
# 10-20-2019
# Original source code and revision history can be found at https://github.com/SCHayworth/4-2-Calories-Burned

# Calculates the number of calories burned on a treadmill given a rate of 4.2 calories per
# minute, and displays the total number of calories burned in 5 minute intervals,
# beginning at 10 minuts and ending at 30.

# Initialize CALORIES_PER_MINUTE constant
# Change this value for a different treadmill.
CALORIES_PER_MINUTE = 4.2

# Print the calories burned every 5 minutes beginning at 10 and ending at 30
for minute in range(10, 31, 5):

    # Multiply CALORIES_PER_MINUTE by the current minute
    calories_burned = minute * CALORIES_PER_MINUTE

    # Display the current total calories burned and the current time in minutes
    print(f'You have burned {calories_burned:.1f} in {minute} minutes!')
