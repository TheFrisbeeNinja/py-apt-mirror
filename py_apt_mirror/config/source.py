
from .exceptions import UnknownSourceTypeError, NoProvidedComponentsError

########################################################################################################################
class Source(object):
    def __init__(self, data):
        self._type = data["type"]
        self._url = data["url"]
        self._distribution = data["distribution"]
        self._alias = ""
        self._components = data["components"]
        self._clean = data["clean"]

        if self._type not in ("deb", "deb-src"):
            raise UnknownSourceTypeError(self._type)

        if not self._components:
            raise NoProvidedComponentsError(self._url)

        if "alias" in data:
            self._alias = data["alias"]

    ####################################################################################################################
    @property
    def type(self) -> str:
        return self._type

   ####################################################################################################################
    @property
    def url(self) -> str:
        return self._url

    ####################################################################################################################
    @property
    def distribution(self) -> str:
        return self._distribution

    ####################################################################################################################
    @property
    def alias(self) -> str:
        return self._alias

    ####################################################################################################################
    @property
    def clean(self) -> bool:
        return self._clean

