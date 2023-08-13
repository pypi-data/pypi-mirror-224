"""Compute probabilities of outcomes for Risus: The Anything RPG.

Preston M. Firestone (c) 2023
License: GPLv3
"""

from __future__ import annotations
from doctest import testmod
from icepool import Die, d6, reduce, Reroll
from typing import Callable
import numpy as np
import pandas as pd


## The unholy trinity, the core troika of the Risus game engine:
def combat(attack_potency: int,
           enemy_potency: int,
           inappropriate: bool = False,
           percent: bool = False,
           **kwargs
) -> float:
    """Simulate basic Risus combat between two clichés of the given potencies.

    In Risus, two characters face off in combat by rolling against
    their chosen cliché: the lower roller loses one of their dice for
    the rest of the combat. In the case that the cliché that rolled
    higher is deemed "inappropriate" by the GM, then the low roller
    loses three die. See Risus page 2 for more detail.

    Arguments:
    ----------

    attack_potency -- The attacking cliché's potency; the only one that can
    be inappropriate in this function.
    enemy_potency -- The defending cliché's potency; this one can't be inappropriate.
    inappropriate -- Whether the first cliche is inappropriate.
    percent -- Whether to return the value as a percent.

    Returns:
    --------
    The chance (potentially as a percent) that the attacker beats the enemy.

    Examples:
    ---------
    >>> round(combat(4,3), 3)
    0.895
    """
    outcome = _combat(attack_potency, enemy_potency, inappropriate)
    return outcome.probabilities(percent=percent)[True]


# This is fancy enough to deserve to be its own procedure, even though in the
# Risus rules it's considered a special case of ordinary combat.
def team_combat(
        leader_potency: int,
        helper_potency: int,
        enemy_potency: int,
        damage_policy: Callable[[int, int], tuple[int]],
        percent: bool = False,
        inappropriate: bool = False,
        **kwargs
) -> float:
    """Simulate team combat.

    This procedure simply counts leader death as loss without attempting to
    reform the team and does not implement the double-damage self-sacrifice.

    Parameters:
    -----------
    leader_potency -- The potency of the team leader's cliché.
    helper_potency -- The total potency of the helpers' clichés.
    enemy_potency -- The potency of the enemy's cliché.
    damage_policy -- A function that takes the leader's and helpers' potencies
    and applies damage to them, returning a new pair of potencies.
    percent -- Whether or not to return the probability as a percent.
    inappropriate -- Whether or not all the team's clichés are inappropriate.

    Returns:
    --------
    The probability (potentially as a percentage) that the team is victorious.

    Examples:
    ---------
    >>> team_combat(4,0,4, damage_team_mates_only)
    0.5
    """
    outcome = _team_combat(leader_potency, helper_potency, enemy_potency,
                           damage_policy, inappropriate)
    return outcome.probabilities(percent=percent)[1]


def single_action_conflict(
        attack_potency: int,
        enemy_potency: int,
        percent: bool = False,
        **kwargs
) -> float:
    """Compute the chances of victory in a single-action conflict.

    The winner of a single action conflict is simply the higher roller. See
    Risus page 3.

    Arguments:
    ----------
    attack_potency -- The potency of the cliché whose chance of victory to compute.
    enemy_potency -- The potency of the cliché they're up against.
    percent -- Whether or not to return the value as a percent.

    Returns:
    --------
    The probability (potentially as a percent) that the attacker is victorious.

    examples:
    >>> round(single_action_conflict(4,3, True), 1)
    79.5

    >>> single_action_conflict(1,6)
    0.0
    """
    pool_1 = attack_potency @ d6
    pool_2 = enemy_potency @ d6

    res_die = reduce(lambda a,b: Reroll if a == b else a > b, [pool_1, pool_2]).simplify()
    # Catch a weird corner case where there's an automatic victory and so the
    # return is ill-formed:
    if attack_potency >= 6 * enemy_potency:
        res_die = Die({True: 1, False: 0})
    if enemy_potency >= 6 * attack_potency:
        res_die = Die({True: 0, False: 1})

    return res_die.probabilities(percent=percent)[1]


