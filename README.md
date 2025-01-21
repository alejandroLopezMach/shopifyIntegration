# Shopify Inventory Management Script

This repository contains a Python script that uses the Shopify API to manage and retrieve information about products, variants, inventory, and store locations in a Shopify store. The script demonstrates how to interact with the Shopify API to fetch and handle data related to product inventory efficiently.

## Features

- **Fetch Products and Variants**: Retrieve detailed information about products, including their variants, inventory item IDs, titles, and prices.
- **Manage Inventory**: Fetch inventory item details in chunks of up to 50 items per request to comply with Shopify API limits.
- **Fetch Locations and Inventory Levels**: Retrieve store location details and query inventory levels at each location.
- **Error Handling**: Includes basic error handling to ensure smooth execution of API calls.

## Requirements

- Python 3.7 or higher
- Shopify Python library: Install using:
  ```bash
  pip install --upgrade shopifyapi
