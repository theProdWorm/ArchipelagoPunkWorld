from Options import Option
from worlds.AutoWorld import World, WebWorld
from BaseClasses import Tutorial, Item, ItemClassification

from . import locations, regions, items, rules
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
    
    item_name_to_id = {name: data.id for name, data in items.item_table.items()}
    location_name_to_id = locations.all_possible_locations
    
    item_name_groups = {
        "Module": {name for name in items.module_table},
        "Currency": {name for name in items.currency_table},
        "Filler": {name for name in items.filler_table},
        "Boss": {name for name in items.boss_table}
    }

    web = PunkWeb()

    def generate_early(self)\
            -> None:        
        if not self.player_name.isascii():
            raise ValueError("PUNK yaml's slot name has invalid characters.")

        locations.create_locations(self)

    def create_items(self)\
            -> None:
        for location in self.get_region("Power 1").locations:
            item = self.create_item("Completed Small Encounter")
            self.multiworld.push_item(location, item, False)
        for location in self.get_region("Power 2").locations:
            item = self.create_item("Completed Advanced Encounter")
            self.multiworld.push_item(location, item, False)
        for location in self.get_region("Power 3").locations:
            item = self.create_item("Completed Final Boss")
            self.multiworld.push_item(location, item, False)

        itempool: list[Item] = []
        unfilled_locations = [location for region in self.multiworld.get_regions(self.player)
                              for location in region.locations
                              if not location.item]

        module_item_names = [name for name, data in items.module_table.items()
                             for _ in range(data.weight)]
        module_item_names = random.sample(module_item_names, self.options.power3_requirements)
        itempool += map(self.create_item, module_item_names)

        num_locations = len(unfilled_locations) - len(module_item_names)

        filler_item_names = [name for name, data in items.item_table.items()
                             if data.weight
                             for _ in range(data.weight)]
        filler_item_names = random.sample(filler_item_names, num_locations)
        itempool += map(self.create_item, filler_item_names)

        self.multiworld.itempool += itempool

    def create_item(self, name: str)\
            -> Item:
        data = items.item_table[name]
        return items.PunkItem(name, data.item_type, data.id, self.player)

    def create_regions(self)\
            -> None:
        regions.create_regions(self)
        
        boss_count = (4 if self.options.victory == 0 
                      else (1 if self.options.victory == 1 
                            else self.options.custom_boss_count))

        victory_condition = rules.get_boss_rule("Final Boss", boss_count).resolve(self)
        self.multiworld.completion_condition[self.player] = victory_condition

    # Sends player options to client
    def fill_slot_data(self)\
            -> dict[str, Any]:
        boss_count = (4 if self.options.victory == 0 
                        else (1 if self.options.victory == 1 
                            else self.options.custom_boss_count))

        return {
            "DeathLinkPenalty": int(self.options.death_link_penalty),
            "DeathLinkDamage": int(self.options.death_link_damage),

            "SmallEncounters": int(self.options.small_encounters),
            "AdvancedEncounters": int(self.options.advanced_encounters),
            "FinalBosses": boss_count,

            "EncountersUnlockShopItems": bool(self.options.encounters_unlock_shop_items),
            "SmallEncounterShopUnlocks": int(self.options.small_encounter_shop_unlocks),
            "AdvancedEncounterShopUnlocks": int(self.options.advanced_encounter_shop_unlocks),
            "FinalBossShopUnlocks": int(self.options.final_boss_shop_unlocks),

            "GeneratorCrates": int(self.options.generator_crates),

            "SeparateColoredCrates": bool(self.options.separate_colored_crates),
            **({
                "WhiteCrates": int(self.options.white_crates),
                "GreenCrates": int(self.options.green_crates),
                "OrangeCrates": int(self.options.orange_crates),
                "PinkCrates": int(self.options.pink_crates),
                "PurpleCrates": int(self.options.purple_crates),
                "YellowCrates": int(self.options.yellow_crates),
            } 
            if self.options.separate_colored_crates 
            else {
                "TotalCrates": int(self.options.total_crates)
            }),

            "FiberPlants": int(self.options.fiber_plants),
            "GlandPlants": int(self.options.gland_plants),

            "Boxes": int(self.options.boxes)
        }
    
    def get_filler_item_name(self)\
            -> str:
        return self.random.choice([a for a in items.filler_table])

    def custom_ut_sort(self, _, location_label: str) -> int:
        return self.location_name_to_id[location_label]