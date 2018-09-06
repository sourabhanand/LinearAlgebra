#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def create_graph(size, tau):
  print("Creating Graph...")
  rand_array = np.random.rand(size, size)
  rand_array = np.where(rand_array <= tau, 1, 0)
  np.fill_diagonal(rand_array, 0)
  return rand_array

def save_fig(freq_array, fig_name, fig_size):
  fig = plt.figure(figsize=fig_size)
  #fig = plt.figure(figsize=(15,8))
  plt.bar(freq_array[:,0], freq_array[:,1])
  plt.xlabel('MATRIX VALUES')
  plt.ylabel('FREQUENCY')
  plt.title('Histogram Of Matrix Values')
  plt.savefig(fig_name, bbox_inches='tight', dpi=fig.dpi)
  print("Plot "+fig_name+" saved")
  plt.cla()
  #plt.show()

def task_one_and_two(adj_matrix, k, n, matrix_name):
  result = adj_matrix
  result_matrices = {}
  for i in range(2, k+1):
    result = np.matmul(result, adj_matrix)
    result_matrices[i] = result
    fn_prefix = matrix_name+str(i)+"size_"+str(n)
    txtfile = fn_prefix + ".txt"
    pngfile = fn_prefix + ".png"
    np.savetxt(txtfile, result, delimiter=',', fmt='%d')
    unique, counts = np.unique(result, return_counts=True)
    freq_array = np.asarray((unique, counts)).T
    save_fig(freq_array, pngfile, (25,10))
  return result_matrices

def task_three(adj_matrix, k, n, an_matrices):
  result = adj_matrix
  freq_of_ones = {}
  for i in range(2, k+1):
    an_matrix = an_matrices[i]
    an_matrix_mod = np.where(an_matrix != 0, 1, an_matrix)
    result = np.logical_or(result, an_matrix_mod)
    fn_prefix = "X"+str(i)+"size_"+str(n)
    txtfile = fn_prefix + ".txt"
    np.savetxt(txtfile, result, delimiter=',', fmt='%d')
    freq_of_ones[i] = np.count_nonzero(result == 1)

  plt.plot(list(freq_of_ones.keys()), list(freq_of_ones.values()))
  plt.savefig("X"+str(n)+".png", bbox_inches='tight')
  #plt.show()

def main():
  k = 5
  tau = 0.2
  sizes = [50, 100, 200]

  # task 1 and 3
  for matrix_size in sizes:
    adj_matrix = create_graph(matrix_size, tau)
    an_matrices = task_one_and_two(adj_matrix, k, matrix_size, "A")
    task_three(adj_matrix, k, matrix_size, an_matrices)

  # task 2
  k = 3
  for matrix_size in sizes:
    adj_matrix = create_graph(matrix_size, 2*tau)
    bn_matrices = task_one_and_two(adj_matrix, k, matrix_size, "B")

if __name__ == '__main__': main()
