from dataclasses import dataclass
from Options import Range, Choice, OptionGroup, DefaultOnToggle, Toggle, PerGameCommonOptions

class Victory(Choice):
    """
    All: Defeat all four final bosses
    One: Defeat any one of the final bosses
    Custom: Defeat the set number of final bosses
    """
    display_name = "Victory Condition"
    option_all = 0
    option_one = 1
    option_custom = 2
    #option_mimic = 3

class CustomBossCount(Range):
    """
    Ignored unless Victory Condition is set to Custom
    Number of final bosses to kill for the victory condition.
    """
    display_name = "Custom Boss Count"
    range_start = 1
    range_end = 16
    default = 1

class DeathLinkPenalty(Choice):
    """
    Determines how the game interprets a received Death,
    assuming DeathLink is enabled.
    Deathlink can be toggled at any time in the game client.

    Damage: Take damage (amount determined by Death Link Damage)
    One health: Set health to 1
    Death: Die immediately
    """
    display_name = "Death Link Penalty"
    option_damage = 0
    option_one = 1
    option_death = 2

class DeathLinkDamage(Range):
    """
    Ignored unless Death Link Penalty is set to Damage
    Amount of damage (as a percentage) to take when receiving a Death Link, excluding shields
    """
    display_name = "Death Link Damage (Percent)"
    range_start = 10
    range_end = 100
    default = 50

class Power1Requirements(Range):
    """
    Number of Module items required for logic to assume the player is ready to beat a small encounter.
    """
    display_name = "Small Encounter Requirements"
    range_start = 1
    range_end = 20
    default = 12
    
class Power2Requirements(Range):
    """
    Number of Module items required for logic to assume the player is ready to beat an advanced encounter.
    """
    display_name = "Advanced Encounter Requirements"
    range_start = 1
    range_end = 40
    default = 20
    
class Power3Requirements(Range):
    """
    Number of Module items required for logic to assume the player is ready to beat a final boss.
    """
    display_name = "Final Boss Requirements"
    range_start = 1
    range_end = 60
    default = 40

class SmallEncounters(Range):
    """
    Number of small/regular encounters to include as location checks
    """
    display_name = "Small Encounters"
    range_start = 0
    range_end = 10
    default = 2

class AdvancedEncounters(Range):
    """
    Number of advanced encounters to include as location checks
    """
    display_name = "Advanced Encounters"
    range_start = 0
    range_end = 10
    default = 3

class EncountersUnlockShopItems(DefaultOnToggle):
    """
    Whether encounters (including final bosses) should unlock items in the shop.
    On: Bosses drop loot (such as currency) like normal, but unlock checks in the shop.
    Off: Replaces boss loot with location checks.
    """
    display_name = "Encounters Unlock Shop Items"

class SmallEncounterShopUnlocks(Range):
    """
    Number of items to unlock in the shop after completing a small encounter location check
    """
    display_name = "Small Encounter Shop Unlocks"
    range_start = 1
    range_end = 5
    default = 2

class AdvancedEncounterShopUnlocks(Range):
    """
    Number of items to unlock in the shop after completing an advanced encounter location check
    """
    display_name = "Advanced Encounter Shop Unlocks"
    range_start = 2
    range_end = 10
    default = 5

class FinalBossShopUnlocks(Range):
    """
    Number of items to unlock in the shop after completing a final boss location check
    """
    display_name = "Final Boss Shop Unlocks"
    range_start = 3
    range_end = 20
    default = 10

class GeneratorCrates(Range):
    """
    Number of location checks that are tied to generator crates
    """
    display_name = "Generator Crates"
    range_start = 5
    range_end = 20
    default = 8

class SeparateColoredCrates(Toggle):
    """
    Whether to separate colored ball crates from each other, 
    e.g., white crates and green crates count as different locations
    """
    display_name = "Separate Colored Crates"

class TotalCrates(Range):
    """
    Ignored if Separate Colored Crates is set to true.
    Total number of colored ball crates to replace with location checks
    """
    display_name = "Total Crates"
    range_start = 10
    range_end = 50
    default = 25

