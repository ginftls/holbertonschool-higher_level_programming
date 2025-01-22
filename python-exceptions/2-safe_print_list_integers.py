def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Skip non-integer values silently
            continue
        except IndexError:
            # Stop execution if x is out of range
            break
    print()  # Print a newline after all integers
    return count
