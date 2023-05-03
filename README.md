# python_101
Python Problems

This repository contains problems solved by using standard Python.

---
## IF-ELSE tasks
<details>
<summary>
<b>Driver's License Eligibility (<a href="task_1.py">if-else/task_1.py</a>)</b>
</summary>

#### Problem
Write a Python program that asks the user to input their age. If the age is equal to or greater than 18, the program should display the message "You can get a driver's license!". If the age is less than 8, the program should display the message "You cannot get a driver's license yet. Come back when you turn 18."


#### Input format
На вход поступает любое целое число, обозначающее возраст кандидата в водители.

#### Output format
Программа решает, может ли кандидат водить машину.

#### Example 
<table><tbody>
  <tr>
    <td><b>Input</b></td>
    <td><b>Output</b></td>
  </tr>
  <tr>
    <td valign='top'>
5<br>
</td>
    <td valign='top'>
вернитесь через 13 лет<br>
</td>
  </tr>
  <tr>
    <td valign='top'>
18<br>
</td>
    <td valign='top'>
вы можете водить машину<br>
</td>
  </tr>
  <tr>
    <td valign='top'>
105<br>
</td>
    <td valign='top'>
вы не можете водить машину<br>
</td>
  </tr>
</tbody></table>
</details>



<details>
<summary>
<b>Number to English Word (<a href="task_2.py">if-else/task_2.py</a>)</b>
</summary>

#### Problem
Write a program that takes an input number from 1 to 10 and displays its English word representation. If the number is not within this range, the program should display an error message.

#### Input format
На вход поступает любое целое число в диапазоне от 1 до 10.

#### Output format
Название числа на английском языке.

#### Example 
<table><tbody>
  <tr>
    <td><b>Input</b></td>
    <td><b>Output</b></td>
  </tr>
  <tr>
    <td valign='top'>
5<br>
</td>
    <td valign='top'>
five<br>
</td>
  </tr>
  <tr>
    <td valign='top'>
8<br>
</td>
    <td valign='top'>
eight<br>
</td>
  </tr>
  <tr>
    <td valign='top'>
105<br>
</td>
    <td valign='top'>
Ошибка, введите число от 1 до 10<br>
</td>
  </tr>
</tbody></table>
</details>



<details>
<summary>
<b>Largest of Three Numbers (<a href="task_3.py">if-else/task_3.py</a>)</b>
</summary>

#### Problem
Write a program that asks the user to input three different numbers and displays the largest of them. The user is guaranteed to enter three distinct numbers.


#### Input format
Три целых числа

#### Output format
Максимальное из трех введенных чисел

#### Example
<table><tbody>
  <tr>
    <td><b>Input</b></td>
    <td><b>Output</b></td>
  </tr>
  <tr>
    <td valign='top'>
5<br>
0<br>
751<br>

</td>
  <td valign='top'>
751<br>
</td>
  </tr>
</tbody></table>
</details>



<details>
<summary>
<b>Movie Ticket Discount Calculator (<a href="task_4.py">if-else/task_4.py</a>)</b>
</summary>

#### Problem
In a certain city, a movie theater offers various discounts for schoolchildren, students, and seniors. Write a program that determines the discount on a ticket for a visitor based on their age. The discounts at the movie theater are as follows:

1. Schoolchildren (from 7 to 17 years old, inclusive) get a 40% discount.
2. Students (from 18 to 24 years old, inclusive) get a 25% discount.
3. Seniors (65 years old and older) get a 50% discount.


#### Input format
На вход поступает целое число, обозначающее возраст посетителя.

#### Output format
Программа выводит размер скидки в процентах.

#### Example
<table><tbody>
  <tr>
    <td><b>Input</b></td>
    <td><b>Output</b></td>
  </tr>
  <tr>
    <td valign='top'>
14<br>
</td>
    <td valign='top'>
40%<br>
</td>
  </tr>
  <tr>
    <td valign='top'>
20<br>
</td>
    <td valign='top'>
25%<br>
</td>
  </tr>
  <tr>
    <td valign='top'>
70<br>
</td>
    <td valign='top'>
50%<br>
</td>
  </tr>
</tbody></table>
</details>