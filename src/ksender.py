from kfile import *
from khost import *
import socket


class KSender:
    def __init__(self, khost, kfilereader):
        """
        :param khost: Information of receiver
        :param kfilereader: Information of file to send

        :type khost: KHost
        :type kfilereader: KFileReader
        """

        self.host = khost
        self.file = kfilereader

        # Create socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_sending(self):
        # Connect to receiver
        self.socket.connect((self.host.addr, self.host.port))

        # Send header
        # self.socket.send(self.file.get_header().encode("utf-8"))
        self.send(self.file.get_header())

        # Send data
        counter = 0
        while counter * self.file.read_size < self.file.size:
            self.send(self.file.read())
            counter += 1
        self.file.finish_reading()

        # Send empty package to finish data sending and receiving
        self.send("")

        # Send end flag
        self.send("|END|")

        self.socket.close()

        print("Sending successfully finished.")
        return 1

    def send(self, data):
        data_len = str(len(data))
        data_len = (16 - len(data_len)) * "0" + str(len(data))
        self.socket.send(data_len.encode("utf-8"))
        if type(data) == str:
            data = data.encode("utf-8")
        self.socket.send(data)


if __name__ == "__main__":
    host = KHost("0.0.0.0", 9301)
    file = KFileReader("/home/user/Downloads/distros/linuxmint-18.2-cinnamon-64bit.iso", 2 ** 13)

    sender = KSender(host, file)

    import time

    current = time.time()
    sender.start_sending()
    print(time.time() - current)
