while True:
  n = int(input())
  n_list = []
  if n == -1:
    break
  for i in range(1, n):
    if n % i == 0:
      n_list.append(i)
  if n == sum(n_list):
    print(n, " = ", " + ".join(str(i) for i in n_list), sep = '')
  else:
    print(n, "is NOT perfect.")