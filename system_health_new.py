import psutil

def monitor_resource(name, current_value):
    """Generic function to handle threshold logic."""
    try:
        threshold = int(input(f"Enter {name} threshold %: "))
        print(f"Current {name} %: {current_value}")
        
        if current_value >= threshold:
            print(f"⚠️  {name} Usage is High, Action required")
        else:
            print(f"✅ {name} usage is Good, Relax")
        print("-" * 30)
    except ValueError:
        print("Invalid input. Please enter a number.")

def run_checks():
    # 1. CPU Check (interval=1 is good for an accurate reading)
    monitor_resource("CPU", psutil.cpu_percent(interval=1))
    
    # 2. Disk Check
    monitor_resource("Disk", psutil.disk_usage('/').percent)
    
    # 3. Memory Check
    monitor_resource("Memory", psutil.virtual_memory().percent)

if __name__ == "__main__":
    run_checks()
