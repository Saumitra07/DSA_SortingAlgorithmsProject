import random
import time

class InplaceQuickSort:
    
    def partition(self, input_array, leftIndex, rightIndex):
        random_index = random.randint(leftIndex, rightIndex-1)
        input_array[random_index], input_array[rightIndex] = input_array[rightIndex], input_array[random_index]
        pivot = input_array[rightIndex]
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
        return left

    def inplace_quicksort(self, input_array, left, right):
        if left >= right:
            return
        l = self.partition(input_array, left, right)   
        self.inplace_quicksort(input_array, left, l-1)
        self.inplace_quicksort(input_array, l+1, right)

    def inplace_quicksort_main(self,input_sizes, input_dictionary, number_of_repetitions):
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
                self.inplace_quicksort(arr, 0, len(arr)-1)
                avg_end_time = time.time()
                total_execution_time += (avg_end_time - avg_start_time)
            avg_time = total_execution_time*1000 / number_of_repetitions
            avg_case.append(avg_time)

            #Best Case
            ascending_time_start = time.time()
            self.inplace_quicksort(arr, 0, len(arr)-1)
            ascending_time_end = time.time()
            best_time = (ascending_time_end - ascending_time_start)*1000
            best_case.append(best_time)

            #Worst Case
            arr.sort(reverse = True)
            descending_time_start = time.time()
            self.inplace_quicksort(arr, 0, len(arr)-1)
            descending_time_end = time.time()
            worst_time = (descending_time_end - descending_time_start)*1000
            worst_case.append(worst_time)

        print('-------------------------Inplace Quick Sort Execution Times-------------------------')
        print('Execution time corresponds to the input sizes: ', input_sizes)
        print("\n")

        print(f'Average Case Exceution Time for {number_of_repetitions} repetitions')
        print(avg_case)
        print("\n")

        print('Execution time for already sorted inputs')
        print(best_case)
        print("\n")

        print('Execution time for reversely sorted inputs')
        print(worst_case)
        print("\n")