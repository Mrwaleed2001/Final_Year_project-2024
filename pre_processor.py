import pandas as pd
import numpy as np

class PreProcessor():

    @staticmethod
    def pre_process(file):
        newcolumnnames= ['email', 'name', 'uni', 'degree_year','JP1', 'SN1', 
                    'EI1', 'TF1', 'SN2', 'EI2', 'JP2', 'JP3', 'EI3', 'SN3', 'JP4', 'SN4', 
                    'EI4', 'TF2', 'SN5', 'EI5', 'JP5', 'JP6', 'JP7', 'SN6', 'EI6', 'TF3', 'SN7', 
                    'EI7', 'JP8', 'EI8']

        #Loading raw-data
        data = pd.read_csv(file)

        #Focusing on 26 questions only
        data2 = data.iloc[:, 1:31]

        #Getting column names
        old_cols = data2.columns

        #Getting data description and info of the 26 questions dataframe
        data_description = data2.describe()
        info = data2.info()

        #getting original data types of columns
        orig_dtypes = data2.dtypes

        #new column names
        data2.columns = newcolumnnames
        new_cols = data2.columns

        #dropping name column as no relevance
        data2.drop('name', axis = 1)

        #Checking count of universities
        uni_counts = data2['uni'].value_counts()

        #In the count above we can notice that same university has provided different names for the university. That creates inconsistency and redundancy

        ned = 'NEDUET|NED|ned|NED university'
        uok = 'UoK|University of Karachi|Karachi University|KU'
        bahria = 'Bahria|Bahria University'
        kiu = 'Karakuroam international university gilgit baltistan|KIU|Karakorum international university gilgit|Kiu'
        dow = 'DOW'
        iobm = 'IoBM'
        szabist = 'Szabist|SZABIST'
        uit = 'usman institute of technology|UIT|UIT UNIVERSITY|UIT University'
        fast = 'FAST'
        zu = 'ziauddin|Ziauddin|Ziauddin University'
        juw = 'JUW|Jinnah University for Women'
        kmdc = 'KMDC|Kmdc'
        iu = 'Iqra University|Iqra University|Iqra Univeristy'
        nust = 'NUST'
        kku = 'Kadir khas university'
        iuhs = 'Indus university of health and sciences'
        aiou = 'Allama Iqbal Open University'
        ssuet = 'Sir syed university of engineering and technology'
        jsmu = 'JSMU'
        hu = 'Habib University'
        tsa = 'Tabanis School of Accountancy|Tabani|TSA|Tabanis School of Accountancy'
        vu = 'VU'
        dcwg = 'degree college for women gilgit'
        aidm = 'Aidm'
        ru = 'Ryerson University'
        uob = 'University of Bolton'
        cmc = 'Cmc'
        ivs = 'Indus Valley School'
        lcmd = 'LCMD'
        iba = 'IBA'

        uni2 = ['NEDUET', 'UoK', 'Bahria', 'KIU', 'DOW', 'IoBM', 'SZABIST', 'UIT', 'FAST', 'Ziauddin University', 'JUW', 'KMDC',
                'IU', 'NUST', 'KKU', 'IUHS', 'Allama Iqbal Open University', 'SSUET', 'JSMU', 'HU', 'Tabanis', 'VU', 
                'Degree College for Women Gilgit', 'AIDM', 'Ryerson University', 'University of Bolton', 'CMC', 'IVS', 'LCMD', 'IBA']

        conditions = [
            (data2['uni'].str.contains(ned)),
            (data2['uni'].str.contains(uok)),
            (data2['uni'].str.contains(bahria)),
            (data2['uni'].str.contains(kiu)),
            (data2['uni'].str.contains(dow)),
            (data2['uni'].str.contains(iobm)),
            (data2['uni'].str.contains(szabist)),
            (data2['uni'].str.contains(uit)),
            (data2['uni'].str.contains(fast)),
            (data2['uni'].str.contains(zu)),
            (data2['uni'].str.contains(juw)),
            (data2['uni'].str.contains(kmdc)),
            (data2['uni'].str.contains(iu)),
            (data2['uni'].str.contains(nust)),
            (data2['uni'].str.contains(kku)),
            (data2['uni'].str.contains(iuhs)),
            (data2['uni'].str.contains(aiou)),
            (data2['uni'].str.contains(ssuet)),
            (data2['uni'].str.contains(jsmu)),
            (data2['uni'].str.contains(hu)),
            (data2['uni'].str.contains(tsa)),
            (data2['uni'].str.contains(vu)),
            (data2['uni'].str.contains(dcwg)),
            (data2['uni'].str.contains(aidm)),
            (data2['uni'].str.contains(ru)),
            (data2['uni'].str.contains(uob)),
            (data2['uni'].str.contains(cmc)),
            (data2['uni'].str.contains(ivs)),
            (data2['uni'].str.contains(lcmd)),
            (data2['uni'].str.contains(iba))
        ] 

        data2["university"] = np.select(conditions, uni2, default="Other")

        # Sort the columns based on initials
        sorted_columns = sorted(new_cols, key=lambda x: (x[:2], x))

        # Reorder the DataFrame based on the sorted columns
        data3 = data2[sorted_columns]

        # print("University Counts")
        # print(uni_counts)

        # print()
        # print("Data description")
        # print(data_description)

        # print()
        # print("Original data types")
        # print(orig_dtypes)

        # return data3
        return (data3, uni_counts, data_description, info, orig_dtypes)




