from collections import Counter

free_products_link_with_order_type_dict = {'Order_type_X': ['1','2','3','4'], 'Order_Type_Y': ['7','8','9','10']}
selected_products_in_checkout = {'product_ids':['21', '22', '27', '29'], 'order_type': 'Order_type_X'}
test_cases = [['21','22','27', '29', '1','1', '2','3','4'],
                ['21','22','27', '29', '1', '2','3','4'],
              ['21','22','27', '29', '1','1', '2','3', '21','22','27', '29', '1','2','3','4'],
              ['21','22','27', '29', '1','2','3','4','21','22','27', '29', '1','2','3','4'],
              ['21','22','27', '29', '2','1','4']]    # generate fake test cases to prove function works

def calculate_difference_list(list_1, list_2):
    """
    :param list_1: First list
    :param list_2: second list
    :return: difference of elements present in list_2, but not in list_1
    """
    diff = Counter(list_2) - Counter(list_1)
    return dict(diff)


def check_function(selected_products_in_checkout, test_case, order_quanity=1):
    """
    :param selected_products_in_checkout: GET the list of products_id ordered in the checkout
    :param test_case: GET the list of products_id on the billing/shipping list
    :param order_quanity: ordered quantity of products in checkout
    :return: nothing, only print which products are missing and which products are extra
    expected_product ---> Using dictionary (a kind of mapping variable), link the selected_products_in_check_out to
                     free products
    """
    expected_product = selected_products_in_checkout['product_ids']
    expected_product.extend(free_products_link_with_order_type_dict[selected_products_in_checkout['order_type']])
    expected_product = expected_product*order_quanity
    print(f'Expected product list is {expected_product}')
    print(f'Products list submitted for shipment is {test_case}')
    extra_product = calculate_difference_list(expected_product, test_case)
    missing_product = calculate_difference_list(test_case, expected_product)
    print(f'Extra Products in the shipment are: {extra_product}')
    print(f'Missing Products in the shipment are: {missing_product}')


check_function(selected_products_in_checkout, test_cases[4], 1)


def add_discounted_products_check():
    return None

def add_returned_products_check():
    return None