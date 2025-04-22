# Keep Teams Active Script

A simple Python script to periodically simulate keyboard input (pressing the Shift key by default) to prevent Microsoft Teams (and the underlying OS) from detecting you as idle and changing your status away from "Available" (green).

**Disclaimer:** This script simulates user input. While designed to be minimally intrusive, it *could* potentially interfere with precise user actions if the timing coincides. Use responsibly and check your organization's policies on such tools. It may require accessibility permissions on your OS.

## Setup and Installation

You need Python 3 installed on your system.

### Clone the project
```bash
git clone git@github.com:Mikasathebest/keep_teams_active.git
```
### Option A: Using `venv` (Built-in)

1.  **Navigate to Project Directory:**
    ```bash
    cd /path/to/keep_teams_active
    ```
2.  **Create Virtual Environment:**
    ```bash
    python3 -m venv keep_teams_active
    ```
3.  **Activate Virtual Environment:**
    ```bash
    source keep_teams_active/bin/activate
    # On Windows (Git Bash/WSL): source keep_teams_active/Scripts/activate
    # On Windows (CMD): keep_teams_active\Scripts\activate.bat
    # On Windows (PowerShell): keep_teams_active\Scripts\Activate.ps1
    ```
    Your terminal prompt should now show `(keep_teams_active)`.
4.  **Install Requirements:**
    ```bash
    pip install -r requirements.txt
    ```

### Option B: Using `uv` (Faster Alternative)

1.  **Install `uv`:** Follow instructions at [astral.sh/uv](https://astral.sh/uv) (e.g., `curl -LsSf https://astral.sh/uv/install.sh | sh`).
2.  **Navigate to Project Directory:**
    ```bash
    cd /path/to/your/script/folder
    ```
3.  **Create and Activate Virtual Environment:**
    ```bash
    uv venv keep_teams_active
    source keep_teams_active/bin/activate
    # On Windows: keep_teams_active\Scripts\activate
    ```
    Your terminal prompt should now show `(keep_teams_active)`.
4.  **Install Requirements:**
    ```bash
    uv pip install -r requirements.txt
    ```

## Running the Script

1.  **Activate Environment:** Make sure your virtual environment (`keep_teams_active`) is activated.
2.  **Run:**
    ```bash
    python keep_teams_active.py
    ```
3.  **Stop:** Press `Ctrl+C` in the terminal where the script is running.

## Keeping the Script Running on macOS (Background)

To keep the script running even after closing the terminal window or logging out, you can use one of these methods:

### Method 1: `nohup` (Simple Background Task)

Good for simple cases, logs output to `nohup.out`.

1.  **Activate Environment:** `source venv/bin/activate` (or `.venv/bin/activate`)
2.  **Run with `nohup`:**
    ```bash
    nohup python keep_teams_active.py &
    ```
    * `nohup`: Prevents the script from stopping when you close the terminal.
    * `&`: Runs the script in the background.
3.  **To Stop:** Find the process ID (PID) and kill it:
    ```bash
    ps aux | grep keep_teams_active.py # Find the PID (ignore the grep process itself)
    kill <PID> # Replace <PID> with the actual process ID
    ```

### Method 2: `tmux` or `screen` (Terminal Multiplexer)

Allows you to detach the session running the script and reattach later.

1.  **Install (if needed):** `brew install tmux` or `brew install screen`
2.  **Start Session:** `tmux` (or `screen`)
3.  **Inside the session:**
    * Activate Environment: `source venv/bin/activate`
    * Run script: `python keep_teams_active.py`
4.  **Detach:**
    * `tmux`: Press `Ctrl+b` then `d`.
    * `screen`: Press `Ctrl+a` then `d`.
5.  **Reattach:** `tmux attach` (or `screen -r`)
6.  **To Stop:** Reattach, then press `Ctrl+C` in the script's terminal.

### Method 3: `launchd` (macOS Native Service)

The most robust method for running background tasks automatically, including starting on login.

1.  **Find Python Path:** Activate your virtual environment (`source venv/bin/activate`) and run `which python`. Copy this full path (e.g., `/path/to/your/script/folder/venv/bin/python`).
2.  **Find Script Path:** Get the absolute path to `keep_teams_active.py` (e.g., `/path/to/your/script/folder/keep_teams_active.py`).
3.  **Create `.plist` File:** Create a file named `com.user.keepteamsactive.plist` (you can choose a different name) in `~/Library/LaunchAgents/`.

    *Example `~/Library/LaunchAgents/com.user.keepteamsactive.plist`:*
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd](http://www.apple.com/DTDs/PropertyList-1.0.dtd)">
    <plist version="1.0">
    <dict>
        <key>Label</key>
        <string>com.user.keepteamsactive</string> <key>ProgramArguments</key>
        <array>
            <string>/path/to/your/script/folder/venv/bin/python</string>
            <string>/path/to/your/script/folder/keep_teams_active.py</string>
        </array>

        <key>RunAtLoad</key>
        <true/> <key>KeepAlive</key>
        <true/> <key>StandardOutPath</key>
        <string>/tmp/keepteamsactive.stdout.log</string> <key>StandardErrorPath</key>
        <string>/tmp/keepteamsactive.stderr.log</string> <key>WorkingDirectory</key>
        <string>/path/to/your/script/folder</string> </dict>
    </plist>
    ```
    **Important:** Replace the placeholder paths with your actual paths from steps 1 and 2. Make sure the `WorkingDirectory` is also correct.

4.  **Load the Service:**
    ```bash
    launchctl load ~/Library/LaunchAgents/com.user.keepteamsactive.plist
    ```
    The script should now start and run in the background. It will also start automatically when you log in.

5.  **To Stop/Unload:**
    ```bash
    # Stop the service temporarily
    launchctl stop com.user.keepteamsactive

    # Unload the service permanently (won't start on next login)
    launchctl unload ~/Library/LaunchAgents/com.user.keepteamsactive.plist
    ```
6.  **To Start Manually (if loaded but not running):**
    ```bash
    launchctl start com.user.keepteamsactive
    ```

Choose the method that best suits your needs for persistence. `launchd` is generally recommended for long-term background operation on macOS.