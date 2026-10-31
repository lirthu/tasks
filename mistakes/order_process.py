def process_order(order):
    if order is None:
        return 0
    if "items" not in order:
        return 0
    if len(order["items"]) > 0:
        total = sum([item["price"] for item in order["items"].values()])
        return total
    else:
        return 0
