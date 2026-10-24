from .bases import PunkTestBase
from Utils import visualize_regions

import random

from .. import locations
from .. import items

class TestPower(PunkTestBase):
    def test_power1(self)\
            -> None:
        locs = [loc for locs in locations.pse_shop_unlocks.values() for loc in locs]

        itempool = [name 
                    for name, data in items.module_table.items()
                    for _ in range(data.weight)]
        combinations = [random.sample(itempool, 12) + ["Completed Small Encounter"]]

        for item_name in combinations[0]:
            item = self.get_item_by_name(item_name)
            self.collect(item)
        
        reachable_regions = [region for region in self.world.get_regions() if self.can_reach_region(region.name)]
        origin = self.world.get_region("Power 0")
        visualize_regions(origin, "regions_puml", 
                                  show_entrance_names = True, 
                                  show_entrance_rules = True, 
                                  regions_to_highlight = reachable_regions)

        for item_name in combinations[0]:
            item = self.get_item_by_name(item_name)
            self.remove(item)

        self.assertAccessDependency(locs, combinations, True)