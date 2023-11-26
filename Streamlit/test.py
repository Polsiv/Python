import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Avianca")


with st.container():
    st.subheader("testing")
    st.title("testing 2")
    st.write("TESTING3")

st.write("elpepe")

for i in range (10):
    st.write(i)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What i do")
        st.write("EFGUHWYERFG;NGBHILRGTBHRGBIFRGBGFLKBGF")


# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

# df

mydataframe = np.random.randn(10, 20)
st.dataframe(mydataframe)


dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)


# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],    s
#     columns=['lat', 'lon'])

# st.map(map_data)

4.5709, -74.2973

col = pd.DataFrame({
    "LAT":[4.5709   ],
    "LON": [-74.2269311]
})

st.map(col)
#4.5868031,-85.0517031