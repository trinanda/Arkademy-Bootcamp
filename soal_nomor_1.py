import json


def product():
    itemId = 12341822
    itemName = 'FGX Flannel Shirt'
    price = 195000
    availableColorAndSize = {
        'color': {'blue-black': ['M', 'L', 'XL'],
                  'black-white': ['L']}
    }

    freeShiping = False

    with open('data.json', 'w') as fp:
        json.dump(
        {'itemId': itemId,
         'itemName': itemName,
         'price': price,
         'availableColorAndSize': availableColorAndSize,
         'freeShiping': freeShiping}, fp)

if __name__ == "__main__":
    product()