import time
import random
from django.shortcuts import render
from django.http import JsonResponse
from .forms import BenchmarkForm

# Theoretical Complexities (Big-O Notation)
THEORETICAL_COMPLEXITIES = {
    'CP-ABE': {
        'key_generation': 'O(N_attr)',  # N_attr = number of attributes
        'encryption': 'O(N_attr_policy)',  # N_attr_policy = number of attributes in policy
        'decryption': 'O(N_attr_key)',  # N_attr_key = number of attributes in key
    },
    'KP-ABE': {
        'key_generation': 'O(N_attr_key)', # N_attr_key = number of attributes in key
        'encryption': 'O(N_attr_policy)', # N_attr_policy = number of attributes in ciphertext
        'decryption': 'O(N_attr_policy)', # N_attr_policy = number of attributes in ciphertext matching key
    }
}

def home_view(request):
    """Renders the homepage."""
    return render(request, 'analysis/home.html')

def analysis_view(request):
    """Renders the analysis page with the benchmark form."""
    form = BenchmarkForm()
    return render(request, 'analysis/analysis.html', {'form': form})

def run_benchmark_view(request):
    """Handles the benchmark form submission and returns results."""
    if request.method == 'POST':
        form = BenchmarkForm(request.POST)
        if form.is_valid():
            dataset_size = form.cleaned_data['dataset_size']
            num_attributes = form.cleaned_data['num_attributes']
            abe_scheme = form.cleaned_data['abe_scheme']

            # Simulate ABE operations and measure time
            key_gen_time = benchmark_key_generation(num_attributes, abe_scheme)
            encryption_time = benchmark_encryption(dataset_size, num_attributes, abe_scheme)
            decryption_time = benchmark_decryption(dataset_size, num_attributes, abe_scheme)

            results = {
                'dataset_size': dataset_size,
                'num_attributes': num_attributes,
                'abe_scheme': abe_scheme,
                'key_generation_time': key_gen_time,
                'encryption_time': encryption_time,
                'decryption_time': decryption_time,
                'theoretical_complexity': THEORETICAL_COMPLEXITIES.get(abe_scheme, {})
            }
            return JsonResponse({'success': True, 'results': results})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

# --- Benchmarking Functions (Simulations) ---
def benchmark_key_generation(num_attributes, abe_scheme):
    """
    Simulates ABE key generation and measures execution time.
    Theoretical Complexity:
        CP-ABE: O(N_attr) - Linear in the number of attributes in the universe.
        KP-ABE: O(N_attr_key) - Linear in the number of attributes associated with the key.
    """
    start_time = time.perf_counter()
    # Simulate work proportional to the number of attributes
    # In a real ABE scheme, this would involve cryptographic operations
    # (e.g., pairings, exponentiations) for each attribute.
    for _ in range(num_attributes):
        _ = pow(random.randint(1, 1000), random.randint(1, 1000), random.randint(1001, 2000)) # Simulate some computation
    # Simulate some base overhead
    time.sleep(0.001 * num_attributes) # Simplified simulation
    end_time = time.perf_counter()
    return round((end_time - start_time) * 1000, 2)  # Return time in milliseconds

def benchmark_encryption(dataset_size, num_attributes, abe_scheme):
    """
    Simulates ABE-based encryption of a static dataset.
    Theoretical Complexity:
        CP-ABE: O(N_attr_policy) - Linear in the number of attributes in the access policy.
        KP-ABE: O(N_attr_policy) - Linear in the number of attributes the ciphertext is encrypted under.
    For simulation, we'll assume policy complexity is related to num_attributes.
    The dataset_size influences the number of encryption operations if encrypting item by item,
    or the size of the data being processed if encrypting as a whole.
    """
    start_time = time.perf_counter()
    # Simulate work proportional to dataset size and attribute complexity
    # In CP-ABE, policy complexity matters. In KP-ABE, the number of attributes for the ciphertext.
    # We'll use num_attributes as a proxy for policy/ciphertext attribute count.
    # Each 'item' in the dataset requires an encryption operation.
    for _ in range(dataset_size // 100): # Simulate processing in chunks or for a sample
        for _ in range(num_attributes):
             _ = pow(random.randint(1, 1000), random.randint(1, 1000), random.randint(1001, 2000))
    time.sleep(0.0001 * dataset_size * num_attributes / 100) # Simplified simulation
    end_time = time.perf_counter()
    return round((end_time - start_time) * 1000, 2)  # Return time in milliseconds

def benchmark_decryption(dataset_size, num_attributes, abe_scheme):
    """
    Simulates ABE-based decryption.
    Theoretical Complexity:
        CP-ABE: O(N_attr_key) - Linear in the number of attributes in the user's key (for matching against policy).
        KP-ABE: O(N_attr_policy) - Linear in the number of attributes in the ciphertext policy (for matching against key).
    Similar to encryption, dataset_size affects overall time if decrypting multiple items.
    """
    start_time = time.perf_counter()
    # Simulate work proportional to dataset size and attribute complexity for decryption
    # In CP-ABE, key attributes are matched. In KP-ABE, ciphertext attributes are matched.
    for _ in range(dataset_size // 100): # Simulate processing in chunks or for a sample
        for _ in range(num_attributes):
            _ = pow(random.randint(1, 1000), random.randint(1, 1000), random.randint(1001, 2000))
    time.sleep(0.0001 * dataset_size * num_attributes / 100) # Simplified simulation
    end_time = time.perf_counter()
    return round((end_time - start_time) * 1000, 2)  # Return time in milliseconds
