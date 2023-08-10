import logging
import time

# Cuando usamos este decorador, cualquier función que encuentre un error registrará ese error antes de que se genere.
# Ejemplo de uso:
# @log_errors
# def divide(x, y):
#    return x / y


def log_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            function_name = getattr(func, "__name__", "UnknownFunction")
            logging.error(
                f"Error in {function_name}: {e}", exc_info=True)

    return wrapper


# El retry_on_failure decorador captará cualquier excepción especificada en la exceptions tupla.
# Si la función falla, registra una advertencia, espera un retraso específico (delay) y luego vuelve a intentarlo.
# Si la función aún falla después del número máximo de intentos (max_retries), registra un error.
# Ejemplo de uso:
# @retry_on_failure(max_retries=5, delay=2, exceptions=(ConnectionError,))
# def send_network_request():
#    # Code to send a network request
#    ...
# Algunas expeciones útiles:DatabaseConnectionError, APILimitError


def retry_on_failure(max_retries=3, delay=1, exceptions=(Exception,)):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                function_name = getattr(
                    func, "__name__", "UnknownFunction")
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logging.warning(
                        f"Failed to execute {function_name}. Retrying in {delay}s. Error: {e}")
                    time.sleep(delay)
            logging.error(
                f"Failed to execute {function_name} after {max_retries} attempts.", exc_info=True)
        return wrapper
    return decorator
