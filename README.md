This is a lightweight integration for pulling the current list of accessible locations via the LauncherDebug.exe CLI from a running Archipelago session.

This Python script uses subprocess to call the Archipelago Launcher in UT mode with the --list flag, parses the output, and filters out non-location lines. 
You can print the results to the terminal or write them to a file.

To use:
Replace slot_name, port, and exe_path with your own.
Leave password as 'None', or add your password in quotes if server has one.
Run the script after the AP session is active.
Comment/uncomment the sections for terminal output and writing to a file as desired.

Optional: Hook it into a live display, Discord bot, etc..

The current version looks at servers running on archipelago.gg, but can be easily adjusted for local servers.

Format: ArchipelagoLauncherDebug.exe "Universal Tracker" -- --nogui --list archipelago://[slot]:[password or 'None']@archipelago.gg:[port]
Example: ArchipelagoLauncherDebug.exe "Universal Tracker" -- --nogui --list archipelago://MyOuterWildsSlot:None@archipelago.gg:12345
