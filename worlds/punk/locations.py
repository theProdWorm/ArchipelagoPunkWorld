from typing import TYPE_CHECKING

from BaseClasses import Location
from .options import *

if TYPE_CHECKING:
    from . import PunkWorld

class PunkLocation(Location):
    game: str = "PUNK"

default_accessible: dict[str, int]
small_encounters: dict[str, int]
advanced_encounters: dict[str, int]
final_bosses: dict[str, int]
pse_shop_unlocks: dict[str, dict[str, int]]
pae_shop_unlocks: dict[str, dict[str, int]]
pfb_shop_unlocks: dict[str, dict[str, int]]

all_locations: dict[str, int]

location_region_mapping: dict[str, dict[str, int]]

def generate_post_boss_locations(type_name: str, num_regions: int, num_unlocks: int, id_offset: int)\
        -> dict[str, dict[str, int]]:
    unlocks: dict[str, dict[str, int]] = {}

    for n in range(num_regions):
        region_name = f"Post {type_name} {n + 1}"

        unlocks.update({region_name: {}})

        for m in range(num_unlocks):
            location_name = f"Post {type_name} {n + 1}-{m + 1}"
            id = n * 100 + m + id_offset

            unlocks[region_name].update({location_name: id})

    return unlocks

def create_locations(world: "PunkWorld")\
        -> None:
    options = world.options
    boss_count = (4 if options.victory == 0 
                  else (1 if options.victory == 1 
                        else options.custom_boss_count))

    global default_accessible
    global small_encounters
    global advanced_encounters
    global final_bosses
    global pse_shop_unlocks
    global pae_shop_unlocks
    global pfb_shop_unlocks

    default_accessible = {
        **{f"Generator Crate {n+1}": n + 1 for n in range(options.generator_crates)},

        **({
               **{f"White Crate {n+1}": n + 100 for n in range(options.white_crates)},
               **{f"Green Crate {n+1}": n + 200 for n in range(options.green_crates)},
               **{f"Orange Crate {n+1}": n + 300 for n in range(options.orange_crates)},
               **{f"Pink Crate {n+1}": n + 400 for n in range(options.pink_crates)},
               **{f"Purple Crate {n+1}": n + 500 for n in range(options.purple_crates)},
               **{f"Yellow Crate {n+1}": n + 600 for n in range(options.yellow_crates)}
           }
           if options.separate_colored_crates
           else {f"Crate {n+1}": n + 700 for n in range(options.total_crates)}),
        **{f"Fiber Plant {n+1}": n + 800 for n in range(options.fiber_plants)},
        **{f"Gland Plant {n+1}": n + 900 for n in range(options.gland_plants)},
        **{f"Box {n+1}": n + 1000 for n in range(options.boxes)}
    }
    
    small_encounters = {f"Small Encounter {n + 1}": n + 1100 for n in range(options.small_encounters)}
    advanced_encounters = {f"Advanced Encounter {n + 1}": n + 1200 for n in range(options.advanced_encounters)}
    final_bosses = {f"Final Boss {n + 1}": n + 1300 for n in range(boss_count)}

    pse_shop_unlocks = generate_post_boss_locations("Small Encounter", 
                                                    options.small_encounters, 
                                                    options.small_encounter_shop_unlocks, 
                                                    10000)
    pae_shop_unlocks = generate_post_boss_locations("Advanced Encounter",
                                                    options.advanced_encounters,
                                                    options.advanced_encounter_shop_unlocks,
                                                    20000)
    pfb_shop_unlocks = generate_post_boss_locations("Final Boss",
                                                    boss_count,
                                                    options.final_boss_shop_unlocks,
                                                    30000)

    global all_locations
    all_locations = default_accessible.copy()
    all_locations.update(small_encounters)
    all_locations.update(advanced_encounters)
    all_locations.update(final_bosses)
    for locs in pse_shop_unlocks.values():
        all_locations.update(locs)
    for locs in pae_shop_unlocks.values():
        all_locations.update(locs)
    for locs in pfb_shop_unlocks.values():
        all_locations.update(locs)

    global location_region_mapping
    location_region_mapping = {
        "Power 0": default_accessible,
        "Power 1": small_encounters,
        "Power 2": advanced_encounters,
        "Power 3": final_bosses,
        **pse_shop_unlocks,
        **pae_shop_unlocks,
        **pfb_shop_unlocks
    }

    # for loc in location_region_mapping["Power 0"]:
    #     print(loc)

all_possible_locations : dict[str, int] = {
    **{f"Generator Crate {n + 1}": n + 1 for n in range(GeneratorCrates.range_end)},
    **{f"White Crate {n + 1}": n + 100 for n in range(WhiteCrates.range_end)},
    **{f"Green Crate {n + 1}": n + 200 for n in range(GreenCrates.range_end)},
    **{f"Orange Crate {n + 1}": n + 300 for n in range(OrangeCrates.range_end)},
    **{f"Pink Crate {n + 1}": n + 400 for n in range(PinkCrates.range_end)},
    **{f"Purple Crate {n + 1}": n + 500 for n in range(PurpleCrates.range_end)},
    **{f"Yellow Crate {n + 1}": n + 600 for n in range(YellowCrates.range_end)},
    **{f"Crate {n + 1}": n + 700 for n in range(TotalCrates.range_end)},
    **{f"Fiber Plant {n + 1}": n + 800 for n in range(FiberPlants.range_end)},
    **{f"Gland Plant {n + 1}": n + 900 for n in range(GlandPlants.range_end)},
    **{f"Box {n + 1}": n + 1000 for n in range(Boxes.range_end)},
    **{f"Small Encounter {n + 1}": n + 1100 for n in range(SmallEncounters.range_end)},
    **{f"Advanced Encounter {n + 1}": n + 1200 for n in range(AdvancedEncounters.range_end)},
    **{f"Final Boss {n + 1}": n + 1300 for n in range(CustomBossCount.range_end)}
}

possible_pse_shop_unlocks: dict[str, dict[str, int]] = generate_post_boss_locations("Small Encounter",
                                                                        SmallEncounters.range_end,
                                                                        SmallEncounterShopUnlocks.range_end,
                                                                        10000)
possible_pae_shop_unlocks: dict[str, dict[str, int]] = generate_post_boss_locations("Advanced Encounter",
                                                                        AdvancedEncounters.range_end,
                                                                        AdvancedEncounterShopUnlocks.range_end,
                                                                        20000)
possible_pfb_shop_unlocks: dict[str, dict[str, int]] = generate_post_boss_locations("Final Boss",
                                                                        CustomBossCount.range_end,
                                                                        FinalBossShopUnlocks.range_end,
                                                                        30000)

for region in possible_pse_shop_unlocks:
    all_possible_locations.update(possible_pse_shop_unlocks[region])
for region in possible_pae_shop_unlocks:
    all_possible_locations.update(possible_pae_shop_unlocks[region])
for region in possible_pfb_shop_unlocks:
    all_possible_locations.update(possible_pfb_shop_unlocks[region])