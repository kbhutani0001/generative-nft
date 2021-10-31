class Variant:

    def __init__(self, name: str, filename: str, rarity: float, layersToExclude: list[str] = []):
        """
        :param name: name of variant
        :param filename: name of file with extension
        :param rarity: rarirty from 0-1
        """
        self.name = name
        self.filename = filename
        self.rarity = rarity
        self.layersToExclude = layersToExclude
