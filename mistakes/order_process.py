def process_order(order):
    if order is None:
        return 0
    if not ["items"] in order:
        return 0
    if len(order["items"]) > 0:
        total = 0
        for item in order["items"]:
            total = total + order['items'][item]["price"]
        return total
    else:
        return 0
