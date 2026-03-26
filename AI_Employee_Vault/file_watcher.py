"""
Car Markaz — AI Employee File Watcher
Owner: Sheikh Ali Kabir
Version: 1.0

This script watches the Inbox/ folder.
When a new .md file appears, it automatically triggers Claude Code.
"""

import time
import shutil
import logging
import threading
import subprocess
from pathlib import Path
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ============================================================
# CONFIGURATION — Only make changes here
# ============================================================
VAULT_ROOT = Path(r"E:\Agentic_PIAIC\Bronze_Tier\AI_Employee_Vault")
CLAUDE_COMMAND = "claude"
WATCH_EXTENSION = ".md"
# ============================================================

INBOX = VAULT_ROOT / "Inbox"
NEEDS_ACTION = VAULT_ROOT / "Needs_Action"
LOGS = VAULT_ROOT / "Logs"

# Thread lock — only one file will be processed at a time
processing_lock = threading.Lock()

# Setup logging — outputs to terminal + daily log file
def get_log_file():
    LOGS.mkdir(exist_ok=True)
    return LOGS / f"{datetime.now().strftime('%Y-%m-%d')}.md"

def setup_logging():
    log_file = get_log_file()
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s — %(message)s",
        datefmt="%H:%M:%S",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_file, encoding="utf-8")
        ]
    )

def log(message):
    logging.info(message)
    # Also write in Obsidian-friendly log format
    log_file = get_log_file()
    timestamp = datetime.now().strftime("%H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


class InboxHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return

        src = Path(event.src_path)

        # Only process .md files
        if src.suffix.lower() != WATCH_EXTENSION:
            log(f"SKIP: Non-.md file ignored — {src.name}")
            return

        # Ignore the template file
        if src.name == "TASK_TEMPLATE.md":
            return

        # Wait for file write to complete
        time.sleep(0.8)

        # Acquire lock — avoid parallel processing
        with processing_lock:
            self.process_file(src)

    def process_file(self, src: Path):
        if not src.exists():
            log(f"ERROR: File already moved or deleted — {src.name}")
            return

        log(f"NEW TASK DETECTED: {src.name}")
        log(f"PROCESSING: Invoking Claude Code...")

        try:
            result = subprocess.run(
                [CLAUDE_COMMAND, "--print",
                 f"Process the task file '{src.name}' in Inbox/ folder. "
                 f"Follow instructions in CLAUDE.md exactly."],
                cwd=str(VAULT_ROOT),
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )

            if result.returncode == 0:
                log(f"SUCCESS: Task '{src.name}' successfully processed")
                log(f"CLAUDE OUTPUT: {result.stdout[:200]}...")
            else:
                log(f"ERROR: Claude exited with code {result.returncode}")
                log(f"STDERR: {result.stderr[:300]}")
                self.move_to_needs_action(src, reason=result.stderr)

        except subprocess.TimeoutExpired:
            log(f"TIMEOUT: Task '{src.name}' — 5 minute limit exceeded")
            self.move_to_needs_action(src, reason="Claude timeout — took more than 5 minutes")

        except FileNotFoundError:
            log(f"ERROR: Claude command not found. Check 'claude --version'.")
            self.move_to_needs_action(src, reason="Claude CLI not found on system")

        except Exception as e:
            log(f"UNEXPECTED ERROR: {str(e)}")
            self.move_to_needs_action(src, reason=str(e))

    def move_to_needs_action(self, src: Path, reason: str):
        """Move file to Needs_Action when an error occurs"""
        if not src.exists():
            return
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        dest = NEEDS_ACTION / f"ERROR_{timestamp}_{src.name}"
        try:
            shutil.move(str(src), str(dest))
            log(f"MOVED TO NEEDS_ACTION: {dest.name} — Reason: {reason[:100]}")
        except Exception as e:
            log(f"MOVE FAILED: {str(e)}")


def main():
    setup_logging()

    # Check required folders exist
    INBOX.mkdir(exist_ok=True)
    NEEDS_ACTION.mkdir(exist_ok=True)
    LOGS.mkdir(exist_ok=True)

    # Watcher setup
    handler = InboxHandler()
    observer = Observer()
    observer.schedule(handler, str(INBOX), recursive=False)
    observer.start()

    log("=" * 55)
    log("CAR MARKAZ — AI EMPLOYEE FILE WATCHER")
    log("Owner: Sheikh Ali Kabir")
    log(f"Watching: {INBOX}")
    log("Drop any .md file into Inbox/ to begin...")
    log("Press Ctrl+C to stop")
    log("=" * 55)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        log("File Watcher has been stopped.")
        log("Car Markaz AI Employee offline.")

    observer.join()


if __name__ == "__main__":
    main()
