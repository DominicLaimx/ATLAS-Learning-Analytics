'''To run code, 
1) on microsoft teams, navigate to excel sheet file
2) Press the arrow down and click "Sync"
3) Login to onedrive
4) Navigate and find path to xlsx file
5) update URL on line 14 , May need to change backslashes to double backslashes
Dependencies:
1) pip install pandas
2) pip install openpyxl
'''


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
url = "D:\\Nanyang Technological University\\NTU Imperial Student-Led Project on Learning Analytics - General\\NTU Student Analytics Survey.xlsx"
df = pd.read_excel(url)
columnlist = list(df.columns)
# for i in columnlist:
#     print(i)
#     print("\n")
df = df[["ID","Year of Study", "School", "I have read and understood the instructions.", \
        "1.\xa0\xa0\xa0\xa0\xa0I keep track of my own learning data (e.g. tracking hours spent on a module per week, strengths and weakness in terms of course topics).2",\
        "2.\xa0\xa0\xa0\xa0 It is important to keep track and analyse my own learning data.2",\
        "3.\xa0\xa0\xa0\xa0 I will adjust my study habits or learning strategies based on insights from learning analytics.2",\
        "Would you like to elaborate on your ratings?2", \
        "1.\xa0\xa0\xa0\xa0 I know that the university has put in place a student data governance policy in line with PDPC.2",\
        "2.\xa0 \xa0 \xa0The university should ask for my explicit consent for learning analytics projects if it involves any identifiable data about me (e.g., name, ethnicity, age, and gender).2",\
        "3.\xa0\xa0\xa0\xa0 I am comfortable with the idea of NTU collecting data on my learning behaviours and performances to improve teaching and learning.2",\
        "4.\xa0\xa0\xa0\xa0 It is important to me that I can opt out of the collection of my learning data for my professors and tutors. 2",\
        "5.\xa0\xa0\xa0\xa0 It is important to me that I can opt out of the collection of my learning data to be used by myself.2",\
        "Would you like to raise any further privacy concerns that NTU should address with learning analytics?2",\
        "Do you have any further suggestions or comments on how you would like to be supported by learning analytics?",\
        "1.\xa0\xa0\xa0\xa0 The university should regularly update me about my learning progress based on the analysis of my educational data.3",\
        "2.\xa0 \xa0The learning analytics service should show how my learning progress compares to the course learning outcomes.3",\
        "3.\xa0\xa0\xa0\xa0 I expect the teaching staff to act (i.e. support me) if the analytics show that I am at-risk of failing, underperforming or needs improvement in my learning.3",\
        "4.\xa0\xa0\xa0\xa0 I feel that the following project could potentially benefit students in NTU. a. Early AleRT for Learning Intervention (EARLI): A predictive AI project to detect and support at-risk students...",\
        "4.\xa0\xa0\xa0\xa0 I feel that the following project could potentially benefit students in NTU. b. Course Analytics Dashboard for Students (CADS): A personalised learning analytics project that provides facul...",\
        "4.\xa0\xa0\xa0\xa0 I feel that the following project could potentially benefit students in NTU.\xa0c. NTU AI Learning Assistant (NALA): Customised Gen-AI tutoring chatbot to guide students based on faculty curat...",\
        "4.\xa0\xa0\xa0\xa0 I feel that the following project could potentially benefit students in NTU.\xa0d. Skills and Course Advising for Learning Excellence (SCALE): A course and co-curricular recommendation AI proj...",\
]]

df.drop(df[df['I have read and understood the instructions.'] != 'Yes'].index, inplace=True)

school_dict = {"CCEB": 8, "CEE": 10, "COE": 5, "EEE": 21, "MSE": 4, "MAE": 12,"REP":4,"SBS":11,"SCSE":22,"SPMS":13,"SSM":2,\
               "ADM":5,"ASE":1, "SOH":15, "WKWSCI":1, "NBS":22, "NIE":3, "LKCSoM":2, "SSS":6}
STEM_Schools = ["CCEB",	"CEE","COE","EEE","MSE","MAE","REP","SBS","SCSE","SPMS","SSM"]
num_STEM_Schools = 8 + 10 + 5 + 21 + 4 + 12 + 4 + 11 + 22 + 13 + 2 #112
#Science,tech,engineering,maths
non_STEM_Schools = ["ADM","ASE", "SOH", "WKWSCI", "NBS", "NIE", "LKCSoM", "SSS"]
num_Non_STEM_Schools = 5 + 1 + 15 + 1 + 22 + 3 + 2 + 6 #55
# print(df["ID"].head(20))
print(num_STEM_Schools, num_Non_STEM_Schools)

