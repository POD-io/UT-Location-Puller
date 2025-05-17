import subprocess
import re

def get_locations(slot_name, port, exe_path, password=None):
    connect_string = f"archipelago://{slot_name}:{password if password else 'None'}@archipelago.gg:{port}"
    
    return [
        line.strip() for line in subprocess.run(
            f'"{exe_path}" "Universal Tracker" -- --nogui --list {connect_string}',
            shell=True, capture_output=True, text=True
        ).stdout.split('\n')
        if line.strip()
		# If non-location data is returned, add to filtering below
		
        and not re.search(r'adding \d+ filler items', line.lower())
        and not any(x in line for x in [
            '[', 'Archipelago', 'Connecting', 'Connected', 'Skipping', 'host', 'Warning'
        ])
    ]


# Add/change your info below ---
slot_name = "SlotName"
port = 12345
exe_path = r"\Archipelago\ArchipelagoLauncherDebug.exe"
password = None  # Change to "YourPasswordHere" if server has a password, otherwise change to None

locations = get_locations(slot_name, port, exe_path, password)

# Uncomment below for your desired output

### PRINT IN TERMINAL ###
for location in locations:
    print(location)

### WRITE TO FILE ###
# with open("locations.txt", "w", encoding="utf-8") as f:
#     for location in locations:
#         f.write(location + "\n")
