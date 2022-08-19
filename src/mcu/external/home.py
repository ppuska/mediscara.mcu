
import logging
from mcu.models.user_defined import Command
from mcu.config import add_tcp_server

class HomeCommand(Command):
    def __init__(self) -> None:
        super().__init__(keyword='home')

        self.__tcp = add_tcp_server('0.0.0.0', 65432)

    def target(self, *_):
        logging.info("Homing robot")
        self.__tcp.send('IAC|HOME\n')