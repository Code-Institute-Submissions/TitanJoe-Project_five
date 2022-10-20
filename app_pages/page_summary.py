import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a fungal disease of the foliage, stems and occasionally flowers "
        f"and fruit where a superficial fungal growth covers the surface of the plant.\n"
        f"* A leaf is collected and examined and visual criteria are used to "
        f"detect powdery mildew.\n"
        )

    st.info(
        f"**Project Dataset**\n"
        f"* The dataset contains 4208 cherry leaf images provided by Farmy & Foods, taken from their crops. "
        )

    st.write(
        f"* For additional information, please visit the"
        f" [Project README](https://github.com/TitanJoe/Project_five/blob/main/README.md)."
        )

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to visually differentiate "
        f"a cherry leaf that is healthy from one that contains powdery mildew.\n"
        f"* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew. "
        )