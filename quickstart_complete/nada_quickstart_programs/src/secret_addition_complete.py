from nada_dsl import *

def nada_main():
    # Define the party
    party1 = Party(name="Party1")

    # Define the inputs as secret integers
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform an operation (multiplication in this case)
    new_int = my_int1 * my_int2

    # Output the result
    return [Output(new_int, "my_output", party=party1)]
