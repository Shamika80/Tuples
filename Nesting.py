def merge_catalogs(*catalogs):
 

  merged_catalog = ()
  for catalog in catalogs:
    merged_catalog += catalog

  return merged_catalog

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

combined_catalog = merge_catalogs(catalog1, catalog2)

print("Combined Product Catalog:")
for product_name, price in combined_catalog:
  print(f"- {product_name} (${price})")