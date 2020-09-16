deposet_sum = float(input())
deposit_limit = int(input())
year_procent = float(input())
first_sum = deposet_sum * year_procent / 100
one_month = first_sum / 12
final_sum = deposet_sum + (deposit_limit * one_month)
print(final_sum)

