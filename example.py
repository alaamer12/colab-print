# -*- coding: utf-8 -*-
"""
Example usage of the colab-print library.

This script demonstrates various features of the colab-print library for displaying
styled text, lists, dictionaries, tables, and pandas DataFrames in environments
that support IPython display (like Jupyter notebooks or Google Colab).
"""

import pandas as pd
import numpy as np  # Added for array examples
from colab_print import (
    Printer, header, title, subtitle, section_divider, subheader,
    code, card, quote, badge, data_highlight, footer,
    highlight, info, success, warning, error, muted, primary, secondary,
    dfd, table, list_, dict_, progress
) 
import time

def demo_printer_class():
    """Demo using the Printer class directly."""
    
    print("=== DEMO: Using Printer Class Directly ===")
    printer = Printer()
    print(f"Available styles: {printer.get_available_styles()}")

    # --- Text Display --- 
    print("\n--- Text Display Examples ---")
    printer.display("This is default text.")
    printer.display("This is highlighted text.", style="highlight")
    printer.display("This is info text.", style="info")
    printer.display("This is success text.", style="success")
    printer.display("This is warning text.", style="warning")
    printer.display("This is error text.", style="error")
    printer.display("This is muted text.", style="muted")
    printer.display("Inline style example.", style="info", font_weight="bold", text_decoration="underline")

    # --- List Display --- 
    print("\n--- List Display Examples ---")
    simple_list = ['Apple', 'Banana', 'Cherry']
    nested_list = ['Fruit', ['Apple', 'Banana'], 'Vegetable', ['Carrot', 'Broccoli']]
    printer.display_list(simple_list, style="success", item_style="padding-left: 15px;")
    printer.display_list(nested_list, ordered=True, style="default")
    printer.display_list(('Tuple', 'Item 1', 'Item 2'), style="warning") # Also works with tuples

    # --- Dictionary Display --- 
    print("\n--- Dictionary Display Examples ---")
    simple_dict = {'Name': 'Bob', 'Role': 'Developer', 'Experience (Years)': 5}
    nested_dict = {
        'Project': 'Colab Print',
        'Version': '0.1.0',
        'Author': {'Name': 'Alaa', 'Contact': 'test@example.com'},
        'Features': ['Text', 'List', 'Dict', 'Table', 'DataFrame']
    }
    printer.display_dict(simple_dict, style="info")
    printer.display_dict(nested_dict, style="default", key_style="color: blue;", value_style="color: green;")

    # --- Table Display --- 
    print("\n--- Table Display Examples ---")
    headers = ["ID", "Product", "Price", "In Stock"]
    rows = [
        [101, "Laptop", 1200.50, True],
        [102, "Keyboard", 75.00, False],
        [103, "Mouse", 25.99, True]
    ]
    printer.display_table(headers, rows, style="default", caption="Inventory")
    printer.display_table(headers, rows, style="highlight", width="80%")

    # --- DataFrame Display --- 
    print("\n--- DataFrame Display Examples ---")
    data = {
        'StudentID': ['S101', 'S102', 'S103', 'S104', 'S105'],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Score': [85.5, 92.0, 78.8, 88.1, 95.2],
        'Major': ['CompSci', 'Physics', 'Math', 'CompSci', 'Physics']
    }
    df = pd.DataFrame(data)

    printer.display_df(df, caption="Student Scores")
    printer.display_df(df, style="info", max_rows=3, precision=1, caption="Limited Rows & Precision")
    printer.display_df(df, style="success", 
                      index=False, 
                      highlight_cols=['Name', 'Score'],
                      highlight_rows={1: "background-color: #DFF0D8;"}, # Bob
                      highlight_cells={(4, 'Score'): "background-color: yellow; font-weight: bold;"}, # Eve's score
                      caption="Styled DataFrame without Index")

    # --- Custom Styles & Themes --- 
    print("\n--- Custom Style & Theme Examples ---")
    
    # Add a single custom style
    printer.add_style("custom_blue", "color: navy; border: 1px solid blue; padding: 5px;")
    printer.display("This uses a custom added style.", style="custom_blue")
    print(f"Updated styles: {printer.get_available_styles()}")

    # Initialize a new Printer with additional themes
    custom_themes = {
        'dark_mode': 'color: #E0E0E0; background-color: #282C34; font-family: Consolas, monospace;',
        'report': 'font-family: "Times New Roman", serif; font-size: 14px; color: #333;'
    }
    themed_printer = Printer(additional_styles=custom_themes)
    themed_printer.display("Dark mode style text.", style="dark_mode")
    themed_printer.display_dict({'report_section': 'Results'}, style="report")


