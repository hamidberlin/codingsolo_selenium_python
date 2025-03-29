import os
import logging

def setup_logger():
    # Verzeichnis für Logs definieren
    log_dir = os.path.join(".venv", "logs")
    os.makedirs(log_dir, exist_ok=True)

    # Log-Datei definieren
    log_file = os.path.join(log_dir, "test_log.log")

    # Logger konfigurieren
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file, mode='a', encoding='utf-8'),
            logging.StreamHandler()  # Ausgabe in der Konsole
        ]
    )

    logger = logging.getLogger(__name__)
    return logger
