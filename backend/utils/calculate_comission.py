from sales.models import CommissionRules


def calculate_commission(product, quantity_sold, day_of_week):
    commission_rate = product.commission_rate

    try:
        rules = CommissionRules.objects.get(day_of_week=day_of_week)
        min_commission_rate = rules.min_commission_rate
        max_commission_rate = rules.max_commission_rate
    except CommissionRules.DoesNotExist:
        min_commission_rate = 0
        max_commission_rate = 10
        
    commission_rate = min(max(commission_rate, min_commission_rate), max_commission_rate)

    total_commission = product.unit_price * quantity_sold * commission_rate
    return total_commission