def target_number(
        potency: int,
        difficulty: int,
        percent: bool = False
) -> float:
    """Compute the probability that a cliché with this potency will meet or exceed the target difficulty.

    True represents success, and False failure."""
    res_die = potency @ d6 >= difficulty
    # Catch a weird corner case where there's an automatic victory and so the
    # return is ill-formed:
    if potency >= difficulty:
        # Auto-success.
        res_die = Die({True: 1, False: 0})
    if difficulty > 6 * potency:
        # Auto-failure
        res_die = Die({True: 0, False: 1})

    return res_die.probabilities(percent=percent)[1]


## Team combat damage policy functions.
def damage_team_mates_only(leader_potency: int, helper_potency: int) -> tuple[int, int]:
    """Deduct one from the helpers, unless there are no more helpers.

    Examples:
    ---------
    >>> damage_team_mates_only(4, 3)
    (4, 2)

    >>> damage_team_mates_only(5, 0)
    (4, 0)
    """
    return (leader_potency, helper_potency-1) if helper_potency else (leader_potency-1,helper_potency)


def damage_volunteer(leader_potency: int, helper_potency: int) -> tuple[int, int]:
    """Deal double damage to a helper if they can take it, then the
    leader if they can take it, then fall back on dealing one damage
    to whoever can absorb it.

    Examples:
    ---------
    >>> damage_volunteer(4, 5)
    (4, 3)

    >>> damage_volunteer(4, 1)
    (2, 1)

    >>> damage_volunteer(2, 1)
    (2, 0)
    """
    if helper_potency >= 2:
        return (leader_potency, helper_potency-2)

    elif leader_potency > 2:
        return (leader_potency-2, helper_potency)

    elif helper_potency > 0:
        return (leader_potency, helper_potency-1)

    else:
        return (leader_potency-1, helper_potency)


## Functions to make tables of probabilities.
def make_target_number_table(
        max_potency: int
) -> pd.DataFrame:

    """Make a dataframe comparing potencies to target numbers.

    This table includes all the target numbers up to the maximum possible for
    the highest potency (that is, 6*max_potency).

    Arguments:
    ----------
    max_potency -- The highest potency to consider.

    Returns:
    --------
    A DataFrame whose columns are the potencies, whose rows are the target
    numbers, and whose contents are the probability (as a percentage) that a
    cliché of that potency would beat that target number.

    Examples:
    ---------
    >>> make_target_number_table(4)
            1      2      3      4
    1   100.0  100.0  100.0  100.0
    2    83.3  100.0  100.0  100.0
    3    66.7   97.2  100.0  100.0
    4    50.0   91.7   99.5  100.0
    5    33.3   83.3   98.1   99.9
    6    16.7   72.2   95.4   99.6
    7     0.0   58.3   90.7   98.8
    8     0.0   41.7   83.8   97.3
    9     0.0   27.8   74.1   94.6
    10    0.0   16.7   62.5   90.3
    11    0.0    8.3   50.0   84.1
    12    0.0    2.8   37.5   76.1
    13    0.0    0.0   25.9   66.4
    14    0.0    0.0   16.2   55.6
    15    0.0    0.0    9.3   44.4
    16    0.0    0.0    4.6   33.6
    17    0.0    0.0    1.9   23.9
    18    0.0    0.0    0.5   15.9
    19    0.0    0.0    0.0    9.7
    20    0.0    0.0    0.0    5.4
    21    0.0    0.0    0.0    2.7
    22    0.0    0.0    0.0    1.2
    23    0.0    0.0    0.0    0.4
    24    0.0    0.0    0.0    0.1
    """
    max_target_number = 6 * max_potency

    tn_array = np.zeros((max_target_number, max_potency))
    for potency in range(1, max_potency+1):
        for tn in range(1, max_target_number+1):
            tn_array[tn-1, potency-1] = round(target_number(potency, tn, True), 1)

    return pd.DataFrame(tn_array, range(1, max_target_number+1), range(1, max_potency+1))


