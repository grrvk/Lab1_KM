import math


# X REPLACEMENT
def func_after_replacement(a, t, h, B):
    results = []
    while t <= B:
        try:
            y = (a*t * math.atan(a / t)) / (math.pow(t, 3) + math.pow(a, 3))
        except Exception as e:
            y = 0  # BECAUSE LIMIT OF FUNCTION IN 0 AREA IS 0
        results.append((t, y))
        t = t + h
    return results


# FUNC WITHOUT REPLACEMENT

def func_without_replacement(t, h, B):
    results = []
    while t <= B:
        y = (math.atan(t)) / (math.pow(t, 3) + 1)
        results.append((t, y))
        t = t + h
    return results


# MIDDLE RECTANGLES

def midd_rect_method(res, h):
    calculation = []
    for i, value in enumerate(res):
        if i % 2 == 1:
            calculation.append(value[1])
    result = sum(calculation) * h
    return result


def runge_calc_rect(a, N, A, B, p):
    h = (B - A) / N
    h_function_values = func_after_replacement(a, A, h / 2, B)
    i_h = midd_rect_method(h_function_values, h)

    h_div = (B - A) / (2 * N)
    h_div_function_values = func_after_replacement(a, A, h_div / 2, B)
    i_h_div = midd_rect_method(h_div_function_values, h_div)

    mark = math.fabs(i_h_div - i_h) / (math.pow(2, p) - 1)

    return mark, i_h, i_h_div, h


# SIMSON METHOD

def runge_rect(a, N, A, B, p, eps):
    print("SIMPSON METHOD")
    mark, i_h, i_h_div, h = runge_calc_rect(a, N, A, B, p)
    print(f"h = {h} ; I_h = {i_h} ; I_h/2 = {i_h_div} ; mark = {mark}")
    while mark > eps:
        N = N * 2
        mark, i_h, i_h_div, h = runge_calc_rect(a, N, A, B, p)
        print(f"h = {h} ; I_h = {i_h} ; I_h/2 = {i_h_div} ; mark = {mark}")
    return mark, i_h_div


def simps_method(res, h, N):
    lower_sum = 0
    upper_sum = 0
    for i in range(1, int(N / 2) + 1, 1):
        lower_sum += res[2 * i - 1][1]
    for i in range(1, int(N / 2), 1):
        upper_sum += res[2 * i][1]
    result = h * (res[0][1] + 4 * lower_sum + 2 * upper_sum + res[-1][1]) / 3
    return result


def runge_calc_simps(a, N, A, B, p):
    h = (B - A) / N
    h_function_values = func_after_replacement(a, A, h, B)
    i_h = simps_method(h_function_values, h, N)

    h_div = (B - A) / (2 * N)
    h_div_function_values = func_after_replacement(a, A, h_div, B)
    i_h_div = simps_method(h_div_function_values, h_div, 2 * N)

    mark = math.fabs(i_h_div - i_h) / (math.pow(2, p) - 1)

    return mark, i_h, i_h_div, h


def runge_acc_simps(a, N, A, B, p, eps):
    print("SIMPSON METHOD")
    mark, i_h, i_h_div, h = runge_calc_simps(a, N, A, B, p)
    print(f"h = {h} ; I_h = {i_h} ; I_h/2 = {i_h_div} ; mark = {mark}")
    while mark > eps:
        N = N * 2
        mark, i_h, i_h_div, h = runge_calc_simps(a, N, A, B, p)
        print(f"h = {h} ; I_h = {i_h} ; I_h/2 = {i_h_div} ; mark = {mark}")
    return mark, i_h_div


# CUT

def vrz(a):
    return float(pow(math.pi, 2) / 8 - pow(math.atan(a), 2) / 2)


def calc_a(EPS):
    print("\nCALCULATING A")
    A = 1
    while vrz(A) > EPS / 2:
        A = A + 1
    return A, vrz(A)

def runge_calc_simps_without_repl(N, A, B, p):
    h = (B - A) / N
    h_function_values = func_without_replacement(A, h, B)
    i_h = simps_method(h_function_values, h, N)

    h_div = (B - A) / (2 * N)
    h_div_function_values = func_without_replacement(A, h_div, B)
    i_h_div = simps_method(h_div_function_values, h_div, 2 * N)

    mark = math.fabs(i_h_div - i_h) / (math.pow(2, p) - 1)

    return mark, i_h, i_h_div, h


def runge_acc_simps_without_repl(N, A, B, p, eps):
    print("SIMPSON METHOD")
    mark, i_h, i_h_div, h = runge_calc_simps_without_repl(N, A, B, p)
    print(f"h = {h} ; I_h = {i_h} ; I_h/2 = {i_h_div} ; mark = {mark}")
    while mark > eps:
        N = N * 2
        mark, i_h, i_h_div, h = runge_calc_simps_without_repl(N, A, B, p)
        print(f"h = {h} ; I_h = {i_h} ; I_h/2 = {i_h_div} ; mark = {mark}")
    return mark, i_h_div
