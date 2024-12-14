class QuickFit:
    def __init__(self):
        # Initialize memory blocks
        self.memory = {
            50: {"block1": 50, "block2": 50},
            100: {"block3": 100, "block4": 100},
            200: {"block5": 200}
        }

    def allocate(self, process_size):
        """
        Allocate memory to a process using exact fit or best fit logic.
        :param process_size: Required size of the memory
        :return: Status message
        """
        # Check for exact fit
        if process_size in self.memory:
            for block_name, block_size in self.memory[process_size].items():
                if block_size >= process_size and block_size > 0:
                    self.memory[process_size][block_name] = 0  # Mark block as used
                    return f"Allocated {process_size} KB in {block_name} (Exact Fit)"

        # Best-fit: find a larger block and split it
        for key in sorted(self.memory.keys()):  # Sort memory sizes to find the best fit
            if key >= process_size:
                for block_name, block_size in self.memory[key].items():
                    if block_size >= process_size and block_size > 0:
                        self.memory[key][block_name] -= process_size  # Update remaining size
                        return f"Allocated {process_size} KB in {block_name} (Split: {block_size} -> {self.memory[key][block_name]})"

        return "No Space in Memory"

    def view_memory(self):
        """
        Display the current state of memory.
        """
        print("\nCurrent Memory State:")
        for size, blocks in self.memory.items():
            print(f"  {size} KB Blocks:")
            for block_name, block_size in blocks.items():
                status = "Free" if block_size > 0 else "Used"
                print(f"    {block_name}: {block_size} KB ({status})")


# Interactive Loop
if __name__ == "__main__":
    x = QuickFit()

    is_running = True
    while is_running:
        try:
            print("\nOptions: ")
            print("  1. Allocate Memory")
            print("  2. View Memory State")
            print("  3. Exit")

            choice = int(input("Enter your choice: ").strip())

            if choice == 1:
                size_to_allocate = int(input("Enter the size of memory to allocate: ").strip())
                response = x.allocate(size_to_allocate)
                print(response)
            elif choice == 2:
                x.view_memory()
            elif choice == 3:
                print("Exiting program.")
                is_running = False
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
