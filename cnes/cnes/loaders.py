from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity, TakeFirst
from cnes.items import CityItem, EquipmentItem


class CityItemLoader(ItemLoader):
    default_item_class = CityItem
    default_output_processor = TakeFirst()
    equipamentos_out = Identity()


class EquipmentItemLoader(ItemLoader):
    default_item_class = EquipmentItem
    default_output_processor = TakeFirst()
    default_input_processor = TakeFirst()
