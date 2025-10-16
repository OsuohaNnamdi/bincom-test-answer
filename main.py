from color_analyzer import BincomColorAnalyzer
from database_manager import DatabaseManager
from algorithms import RecursiveSearch, BinaryConverter, FibonacciCalculator, PatternAnalyzer

def main():
    print("=== Bincom Color Analysis ===")
    
    # Initialize analyzer
    analyzer = BincomColorAnalyzer()
    
    # Print basic info
    print(f"Total colors recorded: {len(analyzer.all_colors)}")
    print(f"Unique colors: {len(analyzer.color_frequencies)}")
    print(f"Color frequencies: {dict(analyzer.color_frequencies)}")
    
    # Answer questions 1-5
    print("1. Mean color:", analyzer.get_mean_color())
    print("2. Most worn color:", analyzer.get_most_worn_color())
    print("3. Median color:", analyzer.get_median_color())
    print("4. Variance of colors:", analyzer.get_color_variance())
    print("5. Probability of red:", f"{analyzer.get_red_probability():.4f}")
    
    # Database section
    print("\n==================================================")
    print("DATABASE OPERATIONS")
    print("==================================================")
    
    db_manager = DatabaseManager()
    if db_manager.test_connection():
        save_data = input("\nDo you want to save the color data to PostgreSQL? (y/n): ").lower().strip()
        if save_data == 'y':
            db_manager.save_color_frequencies(analyzer.color_frequencies)
    else:
        print("\nWARNING: Cannot connect to database.")
    
    # Other algorithms
    print("\n==================================================")
    print("ADDITIONAL ALGORITHMS")
    print("==================================================")
    
    # Recursive search demo
    print("\n7. Recursive Search Demo:")
    numbers_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    search_target = 23
    result_index = RecursiveSearch.recursive_search(numbers_list, search_target)
    print(f"Searching for {search_target} in {numbers_list}: Found at index {result_index}")
    
    # Binary converter demo
    print("\n8. Binary Converter Demo:")
    binary, decimal = BinaryConverter.generate_and_convert()
    print(f"Generated binary: {binary} -> Decimal: {decimal}")
    
    # Fibonacci sum
    print("\n9. Fibonacci Sum:")
    fib_sum = FibonacciCalculator.sum_first_50_fibonacci()
    print(f"Sum of first 50 Fibonacci numbers: {fib_sum}")
    
    # Pattern analysis
    print("\nPattern Analysis from HTML:")
    input_seq = "0101101011101011011101101000111"
    output_seq = PatternAnalyzer.analyze_sequence(input_seq)
    print(f"Input:  {input_seq}")
    print(f"Output: {output_seq}")

if __name__ == "__main__":
    main()