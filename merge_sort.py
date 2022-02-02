import random
import time
class MergeSort:
    def merge(self, input_array, left, mid, right):
        temp = [0]*(right - left + 1)
        i, j, k = left, mid+1, 0
        while i <= mid and j <= right:
            if input_array[i] <= input_array[j]:
                temp[k] = input_array[i]
                i += 1
                k += 1
            else:
                temp[k] = input_array[j]
                j += 1
                k += 1
        
        while i <= mid:
            temp[k] = input_array[i]
            i += 1
            k += 1
        
        while j <= right:
            temp[k] = input_array[j]
            j += 1
            k += 1

        for i in range(left, right+1):
            input_array[i] = temp[i - left]
            
    def merge_sort(self, inpuy_array, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(inpuy_array, left, mid)
            self.merge_sort(inpuy_array, mid+1, right)
            self.merge(inpuy_array, left, mid, right)

    def merge_sort_main(self,input_sizes, input_dictionary, number_of_repetitions):
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
                self.merge_sort(arr,0,len(arr)-1)
                avg_end_time = time.time()
                total_execution_time += (avg_end_time - avg_start_time)
            avg_time = total_execution_time*1000 / number_of_repetitions
            avg_case.append(avg_time)

            #Best Case
            ascending_time_start = time.time()
            self.merge_sort(arr,0,len(arr)-1)
            ascending_time_end = time.time()
            best_time = (ascending_time_end - ascending_time_start)*1000
            best_case.append(best_time)

            #Worst Case
            arr.sort(reverse = True)
            descending_time_start = time.time()
            self.merge_sort(arr,0,len(arr)-1)
            descending_time_end = time.time()
            worst_time = (descending_time_end - descending_time_start)*1000
            worst_case.append(worst_time)

        print('-------------------------Merge Sort Execution Times-------------------------')
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