def demo_global_shortcuts():
    """Demo using the global shortcut functions."""
    
    print("\n=== DEMO: Using Global Shortcut Functions ===")
    
    # --- Heading & Structure Display ---
    print("\n--- Heading & Structure Display ---")
    title("Colab Print Demo")
    subtitle("A showcase of styling capabilities")
    header("Main Section Header")
    subheader("Important Subsection")
    section_divider("Section Break")
    
    # --- Content formatting ---
    print("\n--- Content Formatting ---")
    card("This is a card with important content that stands out from the rest of the text")
    quote("The best way to predict the future is to invent it. - Alan Kay")
    code("import pandas as pd\ndf = pd.read_csv('data.csv')\nprint(df.head())")
    
    # --- Status indicators ---
    print("\n--- Status Indicators ---")
    info("This is an informational message")
    success("Operation completed successfully!")
    warning("Please be cautious with this action")
    error("An error occurred during processing")
    muted("This is less important information")
    
    # --- Special elements ---
    print("\n--- Special Elements ---")
    data_highlight("99.8%")
    badge("NEW")
    badge("PRO", background_color="#9C27B0")  # Style override example
    primary("Primary action button")
    secondary("Secondary option")
    highlight("This text needs attention", font_size="20px")  # Style override example
    footer("© 2023 Colab Print Project")
    
    # --- Data Container Display ---
    print("\n--- Data Container Display ---")
    
    # Sample data
    sample_dict = {
        "key1": "value1",
        "key2": "value2",
        "nested": {"a": 1, "b": 2}
    }
    
    sample_list = ["Item 1", "Item 2", ["Nested 1", "Nested 2"]]
    
    headers = ["Name", "Value", "Description"]
    rows = [
        ["Alpha", 100, "First item in list"],
        ["Beta", 200, "Second item in list"],
        ["Gamma", 300, "Third item in list"]
    ]
    
    data = {
        'Category': ['A', 'B', 'C', 'D'],
        'Value1': [10, 20, 30, 40],
        'Value2': [100, 90, 80, 70]
    }
    df = pd.DataFrame(data)
    
    # Display with the shortcuts
    dict_(sample_dict, key_style="color: #1565C0; font-weight: bold;")
    list_(sample_list, ordered=True)
    table(headers, rows, caption="Sample Table Data")
    dfd(df, max_rows=3, caption="Sample DataFrame")
    
    # --- Style Override Examples ---
    print("\n--- Style Override Examples ---")
    header("Default Header")
    header("Custom Color Header", color="#E53935") 
    header("Larger Header", font_size="32px")
    
    info("Default Info Message")
    info("Custom Info", background_color="rgba(3, 169, 244, 0.1)", border_radius="10px")
    
    card("Default Card")
    card("Custom Card", box_shadow="0 4px 8px rgba(0,0,0,0.2)", border_left="5px solid #673AB7")


def demo_progress_bars():
    """Demo using the progress bar feature."""
    
    print("\n--- Progress Bar Examples ---")
    
    # Import P for progress updates
    from colab_print import P
    
    # Determined progress bar example (manual style)
    print("\n--- Determined Progress Bar (Manual) ---")
    progress_id = progress(total=100, desc="Loading Data", color="#4a6fa5", height="25px")
    for i in range(101):
        P.update_progress(progress_id, i)
        time.sleep(0.01)  # Simulate work being done
    
    # TQDM-like functionality (Automatic progress with iterables)
    print("\n--- TQDM-like Progress (Automatic) ---")
    
    # Example 1: With a list - automatically calculates total
    items = list(range(50))
    for item in progress(items, desc="Processing List"):
        time.sleep(0.02)  # Simulate work being done
    
    # Example 2: With a custom total
    items = range(100)
    for item in progress(items, total=100, desc="Processing Range", color="#2ecc71"):
        if item % 3 == 0:  # Only process every third item
            time.sleep(0.02)
    
    # Example 3: With a generator that doesn't have len() - undetermined progress
    def my_generator():
        for i in range(30):
            yield i
    
    for item in progress(my_generator(), desc="Processing Generator", color="#e74c3c"):
        time.sleep(0.05)
        
    # Traditional undetermined progress example
    print("\n--- Undetermined Progress Bar ---")
    progress_id2 = progress(desc="Processing Data", style="progress", color="#8E44AD", height="20px", animated=True)
    
    # Simulate some processing work
    time.sleep(2)
    
    # Important: Replace the undetermined progress with a completed one
    # This prevents the animation from running forever
    P.update_progress(progress_id2, 100, 100)
    
    # Alternative ways to show completion
    print("\n--- Completing Progress Examples ---")
    
    # Style 1: Show partial completion
    progress_id3 = progress(total=100, desc="Downloading Files", color="#16a085", height="20px")
    for i in range(0, 65, 5):
        P.update_progress(progress_id3, i)
        time.sleep(0.05)
    success("Download partially completed (65%)")
    
    # Style 2: Show error state
    progress_id4 = progress(total=100, desc="Installing Packages", color="#c0392b", height="20px")
    for i in range(0, 85, 5):
        P.update_progress(progress_id4, i)
        time.sleep(0.05)
    error("Installation failed at 85%")