STEM_data = df.loc[df['School'].isin(STEM_Schools)]
print(len(STEM_data))
non_STEM_data = df.loc[df['School'].isin(non_STEM_Schools)]
# print(len(non_STEM_data))
# print(non_STEM_data["ID"])
# print(non_STEM_data.loc[non_STEM_data['1.\xa0\xa0\xa0\xa0\xa0I keep track of my own learning data (e.g. tracking hours spent on a module per week, strengths and weakness in terms of course topics).2']=="Agree"])
# print(non_STEM_data.loc[non_STEM_data['1.\xa0\xa0\xa0\xa0\xa0I keep track of my own learning data (e.g. tracking hours spent on a module per week, strengths and weakness in terms of course topics).2']=="Strongly agree"])
# print(non_STEM_data.loc[non_STEM_data['1.\xa0\xa0\xa0\xa0\xa0I keep track of my own learning data (e.g. tracking hours spent on a module per week, strengths and weakness in terms of course topics).2']=="Neutral"])
# print(non_STEM_data.loc[non_STEM_data['1.\xa0\xa0\xa0\xa0\xa0I keep track of my own learning data (e.g. tracking hours spent on a module per week, strengths and weakness in terms of course topics).2']=="Disagree"])
# print(len(non_STEM_data.loc[non_STEM_data['1.\xa0\xa0\xa0\xa0\xa0I keep track of my own learning data (e.g. tracking hours spent on a module per week, strengths and weakness in terms of course topics).2']=="Strongly disagree"]))


def quantitative_filter(df,column_name):
    # returns [strongly agree, agree, Neutral, disagree, Strongly disagree]
    res = []
    res.append(len(df.loc[df[column_name]=="Strongly agree"]))
    res.append(len(df.loc[df[column_name]=="Agree"]))
    res.append(len(df.loc[df[column_name]=="Neutral"]))
    res.append(len(df.loc[df[column_name]=="Disagree"]))
    res.append(len(df.loc[df[column_name]=="Strongly disagree"]))
    return res

def quantitative_filter2(df,column_name):
    # returns [strongly agree, agree, Neutral, disagree, Strongly disagree]
    res = []
    res.append(len(df.loc[df[column_name]=="Strongly Agree"]))
    res.append(len(df.loc[df[column_name]=="Agree"]))
    res.append(len(df.loc[df[column_name]=="Neutral"]))
    res.append(len(df.loc[df[column_name]=="Disagree"]))
    res.append(len(df.loc[df[column_name]=="Strongly Disagree"]))
    return res
def section_One_Quantitative(data):
    res_dict = {}
    res = quantitative_filter(data,'1.\xa0\xa0\xa0\xa0\xa0I keep track of my own learning data (e.g. tracking hours spent on a module per week, strengths and weakness in terms of course topics).2')
    # print(res)
    # print([res[0]+res[1],res[2],res[3]+res[4]])
    res_dict["q1"]=[res[0]+res[1],res[2],res[3]+res[4]]
    res = quantitative_filter(data,'2.\xa0\xa0\xa0\xa0 It is important to keep track and analyse my own learning data.2')
    # print(res)
    # print([res[0]+res[1],res[2],res[3]+res[4]])
    res_dict["q2"]=[res[0]+res[1],res[2],res[3]+res[4]]
    res = quantitative_filter(data,'3.\xa0\xa0\xa0\xa0 I will adjust my study habits or learning strategies based on insights from learning analytics.2')
    # print(res)
    # print([res[0]+res[1],res[2],res[3]+res[4]])
    res_dict["q3"]=[res[0]+res[1],res[2],res[3]+res[4]]
    return res_dict

def section_Two_Quantitative(data):
    res_dict = {}
    res = quantitative_filter2(data,"1.\xa0\xa0\xa0\xa0 I know that the university has put in place a student data governance policy in line with PDPC.2")
    # print(res)
    # print([res[0]+res[1],res[2],res[3]+res[4]])
    res_dict["q1"]=[res[0]+res[1],res[2],res[3]+res[4]]
    res = quantitative_filter2(data,"2.\xa0 \xa0 \xa0The university should ask for my explicit consent for learning analytics projects if it involves any identifiable data about me (e.g., name, ethnicity, age, and gender).2")
    # print(res)
    # print([res[0]+res[1],res[2],res[3]+res[4]])
    res_dict["q2"]=[res[0]+res[1],res[2],res[3]+res[4]]
    res = quantitative_filter2(data,"3.\xa0\xa0\xa0\xa0 I am comfortable with the idea of NTU collecting data on my learning behaviours and performances to improve teaching and learning.2")
    # print(res)
    # print([res[0]+res[1],res[2],res[3]+res[4]])
    res_dict["q3"]=[res[0]+res[1],res[2],res[3]+res[4]]
    res = quantitative_filter2(data,"4.\xa0\xa0\xa0\xa0 It is important to me that I can opt out of the collection of my learning data for my professors and tutors. 2")
    # print(res)
    # print([res[0]+res[1],res[2],res[3]+res[4]])
    res_dict["q4"]=[res[0]+res[1],res[2],res[3]+res[4]]
    res = quantitative_filter2(data,"5.\xa0\xa0\xa0\xa0 It is important to me that I can opt out of the collection of my learning data to be used by myself.2")
    # print(res)
    # print([res[0]+res[1],res[2],res[3]+res[4]])
    res_dict["q5"]=[res[0]+res[1],res[2],res[3]+res[4]]
    return res_dict

