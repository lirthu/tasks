DISCOUNT = {
    'user_vip': {
        'order_amount': 10000,
        'discount_type': {
            'vip_high_discount': 0.85,
            'vip_low_discount': 0.9
        }
    },
    'user_standard': {
        'order_amount': 5000,
        'discount_type': {
            'standard_discount': 0.95
        }
    }
}


def calculate_discount(user, total):
    if user is None:
        return total
    if user.get("is_vip"):
        if total > DISCOUNT['user_vip']['order_amount']:
            return total * DISCOUNT['user_vip']['discount_type']['vip_high_discount']
        else:
            return total * DISCOUNT['user_vip']['discount_type']['vip_low_discount']
    else:
        if total > DISCOUNT['user_standard']['order_amount']:
            return total * DISCOUNT['user_standard']['discount_type']['standard_discount']
        else:
            return total
