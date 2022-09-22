import pandas as pd
import psycopg2
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
from sklearn import metrics
import streamlit as st
from bokeh.plotting import figure 

# connection database
conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' port='5432' password='admin'")

# reading sql table to pandas dataframe
df = pd.read_sql('select * from angular_velocity', con=conn)
conn.close()


features = ['flight_id','xyz_0_','xyz_1_','xyz_2_']
X = df[features]
Y = df.values[:,5:]

# spliting dataset into test and train
X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.2,random_state=100)

# function to perform training with entropy/gini ?
clf_entropy = DecisionTreeClassifier(criterion="gini",random_state=100,max_depth=10)
clf_entropy.fit(X_train,y_train)

#function to make prediction 
y_pred_en = clf_entropy.predict(X_test)
print(y_pred_en)

#!!!checking Accuracy
print("Accuracy is ",accuracy_score(y_test,y_pred_en)*100)
confusion_matrix = metrics.confusion_matrix(y_test, y_pred_en)


#--------------------------------  Dashboard  ---------------------------------

st.write('# Demo Dashboard ') #st.title('Demo Dashboard')
st.markdown('''Bu dashboard  uçus Id 68 ve 69,  modeli 3, görevi 2, 2022-09-09 tarihinde olan uçuşa ait anormal durumları 
               gösteren istatistikleri ve grafikleri içerir.''')

st.header('İstatistik')


# connection database
#conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' port='5432' password='admin'")


# reading sql table to pandas dataframe
#data = pd.read_sql('select * from angular_velocity', con=conn)
#conn.close() 


#st.write(data.info())
#st.write(data.describe())
st.write("Accuracy is  ",accuracy_score(y_test,y_pred_en)*100)
st.write("Confusion Matrix :  ",confusion_matrix)
st.write("Classification Report :  ",classification_report(y_test,y_pred_en)) 
#st.write(data.head())



# -----------------Grafik----------------------------------------------------------
# convert time to from object to datetime type
df['time'] = pd.to_datetime(df['time']) 

st.header('Grafikler ')

df_1 = df.iloc[:8471,:]
df_2 = df.iloc[8471:,:]

x = df_1['time']
y = df_1['type']


p = figure(
  title = 'Abnormal Durumlar',
  x_axis_label='Zaman',
  y_axis_label = 'Anormal'
)
p.line(x,y,legend_label='line',line_width=1)
st.bokeh_chart(p,use_container_width=True) 



x = df_2['time']
y = df_2['type']


p = figure(
  title = 'Abnormal Durumlar',
  x_axis_label='Zaman',
  y_axis_label = 'Anormal'
)
p.line(x,y,legend_label='line',line_width=1)
st.bokeh_chart(p,use_container_width=True) 

