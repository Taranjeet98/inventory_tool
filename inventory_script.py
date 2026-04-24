import csv

# Open the data file
with open('inventory_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    
    print("Items that need reordering:")
    
    for row in reader:
        # 1. Clean the data (remove extra spaces)
        raw_stock = row['stock_level'].strip().lower()
        
        # 2. Check if it's "Out of Stock" OR if it's totally empty ('')
        if raw_stock == "out of stock" or raw_stock == "":
            stock = 0
        else:
            try:
                stock = float(raw_stock)
            except ValueError:
                # If the data is still weird, skip this item
                continue
            
        # 3. Check the threshold
        # We use try/except here too in case reorder_threshold is missing
        try:
            threshold = float(row['reorder_threshold'])
            if stock < threshold:
                print(f"ID: {row['product_id']} | Category: {row['category']}")
        except ValueError:
            continue