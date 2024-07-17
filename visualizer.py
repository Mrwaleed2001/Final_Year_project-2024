import matplotlib.pyplot as plt
import os
import seaborn as sns
import pandas as pd

class Visualizer():
    
    @staticmethod
    def plot_university_distribution(university_counts):
        # Existing folder
        existing_folder = "visualizations"

        # Directory to save images
        directory = os.path.join(existing_folder, "University Distributions")

        # Create the directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)

        plt.figure(figsize=(10, 8))
        plt.pie(university_counts, labels=university_counts.index, autopct='%1.1f%%', startangle=140,
                textprops={'fontsize': 5})  # Adjust the font size for labels here
        plt.title('Distribution of Universities', fontsize=14)
        plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
        plt.savefig(os.path.join(directory, "Piechart.png"))
        plt.close()

        # Create a bar plot using seaborn
        plt.figure(figsize=(12, 8))
        sns.barplot(x=university_counts.index, y=university_counts, palette="viridis")

        # Add labels and title
        plt.xlabel('University')
        plt.ylabel('Count')
        plt.title('Distribution of Universities')

        # Rotate x-axis labels for better readability (optional)
        plt.xticks(rotation=45, ha="right")
        plt.savefig(os.path.join(directory, "Barplot.png"))
        plt.close()
    
    @staticmethod
    def plots_final_data():
        final_df_2 = pd.read_csv('final_data.csv')
        # Existing folder
        existing_folder = "visualizations"

        # Directory to save images
        directory = os.path.join(existing_folder, "Final Plots")

        # Create the directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)

        plt.figure(figsize=(12, 8))
        # Spread of each class over number of records and how dense the results are
        sns.violinplot(data=final_df_2, y="target",
        x=final_df_2.index)
        plt.xlabel('Records by INDEX')
        plt.ylabel('Target Personality Classes')
        plt.title('Spread and Deviation of each class over the records')
        plt.savefig(os.path.join(directory, "Spread and Deviation of each class.png"))
        plt.close()

        plt.figure(figsize=(12, 8))
        sns.countplot(data=final_df_2, y="university", hue="Result E/I")
        plt.xlabel('Count')
        plt.ylabel('Universities')
        plt.title('EI class count over universities')
        plt.savefig(os.path.join(directory, "EI class count over universities.png"))
        plt.close()

        plt.figure(figsize=(12, 8))
        sns.countplot(data=final_df_2, y="university", hue="Result S/N")
        plt.xlabel('Count')
        plt.ylabel('Universities')
        plt.title('SN class count over universities')
        plt.savefig(os.path.join(directory, "SN class count over universities.png"))
        plt.close()

        plt.figure(figsize=(12, 8))
        sns.countplot(data=final_df_2, y="university", hue="Result T/F")
        plt.xlabel('Count')
        plt.ylabel('Universities')
        plt.title('TF class count over universities')
        plt.savefig(os.path.join(directory, "TF class count over universities.png"))
        plt.close()

        plt.figure(figsize=(12, 8))
        sns.countplot(data=final_df_2, y="university", hue="Result J/P")
        plt.xlabel('Count')
        plt.ylabel('Universities')
        plt.title('JP class count over universities')
        plt.savefig(os.path.join(directory, "JP class count over universities.png"))
        plt.close()

        plt.figure(figsize=(12, 8))
        sns.barplot(data=final_df_2, x=final_df_2.index, y="target")
        plt.xlabel('Personality Target Classes')
        plt.ylabel('Count')
        plt.title('Target class distribution')
        plt.savefig(os.path.join(directory, "Target class distribution.png"))
        plt.close()

        

        
        
