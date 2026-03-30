tasks = [
    {"action": "Write Email", "time_minutes": 10},
    {"action": "Social Media Post", "time_minutes": 30},
    {"action": "Complete Marketing Strategy", "time_minutes": 120},
    {"action": "Check Comments", "time_minutes": 5}
]

print("Agent is analyzing tasks...")

for task in tasks:
    if task["time_minutes"] > 20:
        print(f"Priority task : {task["action"]}")
    else:
        print(f"Quick Task: {task["action"]}")
