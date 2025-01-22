#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Try to divide elements from both lists
            div = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except (TypeError, ValueError):
            print("wrong type")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            # Append the result to the result list
            result.append(div)
    return result