def demo_enhanced_lists():
    """Demo showcasing the enhanced list display features."""
    
    title("Enhanced List Display Features")
    subtitle("Showcasing new styling and formatting capabilities")
    
    # Create a Printer instance for custom configurations
    printer = Printer()
    
    # --- Simple color-coded nested lists ---
    header("Color-coded Nested Lists")
    
    nested_list = [
        "Top Level",
        ["Level 1 - Item 1", "Level 1 - Item 2"],
        "Another Top Level",
        ["Level 1 - Item 3", 
            ["Level 2 - Nested A", "Level 2 - Nested B", 
                ["Level 3 - Deep Nested", "Level 3 - Another Deep"]
            ]
        ],
        "Final Top Level"
    ]
    
    info("Default color-coded nesting scheme:")
    list_(nested_list)
    
    # --- Custom nesting colors ---
    subheader("Custom Nesting Colors")
    
    # Use warm color scheme (reds to yellows)
    warm_colors = [
        "#E53935",  # Red
        "#F57C00",  # Orange
        "#FDD835",  # Yellow
        "#7CB342",  # Light Green
        "#039BE5",  # Light Blue
    ]
    
    info("Warm color scheme for nesting:")
    list_(nested_list, nesting_colors=warm_colors)
    
    # --- Matrix display ---
    header("Matrix Display")
    
    # Simple matrix (2D array)
    matrix_data = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    
    info("Simple 2D matrix (automatically detected):")
    list_(matrix_data)
    
    # Create a NumPy matrix
    np_matrix = np.array([
        [1.2, 3.4, 5.6],
        [7.8, 9.0, 1.2],
        [3.4, 5.6, 7.8],
        [9.0, 1.2, 3.4]
    ])
    
    info("NumPy matrix with auto-detection:")
    list_(np_matrix)
    
    # Force list display for 2D data
    info("Forcing list display for matrix data:")
    list_(matrix_data, matrix_mode=False)
    
    # --- Array-like objects ---
    header("Array-like Objects Support")
    
    # NumPy array (1D)
    np_array = np.array([10, 20, 30, 40, 50])
    info("NumPy 1D array:")
    list_(np_array)
    
    # Pandas Series
    pd_series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
    info("Pandas Series:")
    list_(pd_series)
    
    # Creating a pandas DataFrame
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    info("Pandas DataFrame (displayed as matrix):")
    list_(df)
    
    # --- Complex nested structures ---
    header("Complex Nested Structures")
    
    # Combined nested structure with different types
    complex_structure = [
        "Mixed Types Example",
        {"dict_in_list": "value", "nested_dict": {"a": 1, "b": 2}},
        ["List in list", ["Deeper", np.array([1, 2, 3])]], 
        pd.Series([10, 20, 30], index=['x', 'y', 'z']),
        [
            [1, 2, 3],
            [4, 5, 6]
        ]
    ]
    
    info("Complex nested structure with different data types:")
    list_(complex_structure)
    
    # --- Generator and iterator examples ---
    header("Generators and Iterators")
    
    # Generator example
    def sample_generator(n):
        for i in range(n):
            yield f"Generated item {i}"
    
    info("Generator output:")
    list_(sample_generator(5))
    
    # Iterator example (map object)
    map_iterator = map(lambda x: x * 10, range(5))
    info("Map iterator output:")
    list_(map_iterator)


def main():
    """Main function to run the examples."""
    
    print("===== COLAB PRINT LIBRARY DEMO =====")
    
    # Uncomment to run the original Printer class demo
    # demo_printer_class()
    
    # Demo the new global shortcut functions
    demo_global_shortcuts()
    
    # Demo the enhanced list display features
    demo_enhanced_lists()
    
    # Demo the progress bar feature
    demo_progress_bars()
    
    print("\n===== END OF DEMO =====")


if __name__ == "__main__":
    main() 