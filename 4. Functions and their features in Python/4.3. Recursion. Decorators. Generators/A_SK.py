def recursive_sum(*nums):
    if not nums:
        return 0
    return nums[0] + recursive_sum(*nums[1:])

def recursive_sum(*nums):
    if not nums:
        return 0
    return nums[0] + recursive_sum(*nums[1:])

# Ниже представлены два варианта решения задачи.
# Принципиально они похожи, и отличие только в граничном условии.
# В первом случае, вызов осуществляется даже в том, случае,
# когда куча уже оказывается пуста.
# Во втором – только до тех пор, пока мы не забрали последний кирпич.
