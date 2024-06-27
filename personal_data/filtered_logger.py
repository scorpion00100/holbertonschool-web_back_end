#!/usr/bin/env python3
"""filtered_logger module"""

import logging
import mysql.connector
import os
import re
from typing import List, Tuple

PII_FIELDS: Tuple = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, 
                 message: str, separator: str) -> str:
    """Returns the log message obfuscated"""
    for field in fields:
        pattern = r"(?<={}=)[^{}]+(?={})".format(field, separator, separator)
        message = re.sub(pattern, redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filters values in incoming log records using filter-datum
        """
        m = super().format(record)
        message = filter_datum(self.fields, self.REDACTION, m, self.SEPARATOR)
        return message


def get_logger() -> logging.Logger:
    """Returns a logging.Logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns a connector to the database"""
    username = os.getenv("PERSONAL_DATA_DB_USERNAME")
    pwd = os.getenv("PERSONAL_DATA_DB_PASSWORD")
    host = os.getenv("PERSONAL_DATA_DB_HOST")
    db = os.getenv("PERSONAL_DATA_DB_NAME")

    connector = mysql.connector.connect(
        host=host,
        user=username,
        password=pwd,
        database=db
    )

    return connector


def main() -> None:
    """Main function that obtains a databse connection using get_db,
    retrieves all rows in the users tables and displays each row
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()
    for row in cursor:
        message = "name={}; email={}; phone={}; ssn={}; password={}; "\
                   "ip={}; last_origin={}; user_agent={};".format(row[0],
                                                                  row[1],
                                                                  row[2],
                                                                  row[3],
                                                                  row[4],
                                                                  row[5],
                                                                  row[6],
                                                                  row[7],)
        print("hey")
        logger.info(message)
        print("by")
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
