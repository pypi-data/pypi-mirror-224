from scaffolding_python.combinations_coins.combination_coins import combinations_coins
from scaffolding_python.types.types import Coin
import click

coins: list[Coin] = [
    {'value': 50, 'quantity': 3},
    {'value': 20, 'quantity': 2},
    {'value': 10, 'quantity': 3},
    {'value': 5, 'quantity': 2},
]


@click.command()
@click.option(
    '--goal',
    prompt=f'Dado el la siguiente cantidad de monedas:\n {coins}\n\n ¿Cuál es la cantidad que desea que sumen las combinaciones de monedas?',
    type=int,
    help='Especifica cuanto deben de sumar cada combinación de monedas.'
)
def start(goal: int) -> None:
    try:
        combinations = combinations_coins(coins, goal)
        if (len(combinations) == 0):
            print(
                f'**** No se pueden generar posibles combinaciones para la cantidad {goal}. ****')
        else:
            print(f'Las posibles combinaciones son: \n{combinations}')

    except (ValueError):
        print('\n\n**** Debe proporcionar un numero entero. ****\n\n')
        start()


if __name__ == '__main__':
    start()
