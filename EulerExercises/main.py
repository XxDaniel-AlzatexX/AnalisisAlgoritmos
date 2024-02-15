def problem_1(num):
  #If we list all the natural numbers below that are multiples of 3 or 5, we get 3, 5, 6 and 9.
  #The sum of these multiples is 10. Find the sum of all the multiples of 3 or 5 below 1000.
  sum = 0
  for i in range(num):
    if i % 3 == 0 or i % 5 == 0:
      sum += i
  return sum


def problem_2(num):
  #Each new term in the Fibonacci sequence is generated by adding the previous two terms.
  #By starting with 1 and 2, the first terms will be:
  #1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
  #By considering the terms in the Fibonacci sequence whose values do not exceed four million,
  #find the sum of the even-valued terms.
  sum = 2
  for i in range(num):
    for j in range(sum, num):
      sum += i
      if i + j % 2 == 0:
        sum += i + j
      break
  return sum


def problem_3(num):
  #The prime factors of 13195 are 5, 7, 13 and 29.
  #What is the largest prime factor of the number 13195?
  i = 2
  while i * i <= num:
    if num % i:
      i += 1
    else:
      num //= i
  return num


def problem_4():
  #A palindromic number reads the same both ways.
  #The largest palindrome made from the product of 2 2-digit numbers is:
  #9009 = 91 × 99.
  #Find the largest palindrome made from the product of 2 3-digit numbers.
  def is_palindrome(num):
    return str(num) == str(num)[::-1]

  max = 0
  for i in range(100, 1000):
    for j in range(i, 1000):
      prod = i * j
      if is_palindrome(prod) and prod > max:
        max = prod
  return max


def problem_5(num):
  #2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
  number = 1
  while True:
    if all(number % i == 0 for i in range(1, num)):
      return number
    number += 1


def main():
  print("Problem 1")
  print(problem_1(10))

  print("Problem 2")
  print(problem_2(10))

  print("Problem 3")
  print(problem_3(13195))

  print("Problem 4")
  print(problem_4())

  print("Problem 5")
  print(problem_5(10))


if __name__ == "__main__":
  main()
