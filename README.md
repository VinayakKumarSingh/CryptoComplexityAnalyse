# CryptoComplexitySite

This Django web application demonstrates a simulated implementation of an Attribute-Based Encryption (ABE) system applied to a static dataset. It provides an analysis of algorithm complexities (Key Generation, Encryption, Decryption) for CP-ABE and KP-ABE schemes, allowing users to compare theoretical (Big-O) and empirical (simulated) performance.

## Project Structure

- `CryptoComplexitySite/`: Main Django project directory.
  - `settings.py`: Project settings (includes the `analysis` app).
  - `urls.py`: Main URL configuration (routes to homepage and `analysis` app).
- `analysis/`: Django app for ABE analysis.
  - `views.py`: Contains logic for homepage, analysis form, and benchmark simulation.
  - `urls.py`: URL routes for the `analysis` app (`/analysis/`, `/analysis/run-benchmark/`).
  - `forms.py`: Defines the `BenchmarkForm` for user input.
  - `templates/analysis/`:
    - `home.html`: Project overview and ABE explanation.
    - `analysis.html`: User input form and results display (table and Chart.js chart).
  - `migrations/`: Database migrations (though not heavily used for models in this version).
- `manage.py`: Django's command-line utility.
- `README.md`: This file.

## Requirements

- Python 3.x
- Django

## Setup and Installation

1.  **Clone the repository (or ensure files are in place):**
    ```bash
    # If you had cloned it:
    # git clone <repository-url>
    # cd CryptoComplexitySite
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Django:**
    ```bash
    pip install Django
    ```
    (If you have a `requirements.txt`, you would use `pip install -r requirements.txt`)

4.  **Apply migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Running the Development Server

1.  **Start the server:**
    ```bash
    python manage.py runserver
    ```

2.  Open your web browser and navigate to:
    -   Homepage: `http://127.0.0.1:8000/`
    -   Analysis Page: `http://120.0.0.1:8000/analysis/`

## Features

-   **Homepage:** Provides an introduction to Attribute-Based Encryption (CP-ABE and KP-ABE) and its relevance.
-   **Analysis Page:**
    -   Allows users to input parameters:
        -   Static Dataset Size
        -   Number of Attributes
        -   Choice of ABE Scheme (CP-ABE or KP-ABE)
    -   Validates form input.
-   **Benchmarking:**
    -   Simulates Key Generation, Encryption, and Decryption operations.
    -   Measures and records execution times for these simulated operations.
-   **Results Display:**
    -   Presents empirical timings in a table.
    -   Displays theoretical complexities (Big-O notation) for each operation.
    -   Uses Chart.js to visualize the run-times in a bar chart.

## Simulation Details

-   The ABE operations (key generation, encryption, decryption) are **simulated** in `analysis/views.py`.
-   The simulations use `time.perf_counter()` for timing and include loops with basic arithmetic operations and `time.sleep()` to mimic computational work proportional to the input parameters (number of attributes, dataset size).
-   **These are not cryptographically secure implementations of ABE.** The goal is to demonstrate the concept of complexity analysis rather than provide a production-ready ABE library.

## Theoretical Complexities Noted

-   **CP-ABE:**
    -   Key Generation: `O(N_attr)` (Number of attributes in the universe)
    -   Encryption: `O(N_attr_policy)` (Number of attributes in the access policy)
    -   Decryption: `O(N_attr_key)` (Number of attributes in the user's key)
-   **KP-ABE:**
    -   Key Generation: `O(N_attr_key)` (Number of attributes in the user's key)
    -   Encryption: `O(N_attr_policy)` (Number of attributes the ciphertext is encrypted under)
    -   Decryption: `O(N_attr_policy)` (Number of attributes in the ciphertext policy matching the key)

## Future Extensions (Considerations)

-   **Real ABE Library:** Integrate a proper ABE library (e.g., Charm-Crypto, pycryptodome if suitable primitives exist, or custom implementation) for actual cryptographic operations.
-   **Asynchronous Tasks:** For real, potentially long-running ABE operations, use Celery or Django Channels to perform benchmarks asynchronously, preventing web server timeouts and improving user experience.
-   **More Detailed Dataset Simulation:** Allow users to define characteristics of the static dataset more granularly.
-   **Policy Complexity Input:** For CP-ABE encryption and KP-ABE decryption, allow users to specify the complexity of the access policy (e.g., number of attributes in the policy, structure of the policy).
-   **Error Handling and Logging:** Enhance error handling and implement more robust logging.

This project serves as an educational tool to explore ABE concepts and performance characteristics in a simplified, simulated environment.