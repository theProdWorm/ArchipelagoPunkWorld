from typing import TYPE_CHECKING

from BaseClasses import Region

from . import locations
from . import rules

if TYPE_CHECKING:
    from . import PunkWorld

def create_region(world: "PunkWorld", region_name: str)\
        -> Region:
    region = Region(region_name, world.player, world.multiworld)
    locations_ = locations.location_region_mapping[region_name]
    region.add_locations(locations_)
    return region

def create_connections(world: "PunkWorld", regions: list[Region])\
        -> None:
    regions_dict = {region.name: region for region in regions}

    def connect(source_name: str, destination_name: str, rule)\
            -> None:
        source_region = regions_dict[source_name]
        destination_region = regions_dict[destination_name]
        source_region.connect(destination_region, rule = rule)

    for n in range(3):
        connect(f"Power {n}", f"Power {n+1}", rules.get_power_rule(n+1, world.options))

    # i = 1
    # for region in locations.pse_shop_unlocks:
    #     connect("Power 1", region, rules.get_boss_rule("Small Encounter", i))
    #     i += 1
    # i = 1
    # for region in locations.pae_shop_unlocks:
    #     connect("Power 2", region, rules.get_boss_rule("Advanced Encounter", i))
    #     i += 1
    # i = 1
    # for region in locations.pfb_shop_unlocks:
    #     connect("Power 3", region, rules.get_boss_rule("Final Boss", i))
    #     i += 1
    
def create_regions(world: "PunkWorld")\
        -> list[Region]:
    regions = [create_region(world, region_name)
               for region_name in locations.location_region_mapping]
    create_connections(world, regions)
    world.multiworld.regions += regions