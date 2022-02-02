import random
import time

class ModifiedQuickSort:
    def insertion_sort(self, input_array, left, right):
        for j in range(left+1, right+1):
            key = input_array[j]
            i = j-1
            while i>=0 and input_array[i] > key:
                input_array[i+1] = input_array[i]
                i -= 1
            input_array[i+1] = key

    def swap(self, input_array, left, middle, right):
        if input_array[left] < input_array[middle]:
            if input_array[right] < input_array[left]:
                input_array[left], input_array[right] = input_array[right], input_array[left]
        else:
            if input_array[middle] < input_array[right]:
                input_array[left], input_array[middle] = input_array[middle], input_array[left]
            else:
                input_array[left], input_array[right] = input_array[right], input_array[left]
        if input_array[right] < input_array[middle]:
            input_array[middle], input_array[right] = input_array[right], input_array[middle]
        

    def modified_quick_sort(self, input_array, leftIndex, rightIndex):
        if leftIndex + 10 <= rightIndex:
            middle = (leftIndex + rightIndex)// 2
            self.swap(input_array, leftIndex, middle, rightIndex)
            pivot = input_array[middle]
            input_array[middle], input_array[rightIndex] = input_array[rightIndex], input_array[middle]
            left = leftIndex
            right = rightIndex - 1
            while left <= right:
                while left <= right and input_array[left] <= pivot:
                    left += 1
                while right>=left and input_array[right] >= pivot:
                    right = right - 1
                if left < right:
                    input_array[left], input_array[right] = input_array[right], input_array[left]
            input_array[left], input_array[rightIndex] = input_array[rightIndex], input_array[left]
            self.modified_quick_sort(input_array, leftIndex, left-1)
            self.modified_quick_sort(input_array, left+1, rightIndex)
        else:
            #call insertion sort
            self.insertion_sort(input_array, leftIndex, rightIndex)

    def modified_quick_sort_main(self,input_sizes, input_dictionary, number_of_repetitions):
        #Avg Case
        avg_case = []
        best_case = []
        worst_case = []
        arr = []
        for index, size in enumerate(input_sizes):
            total_execution_time = 0
            #List slicing is used to create a new list is created and does not modify the original arrays
            arr = input_dictionary[size][:]
            for repetition in range(number_of_repetitions):
                random.shuffle(arr)
                avg_start_time = time.time()
                self.modified_quick_sort(arr, 0, len(arr) - 1)
                avg_end_time = time.time()
                total_execution_time += (avg_end_time - avg_start_time)
            avg_time = total_execution_time*1000 / number_of_repetitions
            avg_case.append(avg_time)
            
            #Best Case
            ascending_time_start = time.time()
            self.modified_quick_sort(arr, 0, len(arr) - 1)
            ascending_time_end = time.time()
            best_time = (ascending_time_end - ascending_time_start)*1000
            best_case.append(best_time)

            #Worst Case
            arr.sort(reverse = True)
            descending_time_start = time.time()
            self.modified_quick_sort(arr, 0, len(arr) - 1)
            descending_time_end = time.time()
            worst_time = (descending_time_end - descending_time_start)*1000
            worst_case.append(worst_time)

        print('-------------------------Modfied Quick Sort Execution Times-------------------------')
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