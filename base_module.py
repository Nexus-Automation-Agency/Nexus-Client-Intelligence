from abc import ABC, abstractmethod
from typing import Dict, Any


class IntelligenceModule(ABC):
    """
    Public Contract Layer (No Implementation)

    Note:
    This module defines the interface only.
    All proprietary computation engines are excluded.
    """

    @abstractmethod
    def evaluate(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        pass
