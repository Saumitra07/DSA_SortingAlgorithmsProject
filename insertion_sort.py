import random
import time
class InsertionSort:

    def insertion_sort(self, input_array):
        for j in range(1, len(input_array)):
            key = input_array[j]
            i = j-1
            while i>=0 and input_array[i] > key:
                input_array[i+1] = input_array[i]
                i -= 1
            input_array[i+1] = key

    def insertion_sort_main(self,input_sizes, input_dictionary, number_of_repetitions):
        avg_case = []
        best_case = []
        worst_case = []
        arr = []
        for index, size in enumerate(input_sizes):
            total_execution_time = 0
            #List slicing is used to create a new list is created and does not modify the original arrays
            arr = input_dictionary[size][:]
            #Avg Case
            for repetition in range(number_of_repetitions):
                random.shuffle(arr)
                avg_start_time = time.time()
                self.insertion_sort(arr)
                avg_end_time = time.time()
                total_execution_time += (avg_end_time - avg_start_time)
            avg_time = total_execution_time*1000 / number_of_repetitions
            avg_case.append(avg_time)

            #Best Case
            ascending_time_start = time.time()
            self.insertion_sort(arr)
            ascending_time_end = time.time()
            best_time = (ascending_time_end - ascending_time_start)*1000
            best_case.append(best_time)

            #Worst Case
            arr.sort(reverse = True)
            descending_time_start = time.time()
            self.insertion_sort(arr)
            descending_time_end = time.time()
            worst_time = (descending_time_end - descending_time_start)*1000
            worst_case.append(worst_time)

        print('-------------------------Insertion Sort Execution Times-------------------------')
        print('Execution time corresponds to the input sizes: ', input_sizes)
        print("\n")

        print(f'Average Case Execution Time for {number_of_repetitions} repetitions')
        print(avg_case)
        print("\n")

        print('Execution time for already sorted inputs')
        print(best_case)
        print("\n")

        print('Execution time for reversely sorted inputs')
        print(worst_case)
        print("\n")