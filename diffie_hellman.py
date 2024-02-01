import random

random.seed()

"""
Diffie-Hellman Key Exchange Example

This script demonstrates the Diffie-Hellman key exchange with randomly generated
alpha and beta values using the Sieve of Eratosthenes for prime generation.
"""

def generate_primes(limit):
    # The Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to a given limit. 
    # Initialize a list of boolean values representing numbers from 0 to the limit
    # Initially, all numbers are marked as prime
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # Step 1: Iterate through numbers starting from 2 (the first prime)
    for i in range(2, int(limit**0.5) + 1):
        # Step 2: If the current number is marked as prime, mark its multiples as non-prime
        if is_prime[i]:
            primes.append(i)  # i is a prime number
            # Mark multiples of i as non-prime
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False

    # Step 5: Iterate through the remaining unmarked numbers
    for i in range(int(limit**0.5) + 1, limit + 1):
        # If the current number is marked as prime, add it to the list of primes
        if is_prime[i]:
            primes.append(i)

    # Step 6: Return the list of prime numbers up to the specified limit
    return primes

def initialize_alpha_beta(primes):
    alpha = random.choice(primes)
    primes.remove(alpha)  # Ensure alpha and beta are distinct
    beta = random.choice(primes)
    return alpha, beta

def generate_secret_values(limit):
    return random.randint(1,limit)

def calculate_public_values(alpha, beta, x):
    """
    Calculate the public value for a party in the Diffie-Hellman key exchange.

    Parameters:
    - alpha: The base value.
    - beta: The modulus.
    - x: The secret exponent.

    Returns:
    - The public value: alpha^x % beta
    """
    return pow(alpha, x, beta)

def calculate_shared_secret(y, x, beta):
    """
    Calculate the shared secret key in the Diffie-Hellman key exchange.

    Parameters:
    - alpha: The base value.
    - x: The secret exponent.
    - beta: The modulus.

    Returns:
    - The shared secret key: (public value from the other party)^x % beta
    """
    return pow(y, x, beta)

# alpha and beta
limit = 1000000  # Adjust the limit based on your requirements
prime_numbers = generate_primes(limit)
alpha, beta = initialize_alpha_beta(prime_numbers)

print(f"Generated alpha: {alpha}")
print(f"Generated beta: {beta}")

# Both parties generate secret random values
x_a = generate_secret_values(1000000)
x_b = generate_secret_values(1000000)
print(f"Generated secret random values for A: {x_a} and of B: {x_b}")

# Calculate public values to be exchanged
y_a = calculate_public_values(alpha, beta, x_a)
y_b = calculate_public_values(alpha, beta, x_b)
print(f"Computed public values for A: {y_a} and of B: {y_b}")
print("++++++++++++++++++++++++++++++++++++++++++++")

# Calculate shared secret keys
k_a = calculate_shared_secret(y_b, x_a, beta)
k_b = calculate_shared_secret(y_a, x_b, beta)
print(f"Computed shared secret keys for A: {k_a} and of B: {k_b}")
