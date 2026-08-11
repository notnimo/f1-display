from src.utils.exception import Exception, debug

def test_logging():
    print("logging and exception test")

    print("info test")
    info: Exception = Exception("this is an info message", level=debug.level.INFO)
    debug.log(info)

    print("warning test")
    warning: Exception = Exception("this is a warning message", level=debug.level.WARNING)
    debug.log(warning)

    print("error test")
    error: Exception = Exception("this is an error message", level=debug.level.ERROR)
    debug.log(error)

    print("terminate test")
    terminate: Exception = Exception("this is a terminate message", level=debug.level.TERMINATE)
#    debug.log(terminate)

if __name__ == "__main__":
    test_logging()