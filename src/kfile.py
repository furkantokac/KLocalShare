import os


class KFile:
    """
    KFile should be used dynamically just to keep
    data temporarily because file may be changed
    in a long period.
    """

    def __init__(self, path):
        self.path = path

        self.name = self.path_to_name(self.path)
        self.dir = self.path_to_dir(self.path)
        self.size = -1
        self.hash = -1

    def get_header(self):
        header = [''] * 10

        header[0] = self.name
        header[1] = str(self.size)
        header[8] = self.hash
        header[9] = 'END'

        return '|*|'.join(header)

    def header_to_file(self, header):
        '''
        :type header: str
        '''
        header = header.split("|*|")

        self.name = header[0]
        self.size = int(header[1])
        self.hash = header[2]

    def update_size(self):
        self.size = int(os.path.getsize(self.path))

    def update_hash(self):
        self.hash = 'sha1'

    def path_to_dir(self, path):
        return os.path.split(path)[0]

    def path_to_name(self, path):
        return os.path.split(path)[1]


class KFileWriter(KFile):
    def __init__(self, path):
        super().__init__(path)

        # Open new file to write byte in it
        self.file = open(self.path, "wb")

    def write(self, data):
        self.file.write(data)

    def finish_writing(self):
        self.file.close()


class KFileReader(KFile):
    def __init__(self, path, read_size=4096):
        super().__init__(path)
        self.read_size = read_size

        # File exists so we can calculate its size and hash
        self.update_size()
        self.update_hash()

        # Open the file to read byte
        self.file = open(self.path, "rb")

    def read(self):
        return self.file.read(self.read_size)

    def finish_reading(self):
        self.file.close()
