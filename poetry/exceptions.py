class PoetryException(Exception):

    pass


class InvalidProjectFile(PoetryException):

    pass


class InvalidSource(InvalidProjectFile):

    pass


class MissingSourceURL(InvalidSource):
    def __init__(self, name: str) -> None:
        self._name = name

        message = f'Unable to find the url for the "{name}" source.'

        super().__init__(message)
