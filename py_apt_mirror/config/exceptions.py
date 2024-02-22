from json import JSONDecodeError

########################################################################################################################
class ConfigurationError(Exception):
    """Base exception class for Configuration exceptions."""


########################################################################################################################
class FailedToDecodeJsonError(ConfigurationError):
    def __init__(self, fileName : str, exception : JSONDecodeError) -> None:
        messageLines = [
            "Failed to decode JSON from file {}.".format(fileName),
            "{}".format(exception)
        ]
        super().__init__("".join(messageLines))
        self._fileName = fileName

########################################################################################################################
class FailedToFindConfigFileError(ConfigurationError):
    def __init__(self, fileName : str) -> None:
        super().__init__("Failed to find config file named {}".format(fileName))
        self._fileName = fileName

########################################################################################################################
class UnknownSourceTypeError(ConfigurationError):
    def __init(self, data : str) -> None:
        super().__init__("Unknow source type provided: {}".format(data))
        self._type = data

########################################################################################################################
class NoProvidedComponentsError(ConfigurationError):
    def __init(self, name : str) -> None:
        super().__init__("No provided components for source: {}".format(name))
        self._name = name


