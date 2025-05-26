from mystery import Mystery
import random

mystery = Mystery("diego.perez19@techexchange.in")
sorters = mystery.get_sorters()

# Sorting Groups:
# - Bad Sorts (Stooge, Slow, Bogo): Sorters 4, 6, 12
# - O(n²) Sorts (Bubble, Insertion, Selection): Sorters 2, 5, 11
# - Quick Sort Variants (Median, Random, Last Pivot): Sorters 8, 9, 10
# - Counting Sort: Sorter 7
# - Stable Fast Sorts (Merge, Python Built-in Sort): Sorters 1, 3


# --- Utility function to test sorter ---
def test_sorter(sorter, data, test_name, sorter_id):
    """Runs a sorting test on a given sorter and prints results."""
    print(f"\nSorter {sorter_id + 1} - {test_name}:")
    try:
        time_reported, mem_used = sorter.sort(data)
        print(f"Time reported: {time_reported:.6f}s, Memory: {mem_used} bytes")
        print(f"Sorted correctly? {data == sorted(data)}")
    except Exception as e:
        print(f"Error: {e}")


# --- Tiny List Tests (Identifying Bad Sorts) ---
def test_bad_sorts():
    """Tests bad sorting algorithms on tiny sorted and unsorted lists."""
    print("\n===== Tiny List Tests (Stooge, Slow, Bogo) =====")
    tiny_sorted = [1, 2, 3]
    tiny_unsorted = [3, 1, 2]
    for i in [3, 5, 11]:  # Sorters 4, 6, 12
        for test_name, test_data in [("Sorted", tiny_sorted), ("Unsorted", tiny_unsorted)]:
            test_sorter(sorters[i], test_data[:], test_name, i)


# --- O(n²) Sort Tests (Bubble, Insertion, Selection) ---
def test_n2_sorts():
    """Tests O(n²) sorting algorithms with small and medium lists."""
    print("\n===== O(n²) Sort Tests (Bubble, Insertion, Selection) =====")
    small_sorted = list(range(20))
    small_reversed = list(range(20, 0, -1))
    medium_sorted = list(range(200))
    medium_reversed = list(range(200, 0, -1))
    for i in [1, 4, 10]:  # Sorters 2, 5, 11
        test_sorter(sorters[i], small_sorted[:], "Small Sorted (20)", i)
        test_sorter(sorters[i], small_reversed[:], "Small Reversed (20)", i)
        test_sorter(sorters[i], medium_sorted[:], "Medium Sorted (200)", i)
        test_sorter(sorters[i], medium_reversed[:], "Medium Reversed (200)", i)


# --- Quick Sort Variants (Median, Random, Last Pivot) ---
def test_quick_sort_variants():
    """Tests Quick Sort variants with different pivot strategies."""
    print("\n===== Quick Sort Pivot Behavior Tests =====")
    medium_sorted = list(range(500))
    medium_reversed = list(range(500, 0, -1))
    medium_random = random.sample(range(5000), 500)
    for i in [7, 8, 9]:  # Sorters 8, 9, 10
        test_sorter(sorters[i], medium_sorted[:], "Medium Sorted (500)", i)
        test_sorter(sorters[i], medium_reversed[:], "Medium Reversed (500)", i)
        test_sorter(sorters[i], medium_random[:], "Medium Random (500)", i)


# --- Stability Test (Checking if Sorts Preserve Order) ---
def test_stability():
    """Tests whether sorting algorithms are stable using labeled tuples."""
    print("\n===== Stability Test (Labeled Tuples) =====")
    labeled_tuples = [(2, 'a'), (3, 'a'), (1, 'a'), (3, 'b'), (2, 'b'), (1, 'b')]
    for i, sorter in enumerate(sorters):
        test_copy = labeled_tuples[:]
        try:
            time_reported, mem_used = sorter.sort(test_copy)
            value_sorted = [x[0] for x in test_copy] == sorted([x[0] for x in labeled_tuples])
            stable_sorted = test_copy == sorted(labeled_tuples, key=lambda x: x[0])
            print(f"\nSorter {i + 1}: Sorted? {value_sorted}, Stable? {stable_sorted}, Time: {time_reported:.6f}s, Memory: {mem_used} bytes")
        except Exception as e:
            print(f"\nSorter {i + 1}: Error: {e}")


# --- Counting Sort Test (Only Works on Integers) ---
def test_counting_sort():
    """Tests Counting Sort with a list of random integers."""
    print("\n===== Counting Sort Integer Test (Sorter 7) =====")
    int_list = [random.randint(0, 100) for _ in range(10)]
    sorter = sorters[6]  # Sorter 7 (Counting Sort)
    test_sorter(sorter, int_list[:], "Integer List (10 elements)", 6)



# --- Main Menu ---
def main():
    """Runs user-selected sorting tests."""
    print(
        "\n===== Sorting Algorithm Identification Tests =====\n"
        "1. Tiny List Tests (Bad Sorts: Stooge, Slow, Bogo)\n"
        "2. O(n²) Sort Tests (Bubble, Insertion, Selection)\n"
        "3. Quick Sort Variants (Median, Random, Last Pivot)\n"
        "4. Stability Test (Checking Stable Sorts)\n"
        "5. Counting Sort Test (Only Integer Inputs)\n"
    )

    choice = input("Enter the number of the test to run: ").strip()
    if choice == '1':
        test_bad_sorts()
    elif choice == '2':
        test_n2_sorts()
    elif choice == '3':
        test_quick_sort_variants()
    elif choice == '4':
        test_stability()
    elif choice == '5':
        test_counting_sort()
    else:
        print("Invalid choice. Exiting.")

# Run as script
if __name__ == "__main__":
    main()

