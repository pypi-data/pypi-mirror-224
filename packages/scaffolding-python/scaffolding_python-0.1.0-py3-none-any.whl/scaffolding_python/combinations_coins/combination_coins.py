from scaffolding_python.types.types import Coin
from typing import Union


def combinations_coins(coins: list[Coin], goal: int) -> list[list[int]]:
    result: list[list[int]] = []

    def get_combination_coins(actual_coins: list[Coin], combination_coins: list[int] = []) -> None:
        actual_goal: int = goal - sum(combination_coins)
        if actual_goal == 0:
            result.append(combination_coins)
            get_combination_coins(actual_coins, [])
            return
        elif len(actual_coins) == 0:
            return

        coin = pick_coin(actual_coins, actual_goal)
        if (coin == None):
            return

        combination_coins.append(coin['value'])
        actual_coins = remove_coin(coin, actual_coins)
        return get_combination_coins(actual_coins, combination_coins)

    get_combination_coins(coins)
    return result


def pick_coin(pull: list[Coin], actual_goal: int) -> Union[Coin, None]:

    if len(pull) == 0:
        return None

    if (actual_goal - pull[0]['value'] >= 0):
        return pull[0]

    return pick_coin(pull[1:], actual_goal)


def remove_coin(coin_to_remove: Coin, pull: list[Coin]) -> list[Coin]:
    new_pull: list[Coin] = []
    for coin in pull:
        if coin['value'] == coin_to_remove['value']:
            leftover = coin['quantity'] - 1

            if leftover == 0:
                continue

            new_pull.append({
                'value':  coin['value'], 'quantity': leftover,
            })
        else:
            new_pull.append(coin)
    return new_pull
