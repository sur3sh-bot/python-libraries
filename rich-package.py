from rich.console import Console
from rich.table import Table
from rich.progress import track
import time

console = Console()


table = Table(title="🚀 Space Mission Logistics")

table.add_column("Resource", style="cyan", no_wrap=True)
table.add_column("Status", style="magenta")
table.add_column("Quantity", justify="right", style="green")

table.add_row("Liquid Oxygen", "Stable", "15,000L")
table.add_row("Dehydrated Pizza", "Low Stock", "42 Units")
table.add_row("Robot Morale", "Slightly Grumpy", "88%")

console.print(table)


def simulate_launch():
    console.print("\n[bold yellow]Initiating Launch Sequence...[/bold yellow]")
    # The 'track' function automatically adds a progress bar to any loop
    for step in track(range(100), description="Calculating Trajectory:"):
        time.sleep(0.05) 
    
    console.print("[bold green]✔ Lift off! We have clear skies.[/bold green] 🌌")

simulate_launch()