def make_victory_table(
        max_potency: int,
        compare_func: Callable[[int, int], float],
        inappropriate: bool = False
) -> pd.DataFrame:
    """Make a dataframe representing the chances that a given potency can beat another.

    Arguments:
    ----------
    max_potency -- The largest potency to go up against.
    compare_func -- The function to use to compare the two potencies, either
    `combat` or `single_action_conflict`.
    inappropriate -- Whether or not the attacking cliche is inappropriate

    Returns:
    --------
    A dataframe representing the chances that the row potency can beat the column potency in combat.

    Examples:
    ---------
    >>> make_victory_table(6, combat)
           1      2      3     4     5     6
    1   50.0    5.0    0.1   0.0   0.0   0.0
    2   95.0   50.0    8.2   0.3   0.0   0.0
    3   99.9   91.8   50.0  10.5   0.7   0.0
    4  100.0   99.7   89.5  50.0  12.2   1.1
    5  100.0  100.0   99.3  87.8  50.0  13.7
    6  100.0  100.0  100.0  98.9  86.3  50.0

    >>> make_victory_table(6, combat, True)
           1      2      3     4     5     6
    1   50.0   10.0    1.2   0.0   0.0   0.0
    2   95.0   52.5   16.4   3.5   0.3   0.0
    3   99.9   91.8   54.1  20.7   5.7   0.8
    4  100.0   99.7   89.7  55.2  23.9   7.7
    5  100.0  100.0   99.3  88.3  56.1  26.4
    6  100.0  100.0  100.0  98.9  87.1  56.8

    >>> make_victory_table(6, single_action_conflict)
           1     2     3     4     5     6
    1   50.0  10.0   1.2   0.1   0.0   0.0
    2   90.0  50.0  16.3   3.7   0.6   0.1
    3   98.8  83.7  50.0  20.5   6.3   1.5
    4   99.9  96.3  79.5  50.0  23.5   8.6
    5  100.0  99.4  93.7  76.5  50.0  25.7
    6  100.0  99.9  98.5  91.4  74.3  50.0

    """
    chance_of_victory = np.zeros((max_potency,max_potency))

    # This is a monstrous kludge and I hate the off-by-oneness of the whole situation.
    for potency_1, potency_2 in [(x,y) for x in range(1,max_potency+1) for y in range(1,max_potency+1)]:
        outcome = compare_func(potency_1, potency_2, percent=True, inappropriate=inappropriate)
        chance_of_victory[potency_1-1][potency_2-1] = round(outcome, 1)

    return pd.DataFrame(chance_of_victory, range(1,max_potency+1), range(1,max_potency+1))


def make_team_victory_table(
        max_potency: int,
        damage_policy: Callable[[int, int], tuple[int, int]],
        inappropriate: bool = False
) -> np.ndarray:
    """Make a victory table for a team fighting with damage_policy.

    This is a seperate function from make_victory_table because the team_combat
    function has a different arity than single_action_conflict and combat.

    FIXME: figure out how to get this into a nice DataFrame, or decide
    that some other datastructure is better suited to the present
    problem.

    Returns:
    --------
    A numpy array with axes leader_potency, helper_potency, enemy_potency.

    Examples:
    ---------
    >>> make_team_victory_table(4, damage_team_mates_only)
    array([[[ 79.8,  21.2,   1.5,   0. ],
            [ 93.4,  44.5,   7.2,   0.3],
            [ 98.2,  66.8,  19.1,   1.9],
            [ 99.6,  83.1,  36.4,   6.3]],
    <BLANKLINE>
           [[ 99.6,  79. ,  26.7,   2.8],
            [100. ,  92.7,  49.9,  10.1],
            [100. ,  97.9,  70.7,  23.6],
            [100. ,  99.5,  85.2,  41.3]],
    <BLANKLINE>
           [[100. ,  98.9,  78.2,  30.2],
            [100. ,  99.9,  92.1,  53.1],
            [100. , 100. ,  97.6,  72.8],
            [100. , 100. ,  99.4,  86.3]],
    <BLANKLINE>
           [[100. , 100. ,  98.2,  77.5],
            [100. , 100. ,  99.7,  91.5],
            [100. , 100. , 100. ,  97.3],
            [100. , 100. , 100. ,  99.3]]])

    """
    chance_of_victory = np.zeros((max_potency, max_potency, max_potency))
    potency_combos = [(x, y, z)
                      for x in range(1, max_potency+1)
                      for y in range(1, max_potency+1)
                      for z in range(1, max_potency+1)]

    # This is a monstrous kludge and I hate the off-by-oneness of the whole situation.
    for leader, helper, enemy  in potency_combos:
        outcome = team_combat(leader, helper, enemy, damage_policy, inappropriate=inappropriate, percent=True)
        chance_of_victory[leader-1][helper-1][enemy-1] = round(outcome, 1)

    return chance_of_victory


