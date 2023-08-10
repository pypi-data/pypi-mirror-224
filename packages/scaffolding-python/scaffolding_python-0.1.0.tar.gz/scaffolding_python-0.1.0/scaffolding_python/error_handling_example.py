from scaffolding_python.decorators.error_handling import log_errors
import click


@log_errors
def division(x: int, y: int) -> float:
    return x / y


@click.command()
@click.option(
    '--x',
    prompt='Primer número',
    type=int,
    help="Dividendo"
)
@click.option(
    '--y',
    prompt='Segundo número',
    type=int,
    help="Divisor"
)
def start(x: int, y: int) -> None:
    print(f"El resultado de la división es: {division(x, y)}")


start()
