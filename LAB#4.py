import random
import time

def print_matrix(M, matr_name, tt):
    print("матрица " + matr_name + " промежуточное время = " + str(format(tt, '0.2f')) + " seconds.")
    for i in M:  # делаем перебор всех строк матрицы
        for j in i:  # перебираем все элементы в строке
            print("%5d" % j, end=' ')
        print()

print("\n-----Результат работы программы-------")
try:
    row_q = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    while row_q < 6 or row_q > 100:
        row_q = int(input(
            "Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    K = int(input("Введите число К="))
    start = time.time()
    A, F, AF, FT = [], [], [], []  # задаем матрицы
    for i in range(row_q):
        A.append([0] * row_q)
        F.append([0] * row_q)
        AF.append([0] * row_q)
        FT.append([0] * row_q)
    time_next = time.time()
    print_matrix(F, "F", time_next - start)

    for i in range(row_q):  # заполняем матрицу А
        for j in range(row_q):
            # A[i][j] = random.randint(1, 5)
            if i < j and j < row_q-1-i:
                A[i][j] = 1
            elif i < j and j > row_q-1-i:
                A[i][j] = 2
            elif i > j and j > row_q-1-i:
                A[i][j] = 3
            elif i > j and j < row_q-1-i:
                A[i][j] = 4

    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "A", time_next - time_prev)
    for i in range(row_q):  # F
        for j in range(row_q):
            F[i][j] = A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)

    C = []  # задаем матрицу C
    size = row_q // 2
    for i in range(size):
        C.append([0] * size)

    for i in range(size):  # формируем подматрицу С
        for j in range(size):
            C[i][j] = F[i][size + row_q % 2 + j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(C, "C", time_next - time_prev)

# произведение чисел по периметру области 2

    quantity = 0
    multiplication = 1
    point = 0
    for x in range(size - 1, size // 2 - 1, -1):  # обрабатываем подматрицу C и считаем периметр снизу "треугольника"
        for y in range(size - 1, size // 2, -1):
            multiplication *= C[x][-1 - point]
            point += 1
            break
    # прошли через границу симметрии и считаем периметр сверху "треугольника"
    if size % 2 == 1:                                 #центр есть - идем по диагоналям
        point = 1
        for x in range(size // 2 - 1, 0 - 1, -1):
            for y in range(size // 2 + 1, size, 1):
                multiplication *= C[x][size // 2 + point]
                point += 1
                break
    else:                                             #центра нет - "перепрыгиваем" через него, продолжая идти по периметру
        point = 0
        for x in range(size // 2 - 1, 0 - 1, -1):
            for y in range(size // 2, size, 1):
                multiplication *= C[x][(size // 2) + point]
                point += 1
                break

    for i in range(1, size-1):  #добавляем к произведению основание периметра "треугольника"
        for j in range(size):
            point=0
            multiplication *= C[i+point][size-1]
            point+=1
            break

# сумма чисел, по периметру области 3

    summa = 0
    ppp = 0

    for x in range(size - 1, size // 2 - 1, -1):  # обрабатываем подматрицу C и считаем периметр "треугольника" справа
        for y in range(size - 1, size // 2, -1):
            summa += C[x][-1 - point]
            point += 1
            break
    # прошли через границу симметрии и считаем периметр "треугольника" слева
    if size % 2 == 0:                                #центр есть - идем по диагоналям
        point = 1
        for x in range(size // 2, size):
            for y in range(size // 2 - 1, 0-1, -1):
                summa += C[x][size // 2 - point]
                point += 1
                break
    else:                                             #центра нет - "перепрыгиваем" через него, продолжая идти по периметру
        point = 0
        for x in range(size // 2, size):
            for y in range(size // 2 - 1, 0 - 1, -1):
                summa += C[x][size // 2 - point]
                point += 1
                break

    for i in range(size):  #добавляем к произведению основание периметра "треугольника"
        for j in range(1, size - 1):
            point = 0
            summa += C[size-1][j-point]
            point += 1
        break

    if summa > multiplication:
        print("Случай 1")
        for i in range(size // 2):              #меняем 1 и 3 области симметрично
            for j in range(size):
                b1 = j >= i
                b2 = j <= size - 1 - i
                if b1 and b2:
                    C[i][j], C[size - 1 - i][j] = C[size - 1 - i][j], C[i][j]
    else:                                       #меняем матрицы B и E несимметрично
        print("Случай 2")
        for j in range(0, row_q // 2 + row_q % 2 - 1, 1):
            for i in range(row_q // 2):
                F[i][j], F[i][row_q // 2 + row_q % 2 + j] = F[i][row_q // 2 + row_q % 2+j], F[i][j]
    print_matrix(C, "C", time_next - time_prev)

    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)
    print_matrix(A, "A", 0)

    # считаем пример (A*F)+(K*FT) по действиям
    for i in range(row_q):  # F*A
        for j in range(row_q):
            AF[i][j] = F[i][j] * A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "K*A", time_next - time_prev)

    for i in range(row_q):  # FT
        for j in range(i, row_q, 1):
            FT[i][j], FT[j][i] = F[j][i], F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(FT, "F^T", time_next - time_prev)

    for i in range(row_q):  # K*FT
        for j in range(row_q):
            FT[i][j] = K * FT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(FT, "K*F^T", time_next - time_prev)

    for i in range(row_q):  # A*F+ K*FT
        for j in range(row_q):
            AF[i][j] = AF[i][j] + FT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF, "A*F + K*FT", time_next - time_prev)

    finish = time.time()
    result = finish - start
    print("Program time: " + str(result) + " seconds.")

except ValueError:
   print("\nэто не число")

except FileNotFoundError:
    print(
        "\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл
