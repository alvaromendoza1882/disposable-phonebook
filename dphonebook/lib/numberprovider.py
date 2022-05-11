import datetime
from logging import Logger
from typing import List

import requests

from dphonebook.lib.phonenumber import PhoneNumber


class NumberProvider:
    def __init__(self, logger: Logger, session: requests.Session) -> None:
        self.logger = logger
        self.session = session

    def domain(self) -> str:
        pass

    def verify_number_active(self, number: str, last_message_time: datetime.datetime = None) -> bool:
        # Number is active if last message was within one day
        if last_message_time:
            return (datetime.datetime.now() - last_message_time).days <= 1

        return False

    def last_message_time(self, number: str) -> datetime.datetime:
        pass

    def scrape(self) -> List[PhoneNumber]:
        pass


class SiteNotAvailable(Exception):
    pass
