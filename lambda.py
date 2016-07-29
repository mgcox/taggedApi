from __future__ import print_function

import json

import hashids

from hashids import Hashids

def reduceBrand(brand):
    newstr = brand.title()
    newstr = newstr.replace(" ", "")
    vowels = ('a', 'e', 'i', 'o', 'u')
    for index,x in enumerate(newstr.lower()):
        if index != 0 or index != len(newstr):
            if x in vowels:
                newstr = newstr.replace(x, "")


    return newstr


def hashTag(brand, sku):
    brand = reduceBrand(brand)
    hashids = Hashids()

    hashid = hashids.encode(int(sku))


    return '#' + 'tag' + brand + hashid

print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['brand'])
    print("value2 = " + event['sn'])
    brand = event['brand']
    styleNumber = event['sn']

    hashtag = hashTag(brand, styleNumber)

    return hashtag  # Echo back the first key value
    #raise Exception('Something went wrong')