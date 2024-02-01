# Diffie-Hellman Key Exchange Example

This Python script demonstrates the Diffie-Hellman key exchange, a cryptographic protocol that allows two parties to securely exchange secret keys over an insecure communication channel. The script generates random prime numbers using the Sieve of Eratosthenes and implements the key exchange process.

## Usage

1. **Prime Number Generation:**
   - The script uses the Sieve of Eratosthenes to generate a list of prime numbers up to a specified limit. Adjust the `limit` variable based on your requirements.

2. **Initialization:**
   - Random prime numbers `alpha` and `beta` are chosen as the base and modulus for the Diffie-Hellman key exchange. The `initialize_alpha_beta` function ensures that these values are distinct.

3. **Secret Random Values:**
   - Both parties, labeled as A and B, choose secret random values (`x_a` and `x_b`) for the key exchange.

4. **Public Value Calculation:**
   - Public values (`y_a` and `y_b`) are calculated using the chosen alpha, beta, and secret exponents. These public values are exchanged between the parties.

5. **Shared Secret Key Calculation:**
   - Each party calculates the shared secret key using the public value received from the other party and its own secret exponent.

6. **Output:**
   - The generated alpha and beta values, as well as the secret random values, public values, and shared secret keys, are printed for both parties.

## How to Run

1. Ensure you have Python installed on your system.
2. Run the script using a Python interpreter.

```bash
python3 diffie_hellman.py
```

Adjust the `limit` variable in the script based on your desired range for prime number generation.

## Note

> This script is a basic example and may not cover all security considerations. For real-world applications, additional measures and considerations should be taken to ensure the security of the key exchange process.

Feel free to explore and modify the script to suit your specific needs and understanding of the Diffie-Hellman key exchange algorithm.