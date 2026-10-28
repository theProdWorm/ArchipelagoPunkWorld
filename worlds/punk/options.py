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

class GeneratorCaches(Range):
    """
    Number of location checks that are tied to generator caches
    """
    display_name = "Generator Caches"
    range_start = 5
    range_end = 20
    default = 8

class SeparateColoredCaches(Toggle):
    """
    Whether to separate colored caches from each other, 
    e.g., white caches and purple caches count as different locations
    """
    display_name = "Separate Colored Caches"

class TotalCaches(Range):
    """
    Ignored if Separate Colored Caches is set to true.
    Total number of colored caches to replace with location checks
    """
    display_name = "Total Caches"
    range_start = 10
    range_end = 50
    default = 25

class WhiteCaches(Range):
    """
    Ignored if Separate Colored Caches is set to false.
    Number of location checks tied to white loot caches
    """
    display_name = "White Caches"
    range_start = 2
    range_end = 10
    default = 3
    
class GreenCaches(Range):
    """
    Ignored if Separate Colored Caches is set to false.
    Number of location checks tied to green loot caches
    """
    display_name = "Green Caches"
    range_start = 2
    range_end = 10
    default = 3
    
class OrangeCaches(Range):
    """
    Ignored if Separate Colored Caches is set to false.
    Number of location checks tied to orange loot caches
    """
    display_name = "Orange Caches"
    range_start = 2
    range_end = 10
    default = 3
    
class PinkCaches(Range):
    """
    Ignored if Separate Colored Caches is set to false.
    Number of location checks tied to pink loot caches
    """
    display_name = "Pink Caches"
    range_start = 2
    range_end = 10
    default = 3
    
class PurpleCaches(Range):
    """
    Ignored if Separate Colored Caches is set to false.
    Number of location checks tied to purple loot caches
    """
    display_name = "Purple Caches"
    range_start = 2
    range_end = 10
    default = 3

class YellowCaches(Range):
    """
    Ignored if Separate Colored Caches is set to false.
    Number of location checks tied to yellow loot caches
    """
    display_name = "Yellow Caches"
    range_start = 2
    range_end = 10
    default = 3

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

class LootCrates(Range):
    """
    Number of regular (square) loot crates to include as location checks
    """
    display_name = "Loot Crates"
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
        SmallEncounters,
        AdvancedEncounters,
        SmallEncounterShopUnlocks,
        AdvancedEncounterShopUnlocks,
        FinalBossShopUnlocks
    ], start_collapsed=True),
    OptionGroup("Caches", [
        SeparateColoredCaches,
        TotalCaches,
        GeneratorCaches,
        WhiteCaches,
        GreenCaches,
        OrangeCaches,
        PinkCaches,
        PurpleCaches,
        YellowCaches
    ], start_collapsed=True),
    OptionGroup("Misc Loot", [
        FiberPlants,
        GlandPlants,
        LootCrates
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
    small_encounter_shop_unlocks: SmallEncounterShopUnlocks
    advanced_encounter_shop_unlocks: AdvancedEncounterShopUnlocks
    final_boss_shop_unlocks: FinalBossShopUnlocks
    generator_caches: GeneratorCaches
    separate_colored_caches: SeparateColoredCaches
    total_caches: TotalCaches
    white_caches: WhiteCaches
    green_caches: GreenCaches
    orange_caches: OrangeCaches
    pink_caches: PinkCaches
    purple_caches: PurpleCaches
    yellow_caches: YellowCaches
    small_encounters: SmallEncounters
    advanced_encounters: AdvancedEncounters
    fiber_plants: FiberPlants
    gland_plants: GlandPlants
    loot_crates: LootCrates

preset_minimum = {
    Victory: Victory.option_one,
    CustomBossCount: CustomBossCount.range_start,
    DeathLinkPenalty: DeathLinkPenalty.option_damage,
    SmallEncounterShopUnlocks: SmallEncounterShopUnlocks.range_start,
    AdvancedEncounterShopUnlocks: AdvancedEncounterShopUnlocks.range_start,
    FinalBossShopUnlocks: FinalBossShopUnlocks.range_start,
    GeneratorCaches: GeneratorCaches.range_start,
    SeparateColoredCaches: False,
    TotalCaches: TotalCaches.range_start,
    WhiteCaches: WhiteCaches.range_start,
    GreenCaches: GreenCaches.range_start,
    OrangeCaches: OrangeCaches.range_start,
    PinkCaches: PinkCaches.range_start,
    PurpleCaches: PurpleCaches.range_start,
    YellowCaches: YellowCaches.range_start,
    SmallEncounters: SmallEncounters.range_start,
    AdvancedEncounters: AdvancedEncounters.range_start,
    FiberPlants: FiberPlants.range_start,
    GlandPlants: GlandPlants.range_start,
    LootCrates: LootCrates.range_start
}