#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    weight_list = []
    tries = set()
    for weight in weights:
        hash_table_insert(ht, weight, weights.index(weight))

        weight_list.append(weight)

    counter = 0
    for weight in weight_list:
        difference = limit - weight
        if difference in weight_list and difference != 0:
            counter += 1

            if hash_table_retrieve(ht, difference) is not None and counter < length:
                if hash_table_retrieve(ht, weight) > hash_table_retrieve(ht, difference):
                    answer = [hash_table_retrieve(ht, weight), hash_table_retrieve(ht, difference)]

                elif hash_table_retrieve(ht, weight) < hash_table_retrieve(ht, difference):

                    answer = [hash_table_retrieve(ht, difference), hash_table_retrieve(ht, weight)]

                elif hash_table_retrieve(ht, weight) == hash_table_retrieve(ht, difference):
                    answer = [hash_table_retrieve(ht, difference) + 1, hash_table_retrieve(ht, weight)]

                return answer

            if counter >= length:
                return None



    """
    YOUR CODE HERE
    """



def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
