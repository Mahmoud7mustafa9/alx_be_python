
task = input('Enter your task: ')
priority = input('Priority (high/medium/low): ')
time = input ('Is it time-bound? (yes/no): ')
match priority:
    case "high":
        if time.lower() == "yes":
            print (f'Reminder: {task} is a high priority task that requires immediate attention today!')
        else:
            print(f'Note: {task} is a high priority task. Consider completing it when you have free time.') 

    case "medium" :
        if time.lower() == "yes":
            print ( f'Reminder: {task} is a medium priority task that requires immediate attention today!')
        else:
            print (f'Note: {task} is a medium priority task. Consider completing it when you have free time.')
    case "low" :
        if time.lower() == "yes":
            print(f'Reminder: {task} is a low priority task that requires immediate attention today!')
        else:
            print (f'Note: {task} is a low priority task. Consider completing it when you have free time.')