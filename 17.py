# one, two, three, ...
digit_sum = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4
# eleven, twelve, ...
eleven_nineteen_sum = 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
# tens
tens = 6 + 6 + 5 + 5 + 5 + 7 + 6 + 6
# 100, 200
hundred = 7
hundreds = digit_sum + 9 * hundred
# 21, 22, ..., 99
total_hundred = digit_sum + eleven_nineteen_sum + 10 * tens + 8 * digit_sum

auxand = 3
onethousand = 11

total = 99 * digit_sum + 9 * 99 * (hundred + auxand) + 10 * \
    total_hundred + hundreds + onethousand
print(total)
