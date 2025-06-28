# File: plugins/base_plugin.py

from abc import ABC, abstractmethod

class SecurityPlugin(ABC):
    @abstractmethod
    def run_check(self) -> dict:
        """Each plugin must implement this method to return check results."""
        pass
