import logging
import sys
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

def setup_github_classroom_logger(log_file: str = 'github_classroom.log', level=logging.INFO):
    """Function to setup logger for GitHub Classroom operations"""

    # Create logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create handlers
    console_handler = logging.StreamHandler(sys.stdout)
    file_handler = TimedRotatingFileHandler(log_dir / log_file, when="midnight", interval=1, backupCount=30)
    
    # Set the formatter for handlers
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Create logger and set level
    logger = logging.getLogger('github_classroom')
    logger.setLevel(level)

    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

# Create GitHub Classroom logger
github_classroom_logger = setup_github_classroom_logger()