# Internal computers. These return Icepool Die, since they are implemented recursively.
def _combat(
        attack_potency: int,
        enemy_potency: int,
        inappropriate: bool = False,
        **kwargs
) -> Die:
    """Internal combat calculator.

    Returns:
    --------
    A Die where True is the number of victorious cases and False the number of defeats.

    """
    damage = 3 if inappropriate else 1

    # Base cases.
    if attack_potency <= 0 and enemy_potency > 0:
        # 2 wins.
        return Die({False: 1, True: 0})

    if attack_potency > 0 and enemy_potency <= 0:
        # 1 wins.
        return Die({False: 0, True: 1})

    pool_1 = attack_potency @ d6
    pool_2 = enemy_potency @ d6

    # Recursive calls.
    victory_1 = _combat(attack_potency, enemy_potency-damage)
    victory_2 = _combat(attack_potency-1, enemy_potency)

    # Reroll ties and otherwise figure out how many times each side would win.
    outcome = reduce(lambda a,b: Reroll if a == b else a > b, [pool_1, pool_2])

    # Drill down into the inner calls.
    return (outcome).if_else(victory_1, victory_2).simplify()


def _team_combat(
        leader_potency: int,
        helper_potency: int,
        enemy_potency: int,
        damage_policy: Callable[[int, int], tuple[int]],
        inappropriate: bool = False,
        volunteered: bool = False,
        **kwargs
) -> Die:
    """Team combat internal helper.

    Arguments:
    ----------
    All as `team_combat`.
    volunteered -- Whether or not the leader's potency was doubled by a volunteer.

    Returns:
    --------
    A Die representing victory or defeat.

    """
    # Initialize dice pools and local variables.
    help_die = Die([0,0,0,0,0,6])  # Used by non-leaders when teaming up.
    damage = 3 if inappropriate else 1
    leader_pool = 2*leader_potency @ d6 if volunteered else leader_potency @ d6
    helper_pool = helper_potency @ help_die
    team_pool = leader_pool + helper_pool
    enemy_pool = enemy_potency @ d6

    # Base cases:
    if leader_potency > 0 and enemy_potency <= 0:
        # Team victory!
        return Die({True: 1, False: 0})

    if leader_potency <= 0 and enemy_potency > 0:
        # Enemy victory!
        return Die({True: 0, False: 1})

    # Compute outcome and results of combat.
    outcome = reduce(lambda a,b: Reroll if a == b else a > b, [team_pool, enemy_pool])

    team_victory = lambda: _team_combat(leader_potency, helper_potency, enemy_potency-damage,
                                        damage_policy, inappropriate)

    damaged_leader, damaged_helper = damage_policy(leader_potency, helper_potency)

    if damaged_leader == leader_potency - 2 or damaged_helper == helper_potency - 2:
        volunteered = True
    else:
        volunteered = False

    enemy_victory = lambda: _team_combat(damaged_leader, damaged_helper, enemy_potency,
                                         damage_policy, inappropriate, volunteered)

    return outcome.if_else(team_victory(), enemy_victory()).simplify()


testmod()
