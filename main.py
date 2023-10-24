import math
from functions import runge_acc_simps, runge_rect, calc_a, runge_acc_simps_without_repl

# FOR X CHANGE METHOD
A = 0  # lower boundary
B = 1  # upper boundary
N = 2  # division
# FOR CUTTING METHOD
N_CUT = 2
# SIMILAR
A_BEGINNING = 1
P_SIMPS = 4  # Порядок точності методу Сімпсона
P_RECT = 2  # Порядок точності методу середніх прямокутників
EPS = math.pow(10, -4)  # accuracy

# FOR X CHANGE METHOD

runge_res, i_h_div = runge_acc_simps(A_BEGINNING, N, A, B, P_SIMPS, EPS)
print(f"Result: I approximately is equal to {i_h_div}")
print(f"Final accuracy: {runge_res}")

print("\n")

runge_res_rect, i_h_div_rect = runge_rect(A_BEGINNING, N, A, B, P_RECT, EPS)
print(f"Result: I approximately is equal to {i_h_div_rect}")
print(f"Final accuracy: {runge_res_rect}")

# FOR CUTTING METHOD
B_CUT, value = calc_a(EPS)
print(f"Calculated A = {B_CUT}, I2 = {value}")

runge_res, i_h_div = runge_acc_simps_without_repl(N_CUT, A_BEGINNING, B_CUT, P_SIMPS, EPS/2)
print(f"Result: I1 approximately is equal to {i_h_div}")
print(f"Final accuracy: {runge_res}")

print(f"Final result: I1+I2 = {value+i_h_div}")
