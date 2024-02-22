import os
import logging
import json

from .exceptions import FailedToDecodeJsonError, FailedToFindConfigFileError
from .source import Source

log = logging.getLogger(__name__)


########################################################################################################################
class Configuration(object):
    def __init__(self, fileName: str):
        self._fileName = fileName

        if os.path.isfile(self._fileName):
            try:
                self._data = json.load(open(self._fileName, 'r'))
            except json.JSONDecodeError as e:
                raise FailedToDecodeJsonError(self._fileName, e)

        else:
            raise FailedToFindConfigFileError(self._fileName)

        self._sources = []

        for source in self._data["sources"]:
            self._sources.append(Source(source))

    ####################################################################################################################
    @property
    def fileName(self) -> str:
        return self._fileName

    ####################################################################################################################
    @property
    def mirrorDirectory(self) -> str:
        return os.path.join(self._data["config"]["base_path"], self._data["config"]["mirror_directory"])

    ####################################################################################################################
    @property
    def skeletonDirectory(self) -> str:
        return os.path.join(self._data["config"]["base_path"], self._data["config"]["skeleton_directory"])

    ####################################################################################################################
    @property
    def varDirectory(self) -> str:
        return os.path.join(self._data["config"]["base_path"], self._data["config"]["var_directory"])

    ####################################################################################################################
    @property
    def defaultArch(self) -> str:
        return self._data["config"]["default_arch"]

    ####################################################################################################################
    @property
    def numberOfThreads(self) -> int:
        return self._data["config"]["number_of_threads"]

    ####################################################################################################################
    @property
    def sources(self):
        return self._sources
    

        
