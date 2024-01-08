# بالفعل، تستطيع حل المشكلة أيضًا بازالة المزخرفات، ولم نضطر إلى إزالة تلك الدوال التي قد نحتاج لها في كائنات أخرى، وفي نفس الوقت، لم يتم إلزام الكائن إلا بالدالة الأولى فقط.

# في الواقع، هذا هو الحل الأمثل لمشكلة فصل الواجهات، وذلك لأننا نفصل الواجهات اعتمادًا على احتياجات العملاء، وهناك نوعان من العملاء:

# العميل الأول يحتاج فقط إلى الدالة log_console().
# العميل الثاني يحتاج إلى الدالة log_file() وlog_database().
# لذلك، نقوم بإنشاء واجهة واحدة لكل نوع من العملاء، حيث الواجهة الأولى هي IConsoleLogger، والتي تتطلب فقط الدالة log_console().

# والواجهة الثانية هي IFileDatabaseLogger، والتي تتطلب الدوال log_file() وlog_database().

# وبالتالي يستطيع كل عميل أن يعتمد فقط على الواجهة التي يحتاجها، مما يجعل النظام أكثر مرونة وقابلية للتوسع.

from abc import ABC, abstractmethod

class IConsoleLogger(ABC):
    @abstractmethod
    def log_console(self):
        pass


class IFileDatabaseLogger(ABC):
    @abstractmethod
    def log_file(self):
        pass

    @abstractmethod
    def log_database(self):
        pass


class ConsoleLogger(IConsoleLogger):
    def log_console(self):
        print("Logging to console...")


class FileDatabaseLogger(IFileDatabaseLogger):
    def log_file(self):
        print("Logging to file...")

    def log_database(self):
        print("Logging to database...")


def main():
    logger = ConsoleLogger()
    logger.log_console()

    logger = FileDatabaseLogger()
    logger.log_file()
    logger.log_database()


if __name__ == "__main__":
    main()