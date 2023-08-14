"""Make tables."""

from __future__ import annotations
from typing import Callable

import numpy as np
import pandas as pd

from risus.engine import target_number

def make_target_number_table(
        max_potency: int,
        n_faces: int = 6,
        **kwargs
) -> pd.DataFrame:

    """Make a dataframe comparing potencies to target numbers.

    This table includes all the target numbers up to the maximum possible for
    the highest potency (that is, 6*max_potency).

    # Arguments:
    * `max_potency`: The highest potency to consider.
    * `n_faces`: How many faces the dice should have.

    # Returns:
    A DataFrame whose columns are the potencies, whose rows are the target
    numbers, and whose contents are the probability (as a percentage) that a
    cliché of that potency would beat that target number.

    # Examples:
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

    >>> make_target_number_table(4, breakthrough=True)
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
    max_target_number = n_faces * max_potency

    tn_array = np.zeros((max_target_number, max_potency))
    for potency in range(1, max_potency+1):
        for tn in range(1, max_target_number+1):
            outcome = target_number(potency, tn, n_faces=n_faces, percent=True, **kwargs)
            tn_array[tn-1, potency-1] = round(outcome, 1)

    return pd.DataFrame(tn_array, range(1, max_target_number+1), range(1, max_potency+1))


def make_victory_table(
        max_potency: int,
        compare_func: Callable[..., float],
        **kwargs: bool
) -> pd.DataFrame:
    """Make a dataframe representing the chances that a given potency can beat another.

    # Arguments:
    *`max_potency`: The largest potency to go up against.
    *`compare_func`: The function to use to compare the two potencies, either
    `combat` or `single_action_conflict`.

    Also accepts keyword arguments as for `risus.engine`.

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
    >>> make_victory_table(6, combat, inappropriate=True)
           1      2      3     4     5     6
    1   50.0   10.0    1.2   0.0   0.0   0.0
    2   95.0   52.5   16.4   3.5   0.3   0.0
    3   99.9   91.8   54.1  20.7   5.7   0.8
    4  100.0   99.7   89.7  55.2  23.9   7.7
    5  100.0  100.0   99.3  88.3  56.1  26.4
    6  100.0  100.0  100.0  98.9  87.1  56.8

    >>> from risus.engine import single_action_conflict
    >>> make_victory_table(8, single_action_conflict, n_faces=8)
           1      2     3     4     5     6     7     8
    1   50.0   11.6   1.7   0.2   0.0   0.0   0.0   0.0
    2   88.4   50.0  17.9   4.6   0.9   0.1   0.0   0.0
    3   98.3   82.1  50.0  22.0   7.4   2.0   0.5   0.1
    4   99.8   95.4  78.0  50.0  24.8   9.9   3.3   0.9
    5  100.0   99.1  92.6  75.2  50.0  27.0  12.0   4.6
    6  100.0   99.9  98.0  90.1  73.0  50.0  28.6  13.9
    7  100.0  100.0  99.5  96.7  88.0  71.4  50.0  30.0
    8  100.0  100.0  99.9  99.1  95.4  86.1  70.0  50.0

    """
    chance_of_victory = np.zeros((max_potency,max_potency))

    # This is a monstrous kludge and I hate the off-by-oneness of the whole situation.
    for potency_1, potency_2 in [(x,y) for x in range(1,max_potency+1) for y in range(1,max_potency+1)]:
        outcome = compare_func(potency_1, potency_2, percent=True, **kwargs)
        chance_of_victory[potency_1-1][potency_2-1] = round(outcome, 1)

    return pd.DataFrame(chance_of_victory, range(1,max_potency+1), range(1,max_potency+1))


def make_team_victory_table(
        enemy_potency: int,
        player_potency: int = 6,
        total_helpers: int = 4,
        **kwargs
) -> pd.DataFrame:
    """Make a victory table for a team fighting with damage_policy.

    This is a seperate function from make_victory_table because the team_combat
    function has a different arity than single_action_conflict and combat.

    This function runs in
    O(`enemy_potency*player_potency**2*total_helpers`), which is to
    say, really slowly. Caching doesn't really help, since all of the
    cells of the table need to be visited in any event.

    # Arguments:
    * `enemy_potency`: The largest potency to consider in the enemy axis.
    * `player_potency`: The strongest players to consider.
    * `total_helpers`: How many helpers to allow.

    Also accepts keyword arguments as for `risus.engine.team_combat`.

    # Returns:
    A DataFrame whose first axis represents the leader's potency and
    the second the helper's. The third axis is a Series representing
    the enemy's potency.

    # Examples:
    >>> from risus.damage_policy import damage_volunteer
    >>> from risus.engine import team_combat
    >>> team_combat(2, 4, 4, damage_volunteer)
    0.7055969748511421
    >>> make_team_victory_table(4, damage_policy=damage_volunteer)[2][4][4]
    0.7055969748511421

    """
    from risus.engine import team_combat

    # Whoosh...
    res = pd.DataFrame({leader_potency: {helper_potency:
                                              pd.Series({enemy_potency:
                                                         team_combat(leader_potency,
                                                                     helper_potency,
                                                                     enemy_potency,
                                                                     **kwargs)
                                                         for enemy_potency
                                                         in range(1, enemy_potency+1)})
                                              for helper_potency
                                              in range(1, player_potency*total_helpers+1)}
                             for leader_potency
                             in range(1, player_potency+1)})
    return res
