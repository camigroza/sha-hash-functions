import time
import random
import string
import matplotlib.pyplot as plt
from sha_1 import *
from sha_256 import *
from sha_512 import *


def generate_random_data(size_in_kb):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size_in_kb * 1024)).encode('utf-8')

# Masoara timpul de procesare al unui algoritm SHA personalizat pentru diferite dimensiuni de date (in KB)
def benchmark_custom_algorithm(algorithm, data_sizes):
    times = []
    for size in data_sizes:
        data = generate_random_data(size)
        start_time = time.time()
        algorithm(data)
        end_time = time.time()
        times.append((end_time - start_time) * 1000)
    return times

# Genereaza graficul cu rezultatele benchmarking-ului
def plot_results(data_sizes, sha1_times, sha256_times, sha512_times):
    plt.figure(figsize=(10, 6))
    plt.plot(data_sizes, sha1_times, label="SHA-1", marker="o")
    plt.plot(data_sizes, sha256_times, label="SHA-256", marker="o")
    plt.plot(data_sizes, sha512_times, label="SHA-512", marker="o")

    plt.title("Benchmark: Performanța implementărilor SHA personalizate", fontsize=16)
    plt.xlabel("Dimensiunea datelor (KB)", fontsize=14)
    plt.ylabel("Timp de procesare (ms)", fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.savefig("sha_benchmark_results.png")
    plt.show()


def main():
    data_sizes = [1, 4, 16, 64, 256, 1024, 4096]  # Dimensiuni predefinite (în KB)
    print("Rulez benchmark pentru dimensiunile: ", data_sizes)

    print("Benchmark pentru SHA-1...")
    sha1_times = benchmark_custom_algorithm(sha1, data_sizes)

    print("Benchmark pentru SHA-256...")
    sha256_times = benchmark_custom_algorithm(sha256, data_sizes)

    print("Benchmark pentru SHA-512...")
    sha512_times = benchmark_custom_algorithm(sha512, data_sizes)

    print("\nRezultate benchmark:")
    print("Dimensiunile datelor (KB):", data_sizes)
    print("Timpii pentru SHA-1 (ms):", sha1_times)
    print("Timpii pentru SHA-256 (ms):", sha256_times)
    print("Timpii pentru SHA-512 (ms):", sha512_times)

    plot_results(data_sizes, sha1_times, sha256_times, sha512_times)


if __name__ == "__main__":
    main()
