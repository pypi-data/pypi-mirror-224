
class DataPipe:
    def __init__(self, datapipe) -> None:
        self.datapipe = datapipe

    def __getitem__(self, index):
        pass

    def __len__(self):
        return len(self.datapipe)

    def close(self):
        pass