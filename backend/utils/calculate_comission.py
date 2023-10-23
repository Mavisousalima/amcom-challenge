def calculate_commission(product, quantity_sold):
    commission_rate = product.commission_rate
    min_commission_rate = 1
    max_commission_rate = 10
    commission_rate = min(max(commission_rate, min_commission_rate), max_commission_rate)

    total_commission = product.unit_price * quantity_sold * commission_rate
    return total_commission