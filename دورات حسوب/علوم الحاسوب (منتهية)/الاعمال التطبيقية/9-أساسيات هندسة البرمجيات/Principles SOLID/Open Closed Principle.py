# Bad example
# الملف الاصلي
class Logger:
    def log_console(self):
        print('console logging..')
# اضافة خاصية جديدة بعد فترة
class Logger:
    def log_console(self):
        print('console logging..')
# الخاصية الجديدة
    def log_file(self):
        print('file logging..')



# Good example
# الملف الاصلي
class Logger:
    def log(self):
        pass
# اضافة خاصية جديدة بعد فترة
class ConsoleLogger(Logger):
    def log(self):
        print('console logging..')
# الخاصية الجديدة
class FileLogger(Logger):
    def log(self):
        print('file logging..')