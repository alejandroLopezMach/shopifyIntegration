# pip install --upgrade shopifyapi
import shopify

# En codigo de produccion estas serian variables de entorno
API_KEY = "f6e688d971b96d8f261b4e2691523453"
API_SECRET = "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"
SHOP_NAME = "alejandrocarvajaldemo"

shop_url = f"https://{API_KEY}:{API_SECRET}@{SHOP_NAME}.myshopify.com/admin/api/2023-01"
shopify.ShopifyResource.set_site(shop_url)

'''
    Esta funcion va traer los productos con sus diferentes variantes,
    Almacenara los ID de inventario e imprimira los datos de cada producto
'''
def fetch_products():
    try:
        products = shopify.Product.find()
        inventory_item_ids = []

        print("Products:")
        for product in products:
            for variant in product.variants:
                inventory_item_ids.append(variant.inventory_item_id)
                print(f"Product ID: {product.id}, Title: {product.title}, Price: {variant.price}, Inventory Item ID: {variant.inventory_item_id}")
        return inventory_item_ids
    except Exception as e:
        print(f"Error fetching products: {e}")
        return []


"""
    con los ID de inventario para cada producto podemos
    hacer fetch de estos y ver sus propiedades, El endpoint
    solo permite chunks de 50 por request, entonces primero
    toca crear los chunks para luego imprimirlos.
"""
def fetch_inventory_items(inventory_item_ids):
    try:
        chunk_size = 50
        inventory_items_data = []
        for i in range(0, len(inventory_item_ids), chunk_size):
            ids_chunk = inventory_item_ids[i:i + chunk_size]
            ids = ",".join(map(str, ids_chunk))
            inventory_items = shopify.InventoryItem.find(ids=ids)

            print("\nInventory Items:")
            for item in inventory_items:
                inventory_items_data.append(item)
                print(f"Inventory Item ID: {item.id}, SKU: {item.sku}, Tracked: {item.tracked}")
        return inventory_items_data
    except Exception as e:
        print(f"Error fetching inventory items: {e}")
        return []


"""
    Dado que Shopify separa los inventarios por ubicaciones,
    hay que hacer fetch de estas y luego traerse los inventarios
    de cada ubicacion.
"""
def fetch_inventory_levels(inventory_item_ids):
    try:
        locations = shopify.Location.find()
        print("\nLocations:")
        location_ids = []
        for location in locations:
            location_ids.append(location.id)
            print(f"Location ID: {location.id}, Name: {location.name}")

        print("\nInventory Levels:")
        for location_id in location_ids:
            inventory_levels = shopify.InventoryLevel.find(
                location_ids=location_id,
                inventory_item_ids=",".join(map(str, inventory_item_ids))
            )
            for level in inventory_levels:
                print(f"Item ID: {level.inventory_item_id}, Location ID: {level.location_id}, Quantity: {level.available}")
    except Exception as e:
        print(f"Error fetching inventory levels: {e}")


inventory_item_ids = fetch_products()
if inventory_item_ids:
    inventory_items = fetch_inventory_items(inventory_item_ids)
    fetch_inventory_levels(inventory_item_ids)
else:
    print("No inventory item IDs found.")
