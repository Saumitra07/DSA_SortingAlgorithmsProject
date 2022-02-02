import random
from insertion_sort import InsertionSort
from inplace_quicksort import InplaceQuickSort
from modified_quicksort import ModifiedQuickSort
from merge_sort import MergeSort
from heap_sort import HeapSort


class Sorting:
    def generate_random_numbers(self, input_sizes, input_dict):
        for size in input_sizes:
            arr = random.sample(range(0, size), size)
            input_dict[size] = arr


if __name__ == "__main__":

    number_of_repetitions = 3
    input_sizes = [10, 1000, 2000, 3000, 5000, 10000, 20000, 30000, 40000, 50000, 60000]
    input_dict = {}

    all_sorting_object = Sorting()
    random.seed(100)
    all_sorting_object.generate_random_numbers(input_sizes, input_dict)

    menu = {1: 'Insertion Sort', 2: 'Merge Sort', 3: 'Heap Sort',4: 'In-place quicksort', 5: 'Modified Quicksort', 6:'Run all algorithms', 7: 'Exit'}

    while True:
        print('--------------------------------------------------')
        for key, value in menu.items():
            print(key,'-',value)
        
        select_option = ''
        try:
            select_option = int(input('Please select the sorting algorithm to run: '))
        except:
            print('Please input a number')
        
        if select_option == 1:
            ins_sort = InsertionSort()
            ins_sort.insertion_sort_main(input_sizes, input_dict, number_of_repetitions)

        elif select_option == 2:
            merge_sort = MergeSort()
            merge_sort.merge_sort_main(input_sizes, input_dict, number_of_repetitions)

        elif select_option == 3:
            heap_sort = HeapSort()
            heap_sort.heap_sort_main(input_sizes, input_dict, number_of_repetitions)
        
        elif select_option == 4:
            inplace_qs = InplaceQuickSort()
            inplace_qs.inplace_quicksort_main(input_sizes, input_dict, number_of_repetitions)

        elif select_option == 5:
            modified_qs = ModifiedQuickSort()
            modified_qs.modified_quick_sort_main(input_sizes, input_dict, number_of_repetitions)
        
        elif select_option == 6:
            ins_sort = InsertionSort()
            ins_sort.insertion_sort_main(input_sizes, input_dict, number_of_repetitions)

            merge_sort = MergeSort()
            merge_sort.merge_sort_main(input_sizes, input_dict, number_of_repetitions)

            heap_sort = HeapSort()
            heap_sort.heap_sort_main(input_sizes, input_dict, number_of_repetitions)

            inplace_qs = InplaceQuickSort()
            inplace_qs.inplace_quicksort_main(input_sizes, input_dict, number_of_repetitions)

            modified_qs = ModifiedQuickSort()
            modified_qs.modified_quick_sort_main(input_sizes, input_dict, number_of_repetitions)

        elif select_option == 7:
            break
        else:
            print('Please enter input from the menu options')
