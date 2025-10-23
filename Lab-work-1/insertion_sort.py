# Код згідно з Лістингом 4 
def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    
    # Цикл ітерується від другого елемента до кінця
    # i - це індекс елемента, який потрібно вставити
    for i in range(1, n):
        # Зберігаємо поточний елемент для вставки
        key = arr[i]
        assignments += 1
        
        # j - індекс попереднього елемента
        j = i - 1
        assignments += 1
        
        # Пересуваємо елементи, що більші за key,
        # вправо, щоб звільнити місце для вставки
        while j >= 0 and arr[j] > key:
            comparisons += 1  # Порівняння в умові while
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
            assignments += 1
            
        # Додаткове порівняння, коли умова while стає false
        # (якщо j не стало менше 0)
        if j >= 0:
            comparisons += 1
            
        # Вставляємо key на його правильне місце
        arr[j + 1] = key
        assignments += 1
        
    return arr, comparisons, assignments

## --- Приклад використання ---
##  ВАРІАНТ 20 
my_list = [86, 36, 14, 50, 64, 21, 2, 83, 82]

print(f"Оригінальний список (Варіант 20): {my_list}")

# Використання .copy(), щоб не змінювати оригінал
sorted_list, comps, assigs = insertion_sort(my_list.copy())

print(f"Відсортований список: {sorted_list}")
print(f"Кількість порівнянь: {comps}")
print(f"Кількість присвоєнь: {assigs}")
