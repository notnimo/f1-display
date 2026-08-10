from src.utils.exception.exception import Exception, ExceptionLevel

class Logger:
    def __init__(self, name: str):
        self.name = name
        print(f"--------------------------\nLogger initialized for {self.name}\n--------------------------")

    def log(self, error: Exception):
        match(error.level):
            case ExceptionLevel.INFO:
                print(f"[{self.name}]: INFO: {error.message}")
            case ExceptionLevel.WARNING:
                print(f"[{self.name}]: WARNING: {error.message}")
            case ExceptionLevel.ERROR:
                print(f"[{self.name}]: ERROR: {error.message}")
            case ExceptionLevel.TERMINATE:
                print(f"[{self.name}]: TERMINATE: {error.message}")
                exit(1)

debug: Logger = Logger("F1-disp-logger")