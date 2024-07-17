from pre_processor import PreProcessor
from visualizer import Visualizer
from nlp_processor import NLP_Processor
import pandas as pd

preprocessor = PreProcessor()
df, uni_counts, description, info, data_types  = preprocessor.pre_process('data.csv')

visualizer = Visualizer()
# Creating all visualizations and saving in the visualizations directory/folder

visualizer.plot_university_distribution(uni_counts)
visualizer.plots_final_data()

#Creating CSV after NLP preprocessing
questions_data = df.iloc[:,0:26]
nlp = NLP_Processor()

preprocessed = nlp.preprocessor(questions_data)
df_pre_processed = pd.DataFrame(preprocessed)
df_pre_processed.to_csv('preprocessed_data.csv')



