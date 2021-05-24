# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import streamlit as st
import pandas as pd
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    st.write("""
    # My First Streamlit App
    Hello and *welcome* !
    """)
    number = st.slider("Pick a number", 0, 100)

    chart_data = pd.DataFrame(
        np.random.randn(number, 3),
        columns=['a', 'b', 'c'])
    st.line_chart(chart_data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
