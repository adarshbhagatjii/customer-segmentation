import pandas as pd 
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from kneed import KneeLocator
from sklearn.metrics import silhouette_score


# page setup 
st.set_page_config(page_title="Customer Segmentation", page_icon=":bar_chart:", layout="wide")

# load data
st.subheader("upload your data")
st.write('required columns: Annual Income (k$), Spending Score (1-100)')
file = st.file_uploader("Upload your CSV file", type=["csv"])

df= None 
if file:
    df= pd.read_csv(file)

with st.sidebar:
    st.title("Customer Segmentation")
    st.image("image1.jpg")
    if df is not None:
        features=st.multiselect("Select features for clustering", options=df.columns, default=["Annual Income (k$)", "Spending Score (1-100)"])
        df=df.loc[:, features]

def preprocessing(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            le= LabelEncoder()
            df[col]= le.fit_transform(df[col])

def elbow():
    out=[]
    k_values= range(1,11)
    for i in k_values:
        model= KMeans(n_clusters=i, random_state=42)
        model.fit(df)
        out.append(model.inertia_)
    kl= KneeLocator(range(1,11), out, curve="convex", direction="decreasing")
    df1=pd.DataFrame({"K_val": k_values, "Inertia": out})

    st.subheader("Elbow Method")
    fig=st.line_chart(data=df1, x="K_val", y="Inertia")
    return kl.elbow


if df is not None:
    st.subheader('Sample of your data')
    st.write(df.sample(10))

    preprocessing(df)

    k= elbow()

    model = KMeans(n_clusters=k)
    model.fit(df)
    labels = model.labels_
    df['Cluster'] = labels


    st.subheader("Clustered Data")
    st.scatter_chart(data=df, x=df.columns[0], y=df.columns[1], color="Cluster")