def section_Three_Quantitative(data):
    res_dict = {}
    res = quantitative_filter2(data,"1.\xa0\xa0\xa0\xa0 The university should regularly update me about my learning progress based on the analysis of my educational data.3")
    # print(res)
    # print([res[0]+res[1],res[2],res[3]+res[4]])
    res_dict["q1"]=[res[0]+res[1],res[2],res[3]+res[4]]
    res = quantitative_filter2(data,"2.\xa0 \xa0The learning analytics service should show how my learning progress compares to the course learning outcomes.3")
    # print(res)
    # print([res[0]+res[1],res[2],res[3]+res[4]])
    res_dict["q2"]=[res[0]+res[1],res[2],res[3]+res[4]]
    res = quantitative_filter2(data,"3.\xa0\xa0\xa0\xa0 I expect the teaching staff to act (i.e. support me) if the analytics show that I am at-risk of failing, underperforming or needs improvement in my learning.3")
    # print(res)
    # print([res[0]+res[1],res[2],res[3]+res[4]])
    res_dict["q3"]=[res[0]+res[1],res[2],res[3]+res[4]]
    res = quantitative_filter2(data,"4.\xa0\xa0\xa0\xa0 I feel that the following project could potentially benefit students in NTU. a. Early AleRT for Learning Intervention (EARLI): A predictive AI project to detect and support at-risk students...")
    # print(res)
    # print([res[0]+res[1],res[2],res[3]+res[4]])
    res_dict["q4"]=[res[0]+res[1],res[2],res[3]+res[4]]
    res = quantitative_filter2(data,"4.\xa0\xa0\xa0\xa0 I feel that the following project could potentially benefit students in NTU. b. Course Analytics Dashboard for Students (CADS): A personalised learning analytics project that provides facul...")
    # print(res)
    # print([res[0]+res[1],res[2],res[3]+res[4]])
    res_dict["q5"]=[res[0]+res[1],res[2],res[3]+res[4]]
    res = quantitative_filter2(data,"4.\xa0\xa0\xa0\xa0 I feel that the following project could potentially benefit students in NTU.\xa0c. NTU AI Learning Assistant (NALA): Customised Gen-AI tutoring chatbot to guide students based on faculty curat...")
    # print(res)
    # print([res[0]+res[1],res[2],res[3]+res[4]])
    res_dict["q6"]=[res[0]+res[1],res[2],res[3]+res[4]]
    res = quantitative_filter2(data,"4.\xa0\xa0\xa0\xa0 I feel that the following project could potentially benefit students in NTU.\xa0d. Skills and Course Advising for Learning Excellence (SCALE): A course and co-curricular recommendation AI proj...")
    # print(res)
    # print([res[0]+res[1],res[2],res[3]+res[4]])
    res_dict["q7"]=[res[0]+res[1],res[2],res[3]+res[4]]
    return res_dict
'''No categorisation'''
s1 = section_One_Quantitative(df)
s2 = section_Two_Quantitative(df)
s3 = section_Three_Quantitative(df)
# print(s1.value_counts())

# Categorisation by STEM/non_STEM
s1_STEM = section_One_Quantitative(STEM_data)
s1_non_STEM = section_One_Quantitative(non_STEM_data)
s2_STEM = section_Two_Quantitative(STEM_data)
s2_non_STEM = section_Two_Quantitative(non_STEM_data)
s3_STEM = section_Three_Quantitative(STEM_data)
s3_non_STEM = section_Three_Quantitative(non_STEM_data)
# print("\n\n")
# print("Section one:")
# print("\nSTEM_data")
# print("\nnon_STEM_data")
# print("\n\n")
# print("Section two:")
# print("\nSTEM_data")
# print("\nnon_STEM_data")
# print("\n\n")
# print("Section three:")
# print("\nSTEM_data")
# print("\nnon_STEM_data")



