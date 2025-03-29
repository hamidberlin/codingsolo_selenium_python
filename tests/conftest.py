import pytest
from utils.logging_config import setup_logger

@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    logger = setup_logger()
    logger.info("Test-Session gestartet")
    yield
    logger.info("Test-Session beendet")

# Beispiel für eine Testdatei (TestLoginWithDDTAndScreenshotFirefox.py)
from utils.logging_config import setup_logger

logger = setup_logger()

def test_login():
    logger.info("Starte den Login-Test")
    assert True  # Dein eigentlicher Testcode hier
    logger.info("Test erfolgreich abgeschlossen")
