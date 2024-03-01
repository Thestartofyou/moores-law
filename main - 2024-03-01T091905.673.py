import matplotlib.pyplot as plt

def moores_law(start_year, end_year, transistor_count_start):
    years = range(start_year, end_year + 1)
    transistor_counts = [transistor_count_start]
    for year in years[1:]:
        transistor_counts.append(transistor_counts[-1] * 2)  # doubling every two years

    return years, transistor_counts

def plot_moores_law(years, transistor_counts):
    plt.figure(figsize=(10, 6))
    plt.plot(years, transistor_counts, marker='o', linestyle='-')
    plt.title("Moore's Law: Transistor Count vs. Year")
    plt.xlabel("Year")
    plt.ylabel("Transistor Count (log scale)")
    plt.yscale("log")  # using log scale for better visualization
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    start_year = 1971  # Starting year of Moore's Law
    end_year = 2024    # Ending year for visualization
    transistor_count_start = 2300  # Initial transistor count (e.g., Intel 4004)
    
    years, transistor_counts = moores_law(start_year, end_year, transistor_count_start)
    plot_moores_law(years, transistor_counts)
