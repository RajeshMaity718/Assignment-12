import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("student_performance.csv")

# Display first 5 rows
print(df.head())                                                     # ==================================================
# Task 1: Relational Plot
# ==================================================

sns.relplot(
    data=df,
    x="Hours_Studied",
    y="Exam_Score",
    hue="Gender"
)

plt.show()

# Scatter Style Relplot

sns.relplot(
    data=df,
    x="Hours_Studied",
    y="Exam_Score",
    hue="Gender",
    kind="scatter"
)

plt.show()


# ==================================================
# Task 2: Line Plot as Scatter & Facet
# ==================================================

sns.lineplot(
    data=df,
    x="Hours_Studied",
    y="Exam_Score"
)

plt.show()

# Scatter Style Line Plot

sns.lineplot(
    data=df,
    x="Hours_Studied",
    y="Exam_Score",
    marker="o"
)

plt.show()

# Faceting using categorical column

sns.relplot(
    data=df,
    x="Hours_Studied",
    y="Exam_Score",
    col="Gender",
    kind="line"
)

plt.show()


# ==================================================
# Task 3: Distribution Plots
# ==================================================

# Histogram

sns.histplot(
    data=df,
    x="Exam_Score"
)

plt.show()

# KDE Plot

sns.kdeplot(
    data=df,
    x="Exam_Score"
)

plt.show()

# Rug Plot

sns.rugplot(
    data=df,
    x="Exam_Score"
)

plt.show()

# Histogram + KDE

sns.histplot(
    data=df,
    x="Exam_Score",
    kde=True
)

plt.show()


# ==================================================
# Task 4: Bivariate Distribution Plots
# ==================================================

# Bivariate Histogram

sns.histplot(
    data=df,
    x="Hours_Studied",
    y="Exam_Score"
)

plt.show()

# Bivariate KDE Plot

sns.kdeplot(
    data=df,
    x="Hours_Studied",
    y="Exam_Score",
    fill=True
)

plt.show()


# ==================================================
# Task 5: Matrix Plots
# ==================================================

# Pair Plot

sns.pairplot(df)

plt.show()

# Correlation Heatmap

corr = df.corr(numeric_only=True)

sns.heatmap(
    corr,
    annot=True
)

plt.show()


# ==================================================
# Task 6: Categorical Plots
# ==================================================

# Bar Plot

sns.barplot(
    data=df,
    x="Gender",
    y="Exam_Score"
)

plt.show()

# Box Plot

sns.boxplot(
    data=df,
    x="Gender",
    y="Exam_Score"
)

plt.show()

# Violin Plot

sns.violinplot(
    data=df,
    x="Gender",
    y="Exam_Score"
)

plt.show()

# Count Plot

sns.countplot(
    data=df,
    x="Gender"
)

plt.show()


# ==================================================
# Task 7: Regression Plots
# ==================================================

# Regression Plot

sns.regplot(
    data=df,
    x="Hours_Studied",
    y="Exam_Score"
)

plt.show()

# LM Plot with Hue

sns.lmplot(
    data=df,
    x="Hours_Studied",
    y="Exam_Score",
    hue="Gender"
)

plt.show()


# ==================================================
# Task 8: Multi-Plots & Figure-Level Plots
# ==================================================

# FacetGrid

g = sns.FacetGrid(
    df,
    col="Gender"
)

g.map(
    plt.scatter,
    "Hours_Studied",
    "Exam_Score"
)

plt.show()

# Relplot Dashboard

sns.relplot(
    data=df,
    x="Hours_Studied",
    y="Exam_Score",
    hue="Gender"
)

plt.show()

# Catplot Dashboard

sns.catplot(
    data=df,
    x="Gender",
    y="Exam_Score",
    kind="box"
)

plt.show()

# Displot Dashboard

sns.displot(
    data=df,
    x="Exam_Score",
    kde=True
)

plt.show()
