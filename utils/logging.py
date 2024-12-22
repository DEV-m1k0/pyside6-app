import logging

def setup_logging() -> None:
    logging.basicConfig(level=logging.DEBUG, filename="logs.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")