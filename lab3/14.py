from functions import grams_to_ounces, fahrenheit_to_centigrade, solve, reverse, has_33, uniquelist, is_palindrome, histogram, guess_num

print("1. 100 grams to ounces:", grams_to_ounces(100))

print("\n2. Fahrenheit to Centigrade (98F):", fahrenheit_to_centigrade(98))

print("\n3. Solve for 35 heads and 94 legs:", solve(35, 94))

print("\n4. Reverse a sentence:", reverse("We are ready"))

print("\n5. Check if [1, 3, 3] contains consecutive 3s:", has_33([1, 3, 3]))

print("\n6. Unique list from [1, 4, 5, 2, 5, 3, 1, 5]:", uniquelist([1, 4, 5, 2, 5, 3, 1, 5]))

print("\n7. Is 'madam' a palindrome?", is_palindrome("madam"))

print("\n8. Print a histogram:")
histogram([4, 9, 7])