class WhiteCrates(Range):
    """
    Ignored if Separate Colored Crates is set to false.
    Number of location checks tied to white loot crates
    """
    display_name = "White Crates"
    range_start = 2
    range_end = 10
    default = 3
    
class GreenCrates(Range):
    """
    Ignored if Separate Colored Crates is set to false.
    Number of location checks tied to green (booster) loot crates
    """
    display_name = "Green Crates"
    range_start = 2
    range_end = 10
    default = 3
    
class OrangeCrates(Range):
    """
    Ignored if Separate Colored Crates is set to false.
    Number of location checks tied to orange (caps) loot crates
    """
    display_name = "Orange Crates"
    range_start = 2
    range_end = 10
    default = 3
    
class PinkCrates(Range):
    """
    Ignored if Separate Colored Crates is set to false.
    Number of location checks tied to pink (gel) loot crates
    """
    display_name = "Pink Crates"
    range_start = 2
    range_end = 10
    default = 3
    
class PurpleCrates(Range):
    """
    Ignored if Separate Colored Crates is set to false.
    Number of location checks tied to purple (tech) loot crates
    """
    display_name = "Purple Crates"
    range_start = 2
    range_end = 10
    default = 3

class YellowCrates(Range):
    """
    Ignored if Separate Colored Crates is set to false.
    Number of location checks tied to yellow (gold) loot crates
    """
    display_name = "Yellow Crates"
    range_start = 2
    range_end = 10
    default = 3

class FiberPlants(Range):
    """
    Number of Fiber-yielding plants to include as location checks
    """
    display_name = "Fiber Plants"
    range_start = 5
    range_end = 20
    default = 10

class GlandPlants(Range):
    """
    Number of Gland-yielding plants to include as location checks
    """
    display_name = "Gland Plants"
    range_start = 5
    range_end = 20
    default = 10

class Boxes(Range):
    """
    Number of regular (square) loot boxes to include as location checks
    """
    display_name = "Boxes"
    range_start = 0
    range_end = 50
    default = 0

punk_option_groups = [
    OptionGroup("Difficulty", [
        Power1Requirements,
        Power2Requirements,
        Power3Requirements,
    ], start_collapsed=True),
    OptionGroup("Encounters/Bosses", [
        EncountersUnlockShopItems,
        SmallEncounters,
        AdvancedEncounters,
        SmallEncounterShopUnlocks,
        AdvancedEncounterShopUnlocks,
        FinalBossShopUnlocks
    ], start_collapsed=True),
    OptionGroup("Crates", [
        SeparateColoredCrates,
        TotalCrates,
        GeneratorCrates,
        WhiteCrates,
        GreenCrates,
        OrangeCrates,
        PinkCrates,
        PurpleCrates,
        YellowCrates
    ], start_collapsed=True),
    OptionGroup("Misc Loot", [
        FiberPlants,
        GlandPlants,
        Boxes
    ], start_collapsed=True)
]

@dataclass
class PunkOptions(PerGameCommonOptions):
    victory: Victory
    custom_boss_count:  CustomBossCount
    death_link_penalty: DeathLinkPenalty
    death_link_damage: DeathLinkDamage
    power1_requirements: Power1Requirements
    power2_requirements: Power2Requirements
    power3_requirements: Power3Requirements
    small_encounters: SmallEncounters
    advanced_encounters: AdvancedEncounters
    encounters_unlock_shop_items: EncountersUnlockShopItems
    small_encounter_shop_unlocks: SmallEncounterShopUnlocks
    advanced_encounter_shop_unlocks: AdvancedEncounterShopUnlocks
    final_boss_shop_unlocks: FinalBossShopUnlocks
    generator_crates: GeneratorCrates
    separate_colored_crates: SeparateColoredCrates
    total_crates: TotalCrates
    white_crates: WhiteCrates
    green_crates: GreenCrates
    orange_crates: OrangeCrates
    pink_crates: PinkCrates
    purple_crates: PurpleCrates
    yellow_crates: YellowCrates
    fiber_plants: FiberPlants
    gland_plants: GlandPlants
    boxes: Boxes