'''Categorisation by year'''

Years_dict = {"Year 1": 65, "Year 2":53, "Year 3":21, "Year 4":27, "Year 5 and above":2}

y1_data = df.loc[df["Year of Study"]=="Year 1"]
y2_data = df.loc[df["Year of Study"]=="Year 2"]
y3_data = df.loc[df["Year of Study"]=="Year 3"]
y4_data = df.loc[df["Year of Study"].isin(["Year 4","Year 5 and above"])]

print("\n\n")
print("Section one:")
print("\ny1_data")
s1_y1=section_One_Quantitative(y1_data)
print("\ny2_data")
s1_y2=section_One_Quantitative(y2_data)
print("\ny3_data")
s1_y3=section_One_Quantitative(y3_data)
print("\ny4_data")
s1_y4=section_One_Quantitative(y4_data)

print("\n\n")
print("Section two:")
print("\ny1_data")
s2_y1=section_Two_Quantitative(y1_data)
print("\ny2_data")
s2_y2=section_Two_Quantitative(y2_data)
print("\ny3_data")
s2_y3=section_Two_Quantitative(y3_data)
print("\ny4_data")
s2_y4=section_Two_Quantitative(y4_data)

print("\n\n")
print("Section three:")
print("\ny1_data")
s3_y1=section_Three_Quantitative(y1_data)
print("\ny2_data")
s3_y2=section_Three_Quantitative(y2_data)
print("\ny3_data")
s3_y3=section_Three_Quantitative(y3_data)
print("\ny4_data")
s3_y4=section_Three_Quantitative(y4_data)


# '''Categorise by section 1 qn 1'''
s1q1A = df.loc[df["1.\xa0\xa0\xa0\xa0\xa0I keep track of my own learning data (e.g. tracking hours spent on a module per week, strengths and weakness in terms of course topics).2"].isin(["Strongly agree","Agree"])]
s1q1A_s1 = section_One_Quantitative(s1q1A)
s1q1D = df.loc[df["1.\xa0\xa0\xa0\xa0\xa0I keep track of my own learning data (e.g. tracking hours spent on a module per week, strengths and weakness in terms of course topics).2"].isin(["Strongly disagree","Disagree"])]
s1q1D_s1 = section_One_Quantitative(s1q1D)
s1q1A_s2 = section_Two_Quantitative(s1q1A)
s1q1D_s2 = section_Two_Quantitative(s1q1D)
s1q1A_s3 = section_Three_Quantitative(s1q1A)
s1q1D_s3 = section_Three_Quantitative(s1q1D)

# '''Categorise by section 1 qn 2'''
s1q2A = df.loc[df["2.\xa0\xa0\xa0\xa0 It is important to keep track and analyse my own learning data.2"].isin(["Strongly agree","Agree"])]
s1q2A_s1 = section_One_Quantitative(s1q2A)
s1q2D = df.loc[df["2.\xa0\xa0\xa0\xa0 It is important to keep track and analyse my own learning data.2"].isin(["Strongly disagree","Disagree"])]
s1q2D_s1 = section_One_Quantitative(s1q2D)
s1q2A_s2 = section_Two_Quantitative(s1q2A)
s1q2D_s2 = section_Two_Quantitative(s1q2D)
s1q2A_s3 = section_Three_Quantitative(s1q2A)
s1q2D_s3 = section_Three_Quantitative(s1q2D)


'''Hypo 1 does stem/ non-STEM produce differnet answers for some questions'''
# print("\nSection 1")
# for i in s1_STEM:
#     print([s1_STEM[i][0], s1_STEM[i][1], s1_STEM[i][2], s1_STEM[i][0]/112, s1_STEM[i][2]/112])
# for i in s1_non_STEM:
#     print([s1_non_STEM[i][0], s1_non_STEM[i][1], s1_non_STEM[i][2], s1_non_STEM[i][0]/56, s1_non_STEM[i][2]/56])
# print("\nSection 2")
# for i in s2_STEM:
#     print([s2_STEM[i][0], s2_STEM[i][1], s2_STEM[i][2], s2_STEM[i][0]/112, s2_STEM[i][2]/112])
# for i in s2_non_STEM:
#     print([s2_non_STEM[i][0], s2_non_STEM[i][1], s2_non_STEM[i][2], s2_non_STEM[i][0]/56, s2_non_STEM[i][2]/56])
# print("\nSection 3")
# for i in s3_STEM:
#     print([s3_STEM[i][0], s3_STEM[i][1], s3_STEM[i][2], s3_STEM[i][0]/112, s3_STEM[i][2]/112])
# for i in s3_non_STEM:
#     print([s3_non_STEM[i][0], s3_non_STEM[i][1], s3_non_STEM[i][2], s3_non_STEM[i][0]/56, s3_non_STEM[i][2]/56])
def create_df(datalist,sectionname,sizes):
    combined_data = {
        "question": [],
        "Agree": [],
        "Neutral": [],
        "Disagree": []
    }
    for i in datalist[0]:
        for j in range(len(datalist)):
            combined_data["question"].append(sectionname[j]+"_"+ i)
            combined_data["Agree"].append(datalist[j][i][0]/sizes[j])
            combined_data["Neutral"].append(datalist[j][i][1]/sizes[j])
            combined_data["Disagree"].append(datalist[j][i][2]/sizes[j])
    for i in combined_data:
        combined_data[i]= combined_data[i][::-1]
    combined_df = pd.DataFrame(combined_data)
    return combined_df


