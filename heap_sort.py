import random
import time
class HeapSort:
    def insert_element(self, nums):
        insert_nums = []
        for index, num in enumerate(nums):
            #Insert into array
            insert_nums.append(num)
            while index > 0 and insert_nums[index//2] > insert_nums[index]:
                insert_nums[index//2], insert_nums[index] = insert_nums[index], insert_nums[index//2]
                index = index // 2
        return insert_nums

    def remove_element(self, heapify_nums):
        sorted_array = []
        size = len(heapify_nums)
        for index in range(0, size):
            flag=0
            temp = heapify_nums[0]
            heapify_nums[0] = heapify_nums[len(heapify_nums)-1]
            heapify_nums.pop(len(heapify_nums)-1)
            n = len(heapify_nums)
            i = 0
            while i < n:
                if 2*i+2 <= n-1:
                    if heapify_nums[i] <= heapify_nums[2*i+1] and heapify_nums[i] <= heapify_nums[2*i+2]:
                        sorted_array.append(temp)
                        flag =1
                        break
                    else:
                        j=-1
                        if heapify_nums[2*i+1] > heapify_nums[2*i+2]:
                            j = 2*i+2
                        else:
                            j = 2*i+1
                        heapify_nums[i], heapify_nums[j] = heapify_nums[j], heapify_nums[i]
                        i = j
                else:
                    if 2*i+1 <= n-1:
                        if heapify_nums[i] > heapify_nums[2*i+1]:
                            heapify_nums[i], heapify_nums[2*i+1] = heapify_nums[2*i+1], heapify_nums[i]
                    sorted_array.append(temp)
                    flag=1
                    break

            if flag == 0:       
                sorted_array.append(temp)
        return sorted_array

    def heap_sort(self, nums):
        heapify_array = self.insert_element(nums)
        sorted_array = self.remove_element(heapify_array)
        return sorted_array
    
    def heap_sort_main(self,input_sizes, input_dictionary, number_of_repetitions):
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
                arr = self.heap_sort(arr)
                avg_end_time = time.time()
                total_execution_time += (avg_end_time - avg_start_time)
            avg_time = total_execution_time*1000 / number_of_repetitions
            avg_case.append(avg_time)

            #Best Case
            ascending_time_start = time.time()
            arr = self.heap_sort(arr)
            ascending_time_end = time.time()
            best_time = (ascending_time_end - ascending_time_start)*1000
            best_case.append(best_time)

            #Worst Case
            arr.sort(reverse = True)
            descending_time_start = time.time()
            arr = self.heap_sort(arr)
            descending_time_end = time.time()
            worst_time = (descending_time_end - descending_time_start)*1000
            worst_case.append(worst_time)

        print('-------------------------Heap Sort Execution Times-------------------------')
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