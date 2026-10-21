DISCOUNT = {
    'user_vip' : {'vip_high_discount' : 0.85, 'vip_low_discount' : 0.9},
    'user_standard' : {'standard_discount' : 0.95}
}

def calculate_discount(user, total):
    if user is None:
        return total
    if user.get("is_vip"):
        if total > 10000:
            return total * DISCOUNT['user_vip']['vip_high_discount']
        else:
            return total * DISCOUNT['user_vip']['vip_low_discount']
    else:
        if total > 5000:
            return total * DISCOUNT['user_standard']['standard_discount']
        else:
            return total
