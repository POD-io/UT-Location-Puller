This is a lightweight integration for pulling the current list of accessible locations via the LauncherDebug.exe CLI from a running Archipelago session.

This Python script uses subprocess to call the Archipelago Launcher in UT mode with the --list flag, parses the output, and filters out non-location lines. 
You can print the results to the terminal or write them to a file.

To use:
Replace slot_name, port, and exe_path with your own.
Run the script after the AP session is active.

Optional: Hook it into a live display, Discord bot, etc.
