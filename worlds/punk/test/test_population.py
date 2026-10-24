from .bases import PunkTestBase
from ..options import preset_minimum

class TestPopulation(PunkTestBase):
    options = preset_minimum

    def test_population(self):
        regions = self.world.get_regions()

        for region in regions:
            print(f"{region.name} has {len(region.locations)} locations")