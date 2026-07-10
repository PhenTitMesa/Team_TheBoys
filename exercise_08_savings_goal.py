weekly_savings = 50
weeks = 12
one_time_purchase = 100

total_saved = weekly_savings * weeks
remaining = total_saved - one_time_purchase

print(f"Saving ${weekly_savings} per week for {weeks} weeks.")
print(f"Total saved: ${total_saved}")
print(f"After a ${one_time_purchase} purchase, you have ${remaining} left")