combined_df_STEM= create_df([s1_STEM,s1_non_STEM],["STEM_S1","non_STEM_S1"],[112,56])
combined_df_year = create_df([s1_y1,s1_y2,s1_y3,s1_y4],["y1_S1","y2_S1","y3_S1",">y4_S1"],[65,53,21,29])
combined_df_no = create_df([s1],["S1"],[166])
combined_df_s1q1 = create_df([s1q1A_s1,s1q1D_s1],["Agree","Disagree"],[77,62]) #77 29 62 / 127 26 15 / 118 31 19
# combined_df = combined_df_no
# dropped = [i for i in range(0,2,1)]
# combined_df = combined_df.drop(dropped)
test_df = combined_df_no
test_df.loc[0] = combined_df_no.loc[2]
test_df.loc[1] = combined_df_STEM.loc[5]
test_df.loc[2] = combined_df_year.loc[11]
test_df.loc[3] = combined_df_s1q1.loc[4]
combined_df = test_df
# combined_df = combined_df.drop([0,1,2,3])
print(combined_df)
plot1 = combined_df.plot( 
    x = 'question', 
    kind = 'barh', 
    stacked = True, 
    title = 'Section 1 with no categorisation', 
    mark_right = True)
plt.legend (loc='upper left')
# df_total = combined_df
# df_rel = combined_df[combined_df.columns[1:]].div(df_total, 0)*100
# print(df_rel)
new_df= combined_df
new_df = new_df.drop("question",axis=1)
for n in new_df: 
    for i, (cs, ab, pc) in enumerate(zip(combined_df.iloc[:, 1:].cumsum(1)[n], combined_df[n], new_df[n])):
        
        plt.text(cs - ab / 2, i, str(np.round(pc*100, 1)) + '%',  va = 'center', ha = 'center')
plt.show()

# print([s1_STEM["q2"][0], s1_STEM["q2"][1], s1_STEM["q2"][2], s1_STEM["q2"][0]/112, s1_STEM["q2"][2]/112])
# print([s1_non_STEM["q2"][0], s1_non_STEM["q2"][1], s1_non_STEM["q2"][2], s1_non_STEM["q2"][0]/56, s1_non_STEM["q2"][2]/56])

# print([s1_STEM["q3"][0], s1_STEM["q3"][1], s1_STEM["q3"][2], s1_STEM["q3"][0]/112, s1_STEM["q3"][2]/112])
# print([s1_non_STEM["q3"][0], s1_non_STEM["q3"][1], s1_non_STEM["q3"][2], s1_non_STEM["q3"][0]/56, s1_non_STEM["q3"][2]/56])
# Section 1
# STEM vs non-STEM
# [51, 20, 41] vs [26, 9, 21] 
# [90, 14, 8] vs [37, 12, 7]
# [79, 20, 13] vs [39, 11, 6]

# Section 2
# STEM vs non-STEM
# [70, 20, 22] vs [37, 9, 10]
# [98, 10, 4] vs [49, 4, 3]
# [84, 20, 8] vs [45, 4, 7]
# [89, 18, 5] vs [51, 4, 1]
# [88, 17, 7] vs [50, 4, 2]

# Section 3
# STEM vs non-STEM
# [86, 18, 8] vs [45, 6, 3]
# [99, 8, 5] vs [49, 3, 2]
# [92, 15, 5] vs [49, 3, 2]
# [95, 11, 6] vs [45, 4, 5]
# [91, 12, 9] vs [48, 5, 1]
# [90, 12, 10] vs [45, 6, 3]
# [92, 14, 6] vs [48, 3, 3]

