"""Make tables."""

from __future__ import annotations
from typing import Callable

import numpy as np
import pandas as pd

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
    from risus.engine import target_number
    max_target_number = 6 * max_potency

    tn_array = np.zeros((max_target_number, max_potency))
    for potency in range(1, max_potency+1):
        for tn in range(1, max_target_number+1):
            tn_array[tn-1, potency-1] = round(target_number(potency, tn, True), 1)

    return pd.DataFrame(tn_array, range(1, max_target_number+1), range(1, max_potency+1))


def make_victory_table(
        max_potency: int,
        compare_func: Callable[..., float],
        inappropriate: bool = False,
        **kwargs: bool
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
    >>> from risus.engine import combat
    >>> make_victory_table(6, combat)
           1      2      3     4     5     6
    1   50.0    5.0    0.1   0.0   0.0   0.0
    2   95.0   50.0    8.2   0.3   0.0   0.0
    3   99.9   91.8   50.0  10.5   0.7   0.0
    4  100.0   99.7   89.5  50.0  12.2   1.1
    5  100.0  100.0   99.3  87.8  50.0  13.7
    6  100.0  100.0  100.0  98.9  86.3  50.0

    >>> from risus.engine import combat
    >>> make_victory_table(6, combat, True)
           1      2      3     4     5     6
    1   50.0   10.0    1.2   0.0   0.0   0.0
    2   95.0   52.5   16.4   3.5   0.3   0.0
    3   99.9   91.8   54.1  20.7   5.7   0.8
    4  100.0   99.7   89.7  55.2  23.9   7.7
    5  100.0  100.0   99.3  88.3  56.1  26.4
    6  100.0  100.0  100.0  98.9  87.1  56.8

    >>> from risus.engine import single_action_conflict
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

    # Returns:
    --------
    A numpy array with axes leader_potency, helper_potency, enemy_potency.

    # Examples:
    >>> from risus.damage_policy import damage_team_mates_only
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
    from risus.engine import team_combat
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
