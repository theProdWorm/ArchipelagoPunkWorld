from Options import Option
from worlds.AutoWorld import World, WebWorld
from BaseClasses import Tutorial, Item, ItemClassification

from . import locations, regions
from .items import PunkItem, item_table, module_table, currency_table, filler_table
from .options import PunkOptions

from typing import Any
from dataclasses import fields
import random
import re

class PunkWeb(WebWorld):
    bug_report_page = "https://github.com/theProdWorm/PunkArchipelago/issues"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the PUNK integration for Archipelago multiworld games.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Prodworm"])]

    theme = "partyTime"

    option_groups = options.punk_option_groups

class PunkWorld(World):
    """
    PUNK is an open world bullet hell action roguelike.
    Fight vicious creatures, explore diverse biomes, hone your movement skills, 
    manage resources, tinker with weapons and gadgets to upgrade your tiny ship 
    until you become the apex predator of this strange, alien world.
    """
    game = "PUNK"
    options: PunkOptions
    options_dataclass = PunkOptions
    topology_present = False
    origin_region_name = "Power 0"
    
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = locations.all_possible_locations
    
    item_name_groups = {
        "Module": {name for name in module_table},
        "Currency": {name for name in currency_table},
        "Filler": {name for name in filler_table}
    }

    required_client_version = (0, 6, 8)
    web = PunkWeb()

    def generate_early(self)\
            -> None:        
        if not self.player_name.isascii():
            raise ValueError("PUNK yaml's slot name has invalid characters.")

        locations.create_locations(self)

    def pre_fill(self)\
            -> None:

        if False: #not self.options.replace_boss_drops_with_shop_unlocks:
            return

        def fill_encounters(num: int, type: str, offset: int):
            for n in range(num):
                location = self.get_location(f"{type} {n+1}")
                item = PunkItem(f"Completed {type}",
                                ItemClassification.progression, offset+n, self.player)

                self.multiworld.push_item(location, item, False)

        boss_count = (4 if self.options.victory == 0 
                    else (1 if self.options.victory == 1 
                            else self.options.custom_boss_count))
        
        fill_encounters(self.options.small_encounters, "Small Encounter", 10000)
        fill_encounters(self.options.advanced_encounters, "Advanced Encounter", 11000)
        fill_encounters(boss_count, "Final Boss", 12000)

    def create_items(self)\
            -> None:
        itempool = [name 
                    for name, data in item_table.items()
                    for _ in range(data.weight)]
        itempool = random.sample(itempool, len(locations.all_locations))

        self.multiworld.itempool += map(self.create_item, itempool)

    def create_item(self, name: str)\
            -> Item:
        data = item_table[name]
        return PunkItem(name, data.item_type, data.code, self.player)

    def create_regions(self)\
            -> None:
        regions.create_regions(self)

    # Sends player options to client
    def fill_slot_data(self)\
            -> dict[str, Any]:
        option_fields = fields(self.options)

        slot_data = {}

        for field in option_fields:
            option = getattr(self.options, field.name)
            value = option.value

            if isinstance(value, Option):
                print(f"Nested option object: {field.name} = {value}")

            slot_data[field.name] = value

        return slot_data

    def get_filler_item_name(self)\
            -> str:
        return self.random.choice(filler_table)

    def custom_ut_sort(self, _, location_label: str) -> int:
        return self.location_name_to_id[location_label]