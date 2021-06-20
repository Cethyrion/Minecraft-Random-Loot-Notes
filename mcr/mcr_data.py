from collections import defaultdict
from typing import Any, Callable, Union

from mcr.flags import MCRFlags
from mcr.loot_table_map import LootTableMap
from mcr.mc.commands.mcfunction import MCFunction
from mcr.mc.data_structures.advancement import Advancement
from mcr.mc.data_structures.recipe import CraftingShaped, Recipe


class MCRData():
    printStep: Callable[..., Any]
    printDetail: Callable[[str], Any]

    jarname: str

    flags: MCRFlags
    flagInfo: dict[str, dict[str, str]]

    seed: str
    seed_generated: bool

    datapack_name: str
    datapack_filename: str

    datapack_desc: str

    notesGrantSelector: str

    requires_cheats: list[str]
    double_tall_blocks: list[str]

    loot_table_maps: dict[str, LootTableMap] = {}
    remaining_table_names: list[str] = []

    original_to_table_name: dict[str, str] = {}

    tabs: list[str] = []
    advancements: dict[str, Advancement] = {}

    mcr_item = 'writable_book'

    tabbed_advs_and_recipes: dict[str, list[Union[Advancement, Recipe]]] = {}
    recipes: dict[str, CraftingShaped] = {}

    functions: defaultdict[str, MCFunction] = defaultdict(MCFunction)

    def __init__(self, flags: MCRFlags, flagInfo: dict[str, dict[str, str]], seed: str, seed_generated: bool, datapack_name: str):
        self.printStep = print
        self.printDetail = print

        self.flags = flags
        self.flagInfo = flagInfo
        self.seed = seed
        self.seed_generated = seed_generated
        self.datapack_name = datapack_name
