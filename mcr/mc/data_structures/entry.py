from typing import List, Union, Callable
from enum import Enum

from mcr.mc.base import JsonDict
from mcr.mc.properties import json_basic, json_list
from mcr.mc.interactable import MCInteractable, MCActionInfo, eItemType, eActionType, interact_with_items, interact_with_subitems

from mcr.mc.data_structures.condition import Condition
from mcr.mc.data_structures.function import Function

class eEntry(str, Enum):
	item			= 'minecraft:item'
	tag				= 'minecraft:tag'
	loot_table		= 'minecraft:loot_table'
	group			= 'minecraft:group'
	alternatives	= 'minecraft:alternatives'
	sequence		= 'minecraft:sequence'
	dynamic			= 'minecraft:dynamic'
	empty			= 'minecraft:empty'

class eDynamic(str, Enum):
	contents = 'minecraft:contents'
	dyn_self = 'minecraft:self'


class Entry(JsonDict, MCInteractable):
	conditions:	List[Condition]	= json_list('conditions', Condition.create)
	typ:		eEntry			= json_basic('type', eEntry)
	weight:		int				= json_basic('weight', int)
	quality:	int				= json_basic('quality', int)

	def interact(self, info: MCActionInfo):
		if info.item_type == eItemType.Entry and 'children' in self:
			interact_with_items(self, 'children', info)

		elif info.item_type == eItemType.Condition:
			if 'conditions' in self:
				interact_with_items(self, 'conditions', info)
			if 'children' in self:
				interact_with_subitems(self['children'], info)
				if info.action_type is eActionType.Delete and self.typ is eEntry.alternatives and not any('conditions' in child for child in self['children']):
					self.typ = eEntry.group
			if 'functions' in self:
				interact_with_subitems(self['functions'], info)

	@staticmethod
	def create(json_body):
		typ = json_body['type']

		if typ == eEntry.item:
			return ItemEntry(json_body)

		elif typ == eEntry.tag:
			return TagEntry(json_body)

		elif typ == eEntry.loot_table:
			return LootTableEntry(json_body)

		elif typ == eEntry.group:
			return GroupEntry(json_body)

		elif typ == eEntry.alternatives:
			return AlternativesEntry(json_body)

		elif typ == eEntry.sequence:
			return SequenceEntry(json_body)

		elif typ == eEntry.dynamic:
			return DynamicEntry(json_body)

		else:
			return Entry(json_body)


class ItemEntry(Entry):
	name:		str				= json_basic('name', str)
	functions:	List[Function]	= json_list('functions', Function.create)

class TagEntry(Entry):
	name:	str		= json_basic('name', str)
	expand:	bool	= json_basic('expand', bool)

class LootTableEntry(Entry):
	name: str = json_basic('name', str)

class GroupEntry(Entry):
	children: List[Entry] = json_list('children', Entry.create)

class AlternativesEntry(Entry):
	children: List[Entry] = json_list('children', Entry.create)

class SequenceEntry(Entry):
	children: List[Entry] = json_list('children', Entry.create)

class DynamicEntry(Entry):
	name: eDynamic = json_basic('name', eDynamic)


a = property()