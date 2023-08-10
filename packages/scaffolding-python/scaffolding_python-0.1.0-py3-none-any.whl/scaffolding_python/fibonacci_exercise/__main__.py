from scaffolding_python.fibonacci_exercise.fibonacci import generate_fibonacci_series
import click


@click.command()
@click.option(
    '--long',
    prompt='Longitud de la serie',
    type=int,
    default=2,
    required=False,
    help="Especifica el largo de la secuencia, ej: para generar la secuencia 0, 1, 2. Debe de escribir 3"
)
def start(long: int) -> None:
    try:
        print(generate_fibonacci_series(long))

    except (ValueError):
        print('\n\n**** Debe proporcionar un numero entero. ****\n\n')
        start()


if __name__ == '__main__':
    start()
