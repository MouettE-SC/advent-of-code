from copy import copy
from typing import Self

#               (name,            cost, damage, heal, duration, armor, damage, recharge)
magic_missile = ('Magic Missile',   53,      4,    0,        0,     0,      0,        0)
drain         = ('Drain',           73,      2,    2,        0,     0,      0,        0)
shield        = ('Shield',         113,      0,    0,        6,     7,      0,        0)
poison        = ('Poison',         173,      0,    0,        6,     0,      3,        0)
recharge      = ('Recharge',       229,      0,    0,        5,     0,      0,      101)

all_spells = (magic_missile, drain, shield, poison, recharge)


class GameState:

    def __init__(self, hp, mana, boss_hp, boss_damage):
        self.hp = hp
        self.armor = 0
        self.mana = mana
        self.boss_hp = boss_hp
        self.boss_damage = boss_damage
        self.messages = []
        self.spell_history = []
        self.active_effects = []

    def available_spells(self):
        if self.boss_hp == 0 or self.hp == 0:
            return []
        return [s for s in all_spells if self.mana >= s[1] and s[0] not in [e[0] for e in self.active_effects if e[1] > 1]]

    def __copy__(self):
        g = GameState(self.hp, self.mana, self.boss_hp, self.boss_damage)
        g.armor = self.armor
        g.messages = self.messages.copy()
        g.spell_history = self.spell_history.copy()
        g.active_effects = [e.copy() for e in self.active_effects]
        return g

    def m(self, m: str):
        self.messages.append(m)

    def apply_effects(self):
        for effect in self.active_effects:
            effect[1] -= 1
            if effect[0] == 'Shield':
                self.m(f'Shield\'s timer is now {effect[1]}.')
                if effect[1] == 0:
                    self.m(f'Shield wears off, decreasing armor by {effect[2]}.')
                    self.armor = 0
            elif effect[0] == 'Poison':
                self.boss_hp = max(0, self.boss_hp - effect[3])
                if self.boss_hp == 0:
                    self.m(f'Poison deals {effect[3]} damage; This kills the boss, and the player wins.')
                else:
                    self.m(f'Poison deals {effect[3]} damage; its timer is now {effect[1]}.')
                if effect[1] == 0:
                    self.m('Poison wears off.')
            elif effect[0] == 'Recharge':
                self.m(f'Recharge provides {effect[4]} mana; its timer is now {effect[1]}.')
                self.mana += effect[4]
                if effect[1] == 0:
                    self.m('Recharge wears off.')
        self.active_effects = [e for e in self.active_effects if e[1] > 0]

    def won(self):
        return self.boss_hp == 0

    def spent_mana(self):
        return sum([s[1] for s in self.spell_history])

    def turn(self, spell) -> Self:
        ns = copy(self)
        if ns.spell_history:
            ns.m('')
        ns.spell_history.append((spell[0], spell[1]))
        ns.m('-- Player turn --')
        ns.m(f'- Player has {ns.hp} hit point(s), {ns.armor} armor, {ns.mana} mana')
        ns.m(f'- Boss has {ns.boss_hp} hit point(s)')
        ns.hp -= 1
        if ns.hp == 0:
            ns.m('Player looses 1 hit point. This kills him and the boss wins.')
            return ns
        else:
            ns.m('Player looses 1 hit point.')
        ns.apply_effects()
        if ns.boss_hp == 0:
            return ns
        ns.mana -= spell[1]
        if spell == magic_missile:
            ns.boss_hp = max(0, ns.boss_hp - spell[2])
            if ns.boss_hp == 0:
                ns.m(f'Player casts {spell[0]}, dealing {spell[2]} damage. This kills the boss, and the player wins.')
                return ns
            else:
                ns.m(f'Player casts {spell[0]}, dealing {spell[2]} damage.')
        elif spell == drain:
            ns.boss_hp = max(0, ns.boss_hp - spell[2])
            ns.hp += spell[3]
            if ns.boss_hp == 0:
                ns.m(f'Player casts {spell[0]}, dealing {spell[2]} damage. This kills the boss, and the player wins.')
                return ns
            else:
                ns.m(f'Player casts {spell[0]}, dealing {spell[2]} damage, and healing {spell[3]} hit points.')
        elif spell == shield:
            ns.armor = spell[5]
            ns.active_effects.append([spell[0]] + list(spell)[4:])
            ns.m(f'Player casts {spell[0]}, increasing armor by {spell[5]}.')
        else:
            ns.active_effects.append([spell[0]] + list(spell)[4:])
            ns.m(f'Player casts {spell[0]}.')
        ns.m('')
        ns.m('-- Boss turn --')
        ns.m(f'- Player has {ns.hp} hit point(s), {ns.armor} armor, {ns.mana} mana')
        ns.m(f'- Boss has {ns.boss_hp} hit point(s)')
        ns.apply_effects()
        if ns.boss_hp == 0:
            return ns
        if ns.armor > 0:
            real_damage = ns.boss_damage - ns.armor
            ns.hp = max(0, ns.hp - real_damage)
            if ns.hp == 0:
                ns.m(f'Boss attacks for {ns.boss_damage} - {ns.armor} = {real_damage} damage! This kills the player and the boss wins.')
            else:
                ns.m(f'Boss attacks for {ns.boss_damage} - {ns.armor} = {real_damage} damage.')
        else:
            ns.hp = max(0, ns.hp - ns.boss_damage)
            if ns.hp == 0:
                ns.m(f'Boss attacks for {ns.boss_damage} damage! This kills the player and the boss wins.')
            else:
                ns.m(f'Boss attacks for {ns.boss_damage} damage!')
        return ns

boss = []
for l in [a.strip() for a in open('day22.input', 'r').readlines()]:
    boss.append(int(l.split(": ")[1]))


g = GameState(50, 500, boss[0], boss[1])
steps = [(g, g.available_spells())]

t = 2**31
while steps:
    s = steps[-1][1].pop()
    ng = steps[-1][0].turn(s)
    av_spells = [av_s for av_s in ng.available_spells() if ng.spent_mana() + av_s[1] < t]

    if av_spells:
        steps.append((ng, av_spells))
    else:
        if ng.won():
            t = min(t, ng.spent_mana())
        while steps and not steps[-1][1]:
            del steps[-1]

print(t)
