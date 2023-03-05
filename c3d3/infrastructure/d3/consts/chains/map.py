from c3d3.core.decorators.classproperty.decorator import classproperty

from c3d3.infrastructure.d3.consts.chains.fantom.chain import Fantom
from c3d3.infrastructure.d3.consts.chains.optimism.chain import Optimism
from c3d3.infrastructure.d3.consts.chains.polygon.chain import Polygon


class ChainMap:

    _CHAINS = {
        Fantom.name: Fantom,
        Optimism.name: Optimism,
        Polygon.name: Polygon
    }

    @classproperty
    def chains(self) -> dict:
        return self._CHAINS

    @classmethod
    def get_chain(cls, name: str):
        return cls.chains.get(name)
