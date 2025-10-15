# ============================================================
# Student Survey Data Visualization App
# ============================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# ------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------
st.set_page_config(page_title="Scientific Visualization", layout="wide")
st.title("🎓 Scientific Visualization: Student Survey Analysis")
st.markdown("---")

# ------------------------------------------------------------
# 1️⃣ Visualization 1: Gender Distribution (Plotly Donut Chart)
# ------------------------------------------------------------
st.header("1️⃣ Gender Distribution in Arts Faculty")

gender_counts = arts_df["Gender"].value_counts()
labels = gender_counts.index
values = gender_counts.values

fig1 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
fig1.update_layout(
    title_text="Distribution of Gender in Arts Faculty",
    autosize=False,
    width=600,
    height=600,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
st.plotly_chart(fig1, use_container_width=True)

st.markdown("""
**Interpretation:**  
The gender distribution chart shows that female students form a slightly larger proportion in the Arts faculty.  
This suggests higher female participation or enrollment in this field compared to male students.
""")

# ------------------------------------------------------------
# 2️⃣ Visualization 2: Count of Male vs Female Students (Matplotlib)
# ------------------------------------------------------------
st.header("2️⃣ Count of Male vs Female Students (Bar Chart)")

gender_counts = arts_df["Gender"].value_counts()
fig2, ax = plt.subplots(figsize=(8, 6))
gender_counts.plot(kind="bar", ax=ax, color=["skyblue", "salmon"])
ax.set_title("Count of Male vs Female Students in Arts Faculty")
ax.set_xlabel("Gender")
ax.set_ylabel("Count")
ax.set_xticklabels(gender_counts.index, rotation=0)
st.pyplot(fig2)

st.markdown("""
**Interpretation:**  
The majority of resondents are female students, making up about two-thirds of the total survey population. 
This will indicates a higher participation rate among female students in feedback activities, possibly reflecting greater engagement or representation in the programs surveyed.""")

# ------------------------------------------------------------
# 3️⃣ Visualization 3: Comparison of Mean Scores (Q3 vs Q5)
# ------------------------------------------------------------
st.header("3️⃣ Comparison of Mean Scores (Expectation vs. Reality)")

mean_q3 = arts_df['Q3 [What was your expectation about the University as related to quality of resources?]'].mean()
mean_q5 = arts_df['Q5 [To what extent your expectation was met?]'].mean()

mean_scores = pd.Series({
    'Mean Q3 (Expectation about quality of resources)': mean_q3,
    'Mean Q5 (Extent expectation was met)': mean_q5
})

fig3, ax = plt.subplots(figsize=(8, 6))
mean_scores.plot(kind='bar', ax=ax, color=['cornflowerblue', 'lightgreen'])
ax.set_title('Comparison of Mean Scores for Q3 and Q5')
ax.set_ylabel('Mean Score')
ax.set_xticklabels(mean_scores.index, rotation=15, ha='right')
ax.set_ylim(0, 5)
st.pyplot(fig3)

st.markdown("""
**Interpretation:**  
The bar chart is compares students' expectations about the quality of universuty resources with how much their expectations were met. 
The results show that the students rated their actual experience slightly higher than their initial expectations. 
This means that the most students felt the quality of the university's resources was better that they had expected. 
Overall, it suggests that the university is doing a good job in providing learning resources that meet or even exceed students' expectations.""")

# ------------------------------------------------------------
# 4️⃣ Visualization 4: Best Aspect of the Program (Pie Chart)
# ------------------------------------------------------------
st.header("4️⃣ Best Aspect of the Program (Q7)")

q7_counts = arts_df["Q7. In your opinion,the best aspect of the program is"].value_counts()

fig4, ax = plt.subplots(figsize=(8, 8))
ax.pie(q7_counts, labels=q7_counts.index, autopct='%1.1f%%', startangle=140)
ax.set_title("Distribution of Responses for Best Aspect of the Program (Q7)")
ax.axis("equal")
st.pyplot(fig4)

st.markdown("""
**Interpretation:**  
The majority of students identified “Teaching/Learning” as the best aspect of their program.  
This will reveals that the instructional quality is the main strength of the university, to emphasizing the effective academic delivery and supportive teaching staff.""")

# ------------------------------------------------------------
# 5️⃣ Visualization 5: Aspects to Improve (Horizontal Bar Chart)
# ------------------------------------------------------------
st.header("5️⃣ Aspects of the Program That Could Be Improved")

improvement_counts = arts_df['What aspects of the program could be improved?'].value_counts()

fig5, ax = plt.subplots(figsize=(10, 8))
improvement_counts.plot(kind='barh', ax=ax, color='lightcoral')
ax.set_title('Aspects of the Program that Could Be Improved')
ax.set_xlabel('Count')
ax.set_ylabel('Aspect')
ax.invert_yaxis()
st.pyplot(fig5)

st.markdown("""
**Interpretation:**  
Students most frequently suggested improvements in “Teaching Methods” and “Learning Environment followed by the Facilities and Environment."
This also will aligns with the student' earlier responses that showing slightly lower satisfaction with practical and infrastructural resources, which it highlighting the key focus areas for university development.""")

# ------------------------------------------------------------
# 6️⃣ Visualization 6: Expectation Met Scores by Academic Year (Box Plot)
# ------------------------------------------------------------
st.header("6️⃣ Expectation Met Scores by Academic Year")

fig6, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(
    x='Bachelor  Academic Year in EU',
    y='Q5 [To what extent your expectation was met?]',
    data=arts_df,
    palette="pastel",
    ax=ax
)
ax.set_title('Distribution of Expectation Met Scores by Academic Year')
ax.set_xlabel('Academic Year')
ax.set_ylabel('Expectation Met Score (1–5)')
st.pyplot(fig6)

st.markdown("""
**Interpretation:**  
The box plot shows that second-year students are generally the most satisfied, with their expectations being met more than other groups. 
First-year students have the lowest satisfaction levels, while third- and fourth-year students fall somewhere in between. 
This suggests that students might feel more positive about their experience after settling into university life, but satisfaction tends to balance out as they progress through later years.""")
