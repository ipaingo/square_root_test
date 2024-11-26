### План тестирования функции `get_square_roots`

#### Тест 1: `test_a_is_zero`  
- **Цель:** Проверить работу функции при `a = 0`.  
- **Входные данные:** `a = 0`, `b = 8`, `c = 16`.  
- **Ожидаемый результат:** `(-2)` — кортеж с одним элементом.  
- **Описание процесса:** Вызывается функция, проверяется тип результата (кортеж) и его длина, затем точность вычисления.

---

#### Тест 2: `test_a_is_zero_b_is_zero`  
- **Цель:** Проверить поведение функции при `a = 0` и `b = 0`.  
- **Входные данные:** `a = 0`, `b = 0`, `c = 8`.  
- **Ожидаемый результат:** `()` — пустой кортеж.  
- **Описание процесса:** Проверяется, что результат пуст.

---

#### Тест 3: `test_b_is_zero_c_negative`  
- **Цель:** Проверить вычисления при `b = 0` и `c < 0`.  
- **Входные данные:** `a = 2`, `b = 0`, `c = -32`.  
- **Ожидаемый результат:** `(-4, 4)` — кортеж из двух элементов.  
- **Описание процесса:** Проверяется тип, длина и значения результата с заданной точностью.

---

#### Тест 4: `test_b_is_zero_c_is_zero`  
- **Цель:** Проверить вычисления при `b = 0` и `c = 0`.  
- **Входные данные:** `a = 123`, `b = 0`, `c = 0`.  
- **Ожидаемый результат:** `(0)` — кортеж с одним элементом.  
- **Описание процесса:** Проверяется тип, длина и значение результата.

---

#### Тест 5: `test_b_is_zero_c_positive`  
- **Цель:** Проверить поведение функции при `b = 0` и `c > 0`.  
- **Входные данные:** `a = 3`, `b = 0`, `c = 9`.  
- **Ожидаемый результат:** `()` — пустой кортеж.  
- **Описание процесса:** Проверяется, что результат пуст.

---

#### Тест 6: `test_c_is_zero`  
- **Цель:** Проверить поведение функции при `c = 0`.  
- **Входные данные:** `a = 3`, `b = 6`, `c = 0`.  
- **Ожидаемый результат:** `(0, -2)` — кортеж из двух элементов.  
- **Описание процесса:** Проверяется тип результата, длина и точность вычисления.

---

#### Тест 7: `test_all_zero`  
- **Цель:** Проверить поведение функции при `a = 0`, `b = 0`, `c = 0`.  
- **Входные данные:** `a = 0`, `b = 0`, `c = 0`.  
- **Ожидаемый результат:** `("any")` — кортеж с одним элементом.  
- **Описание процесса:** Проверяется, что результат содержит строку "any".

---

#### Тест 8: `test_d_greater_than_zero`  
- **Цель:** Проверить вычисления при дискриминанте > 0.  
- **Входные данные:**  
  - `a = 4`, `b = -12`, `c = 5`.  
  - `a = 6`, `b = 11`, `c = -10`.  
- **Ожидаемый результат:**  
  - `(0.5, 2.5)` для первых входных данных.  
  - `(-2.5, 0.6667)` для вторых.  
- **Описание процесса:** Проверяется тип, длина и точность вычисления результата.

---

#### Тест 9: `test_d_lower_than_zero`  
- **Цель:** Проверить поведение функции при дискриминанте < 0.  
- **Входные данные:** `a = 20`, `b = -2`, `c = 3`.  
- **Ожидаемый результат:** `()` — пустой кортеж.  
- **Описание процесса:** Проверяется, что результат пуст.

---

#### Тест 10: `test_d_is_zero`  
- **Цель:** Проверить вычисления при дискриминанте = 0.  
- **Входные данные:** `a = 4`, `b = 8`, `c = 4`.  
- **Ожидаемый результат:** `(-1)` — кортеж с одним элементом.  
- **Описание процесса:** Проверяется тип, длина и значение результата.
