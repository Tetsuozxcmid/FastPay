# FastPay

## Installation

Follow these steps to set up the project:

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   **On Windows:**

        ```bash
        venv/scripts/activate
        ```

    *   **On macOS and Linux:**

        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

**IMPORTANT**

Go at Stripe website and create your API Keys
  - Keys ( **Secret key "sk"** and **Publishable key "pk"**)
  - Customer ( **payment method is Card** )
  - Products ( **in this case it is subscriptions** , give them price )

1.  **Create a `.env` file:**  In the root directory of the project, create a file named `.env`.
2.  **Populate the `.env` file:** Add the following variables to your `.env` file, replacing the placeholder values with your actual Stripe API keys and IDs:

| Variable               | Description                                                                 | Example Value (Replace with your values!)                     |
| ---------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------ |
| `STRIPE_SECRET_KEY`    | Your Stripe secret API key (for server-side operations).                    | `sk_test_YOUR_SECRET_KEY`                                    |
| `CUSTOMER_ID`          | Your Stripe customer ID (for creating subscriptions or other operations). | `cus_YOUR_CUSTOMER_ID`                                       |
| `PREMIUM_PRICE_ID`     | The Stripe Price ID for your premium subscription plan.                   | `price_1234567890abcdefghijkl`                            |
| `BASIC_PRICE_ID`       | The Stripe Price ID for your basic subscription plan.                      | `price_0987654321zyxwvutsrqpon`                            |
| `STRIPE_PUBLIC_KEY`    | Your Stripe publishable key (for client-side integration).                | `pk_test_YOUR_PUBLISHABLE_KEY`                               |





