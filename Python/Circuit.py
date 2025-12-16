a=100101
b=111001
c=100110
a_and_b=a & b
b_and_c=b & c
b_or_c=b | c
b_or_c_and_b_and_c=b_or_c & b_and_c
q=a_and_b | b_or_c_and_b_and_c
print("The Circuit is :""\n")
print("A and B\n" \
"b_and_c\n" \
"b_or_c\n" \
"_or_c_and_b_and_c\n" \
"q=a_and_b | b_or_c_and_b_and_c\n")
print("The result is :",q)
