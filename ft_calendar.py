from datetime import datetime

def count_days_until_christmas():
    today = datetime.today()
    christmas_date = datetime(today.year, 12, 25)
    
    if today > christmas_date:
        christmas_date = datetime(today.year + 1, 12, 25)
    
    delta = christmas_date - today
    return delta.days

print(f"Il reste {count_days_until_christmas()} jours avant Noël ! 🎄")
