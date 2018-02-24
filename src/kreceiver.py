from kfile import *
from khost import *
import socket


class KReceiver:
    def __init__(self, khost, kfilewriter):
        """
        :param khost: Information of sender
        :param kfilewriter: Information of file that will be created

        :type khost: KHost
        :type kfilewriter: KFileWriter
        """
        self.sender = khost
        self.file = kfilewriter

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((khost.addr, khost.port))
        self.socket.listen(2)

    def start_listening(self):
        print("Listening for coming connactions...")
        sender, addr = self.socket.accept()

        print("[*] Accepted connection from : %s:%d" % (addr[0], addr[1]))
        self.start_receiving(sender)

    def start_receiving(self, sender):
        # Receive header
        header = self.recv(sender).decode("utf-8")
        self.file.header_to_file(header)
        print("[*] Header is received : " + header)

        # Receive data till |END| flag is received
        while True:
            data = self.recv(sender)
            if data == b"":
                break
            self.file.write(data)

        self.file.finish_writing()

        # Receive end flag
        finish_flag = self.recv(sender).decode("utf-8")
        self.socket.close()

        if finish_flag == "|END|":
            print("Receiving successfuly finished.")
            return 1

        print("Receiving is not successful. Missing finish flag.")
        return 0

    def recv(self, sender):
        data = sender.recv(16).decode("utf-8")
        # print("DATA :", data)
        data_len = int(data)
        # data_len = int(sender.recv(16).decode("utf-8"))
        return sender.recv(data_len)


if __name__ == "__main__":
    host = KHost("0.0.0.0", 9301)
    file = KFileWriter("/home/ft/Downloads/new-linuxmint-18.2-cinnamon-64bit2.iso")

    receiver = KReceiver(host, file)
    receiver.start_listening()
    receiver.socket.close()
