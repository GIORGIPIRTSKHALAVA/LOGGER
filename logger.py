import logging

class ConsoleLogger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler('add-logging-levels')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(self.formatter)
        self.logger.addHandler(file_handler)

    def validate_message(self, message):
        if not message or not message.strip():
            raise ValueError("Message must not be null or blank")
    def log(self, message):
        try:
            self.validate_message(message)
            self.logger.debug(message)
            self.logger.info(message)
        except ValueError as e:
            self.logger.error(f"Validation error: {e}")
if __name__ == "__main__":
    logger = ConsoleLogger()
    logger.log("This is a valid message")
    logger.log("  ")


