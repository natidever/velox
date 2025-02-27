import subprocess
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.bot_process = None
        self.start_bot()

    def start_bot(self):
        """Start the Telegram bot process."""
        logger.info("Starting Telegram bot...")
        self.bot_process = subprocess.Popen(
            [sys.executable, "/app/velox_telegram_bot/main.py"],
            cwd="/app"
        )

    def restart_bot(self):
        """Restart the Telegram bot process."""
        if self.bot_process and self.bot_process.poll() is None:
            logger.info("Terminating existing bot process...")
            self.bot_process.terminate()
            self.bot_process.wait()  # Wait for the process to terminate
        self.start_bot()

    def on_modified(self, event):
        """Handle file modification events."""
        if event.src_path.endswith('.py'):
            logger.info(f"Detected change in: {event.src_path}")
            self.restart_bot()

def run_dev_server():
    """Run the development server and bot reloader."""
    logger.info("Starting development server...")

    # Start the Django server
    django_process = subprocess.Popen(
        [sys.executable, "/app/backend/manage.py", "runserver", "0.0.0.0:8000"],
        cwd="/app/backend"
    )

    # Set up file watching for the bot
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path='/app/velox_telegram_bot', recursive=True)
    observer.start()

    logger.info("Watching for changes in the Telegram bot...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        logger.info("Stopping observer...")
        django_process.terminate()
        logger.info("Django server terminated.")
    observer.join()

if __name__ == "__main__":
    run_dev_server()