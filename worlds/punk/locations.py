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
        region_name = f"Post {type_name} {n+1}"

        unlocks.update({region_name: {}})

        for m in range(num_unlocks):
            location_name = f"Post {type_name} {n+1}-{m+1}"
            id = n * num_regions + m + id_offset

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
        **{f"Generator Cache {n+1}": n for n in range(options.generator_caches)},

        **({
               **{f"White Cache {n+1}": n + 100 for n in range(options.white_caches)},
               **{f"Green Cache {n+1}": n + 200 for n in range(options.green_caches)},
               **{f"Orange Cache {n+1}": n + 300 for n in range(options.orange_caches)},
               **{f"Pink Cache {n+1}": n + 400 for n in range(options.pink_caches)},
               **{f"Purple Cache {n+1}": n + 500 for n in range(options.purple_caches)},
               **{f"Yellow Cache {n+1}": n + 600 for n in range(options.yellow_caches)}
           }
           if options.separate_colored_caches
           else {f"Loot Cache {n+1}": n + 700 for n in range(options.total_caches)}),
        **{f"Fiber Plant {n+1}":n+800 for n in range(options.fiber_plants)},
        **{f"Gland Plant {n+1}":n+900 for n in range(options.gland_plants)},
        **{f"Loot Crate {n+1}":n+1000 for n in range(options.loot_crates)}   
    }
    
    small_encounters = {f"Small Encounter {n+1}":n+1100 for n in range(options.small_encounters)}
    advanced_encounters = {f"Advanced Encounter {n+1}":n+1200 for n in range(options.advanced_encounters)}
    final_bosses = {f"Final Boss {n+1}": n + 1300 for n in range(boss_count)}

    pse_shop_unlocks = generate_post_boss_locations("Small Encounter", 
                                                    options.small_encounters, 
                                                    options.small_encounter_shop_unlocks, 
                                                    2000)
    pae_shop_unlocks = generate_post_boss_locations("Advanced Encounter",
                                                    options.advanced_encounters,
                                                    options.advanced_encounter_shop_unlocks,
                                                    3000)
    pfb_shop_unlocks = generate_post_boss_locations("Final Boss",
                                                    boss_count,
                                                    options.final_boss_shop_unlocks,
                                                    4000)

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
    **{f"Generator Cache {n+1}": n for n in range(GeneratorCaches.range_end)},
    **{f"White Cache {n+1}": n + 100 for n in range(WhiteCaches.range_end)},
    **{f"Green Cache {n+1}": n + 200 for n in range(GreenCaches.range_end)},
    **{f"Orange Cache {n+1}": n + 300 for n in range(OrangeCaches.range_end)},
    **{f"Pink Cache {n+1}": n + 400 for n in range(PinkCaches.range_end)},
    **{f"Purple Cache {n+1}": n + 500 for n in range(PurpleCaches.range_end)},
    **{f"Yellow Cache {n+1}": n + 600 for n in range(YellowCaches.range_end)},
    **{f"Loot Cache {n+1}": n + 700 for n in range(TotalCaches.range_end)},
    **{f"Fiber Plant {n+1}":n+800 for n in range(FiberPlants.range_end)},
    **{f"Gland Plant {n+1}":n+900 for n in range(GlandPlants.range_end)},
    **{f"Loot Crate {n+1}":n+1000 for n in range(LootCrates.range_end)},
    **{f"Small Encounter {n+1}":n+1100 for n in range(SmallEncounters.range_end)},
    **{f"Advanced Encounter {n+1}":n+1200 for n in range(AdvancedEncounters.range_end)},
    **{f"Final Boss {n+1}": n + 1300 for n in range(CustomBossCount.range_end)}
}

possible_pse_shop_unlocks: dict[str, dict[str, int]] = generate_post_boss_locations("Small Encounter",
                                                                        SmallEncounters.range_end,
                                                                        SmallEncounterShopUnlocks.range_end,
                                                                        2000)
possible_pae_shop_unlocks: dict[str, dict[str, int]] = generate_post_boss_locations("Advanced Encounter",
                                                                        AdvancedEncounters.range_end,
                                                                        AdvancedEncounterShopUnlocks.range_end,
                                                                        3000)
possible_pfb_shop_unlocks: dict[str, dict[str, int]] = generate_post_boss_locations("Final Boss",
                                                                        CustomBossCount.range_end,
                                                                        FinalBossShopUnlocks.range_end,
                                                                        4000)

for region in possible_pse_shop_unlocks:
    all_possible_locations.update(possible_pse_shop_unlocks[region])
for region in possible_pae_shop_unlocks:
    all_possible_locations.update(possible_pae_shop_unlocks[region])
for region in possible_pfb_shop_unlocks:
    all_possible_locations.update(possible_pfb_shop_unlocks[region])