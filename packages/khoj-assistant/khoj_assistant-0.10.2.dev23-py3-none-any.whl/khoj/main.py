# Standard Packages
import os
import signal
import sys
import locale

if sys.stdout is None:
    sys.stdout = open(os.devnull, "w")
if sys.stderr is None:
    sys.stderr = open(os.devnull, "w")

import logging
import threading
import warnings
from platform import system

# Ignore non-actionable warnings
warnings.filterwarnings("ignore", message=r"snapshot_download.py has been made private", category=FutureWarning)
warnings.filterwarnings("ignore", message=r"legacy way to download files from the HF hub,", category=FutureWarning)

# External Packages
import uvicorn
from fastapi import FastAPI
from rich.logging import RichHandler
import schedule

# Internal Packages
from khoj.configure import configure_routes, initialize_server
from khoj.utils import state
from khoj.utils.cli import cli

# Initialize the Application Server
app = FastAPI()

# Set Locale
locale.setlocale(locale.LC_ALL, "")

# Setup Logger
rich_handler = RichHandler(rich_tracebacks=True)
rich_handler.setFormatter(fmt=logging.Formatter(fmt="%(message)s", datefmt="[%X]"))
logging.basicConfig(handlers=[rich_handler])

logger = logging.getLogger("khoj")


def run():
    # Turn Tokenizers Parallelism Off. App does not support it.
    os.environ["TOKENIZERS_PARALLELISM"] = "false"

    # Load config from CLI
    state.cli_args = sys.argv[1:]
    args = cli(state.cli_args)
    set_state(args)

    # Create app directory, if it doesn't exist
    state.config_file.parent.mkdir(parents=True, exist_ok=True)

    # Set Logging Level
    if args.verbose == 0:
        logger.setLevel(logging.INFO)
    elif args.verbose >= 1:
        logger.setLevel(logging.DEBUG)

    # Set Log File
    fh = logging.FileHandler(state.config_file.parent / "khoj.log", encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    logger.info("🌘 Starting Khoj")

    if not args.gui:
        # Setup task scheduler
        poll_task_scheduler()

        # Start Server
        initialize_server(args.config, args.regenerate, required=False)
        configure_routes(app)
        start_server(app, host=args.host, port=args.port, socket=args.socket)
    else:
        from PySide6 import QtWidgets
        from PySide6.QtCore import QTimer

        from khoj.interface.desktop.main_window import MainWindow, ServerThread
        from khoj.interface.desktop.system_tray import create_system_tray

        # Setup GUI
        url = f"http://{args.host}:{args.port}"
        gui = QtWidgets.QApplication([])
        main_window = MainWindow(url)

        # System tray is only available on Windows, MacOS.
        # On Linux (Gnome) the System tray is not supported.
        # Since only the Main Window is available
        # Quitting it should quit the application
        if system() in ["Windows", "Darwin"]:
            gui.setQuitOnLastWindowClosed(False)
            tray = create_system_tray(gui, main_window)
            tray.show()

        # Setup Server
        initialize_server(args.config, args.regenerate, required=False)
        configure_routes(app)
        server = ServerThread(start_server_func=lambda: start_server(app, host=args.host, port=args.port))

        logger.info(f"🌗 Khoj is running at {url}")

        # Show config window on first run and main window otherwise
        startup_window = (
            main_window.show_page(maximized=True) if args.config else main_window.show_page("config", maximized=True)
        )
        startup_window()

        # Setup Signal Handlers
        signal.signal(signal.SIGINT, sigint_handler)
        # Invoke Python interpreter every 500ms to handle signals, run scheduled tasks
        timer = QTimer()
        timer.start(500)
        timer.timeout.connect(schedule.run_pending)

        # Start Application
        server.start()
        gui.aboutToQuit.connect(server.terminate)

        # Close Splash Screen if still open
        if system() != "Darwin":
            try:
                import pyi_splash

                # Update the text on the splash screen
                pyi_splash.update_text("Khoj setup complete")
                # Close Splash Screen
                pyi_splash.close()
            except:
                pass

        gui.exec()


def sigint_handler(*args):
    from PySide6 import QtWidgets

    QtWidgets.QApplication.quit()


def set_state(args):
    state.config_file = args.config_file
    state.config = args.config
    state.verbose = args.verbose
    state.host = args.host
    state.port = args.port
    state.demo = args.demo


def start_server(app, host=None, port=None, socket=None):
    logger.info("🌖 Khoj is ready to use")
    if socket:
        uvicorn.run(app, proxy_headers=True, uds=socket, log_level="debug", use_colors=True, log_config=None)
    else:
        uvicorn.run(app, host=host, port=port, log_level="debug", use_colors=True, log_config=None)
    logger.info("🌒 Stopping Khoj")


def poll_task_scheduler():
    timer_thread = threading.Timer(60.0, poll_task_scheduler)
    timer_thread.daemon = True
    timer_thread.start()
    schedule.run_pending()


def run_gui():
    sys.argv += ["--gui"]
    run()


if __name__ == "__main__":
    run_gui()
