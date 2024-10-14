# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#   nbhosting:
#     title: test sur le langage Python
# ---

# %% [markdown]
# License CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# Sample data for different types of charts
np.random.seed(42)

# %%
# Scatterplot
x = np.random.rand(50)
y = 2 * x + np.random.normal(0, 0.1, 50)
plt.figure(figsize=(6, 4))
plt.scatter(x, y)
plt.title('Scatterplot: Relationship between X and Y')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# %%
# Bar chart
categories = ['A', 'B', 'C', 'D', 'E']
values = [15, 25, 35, 30, 10]
plt.figure(figsize=(6, 4))
plt.bar(categories, values)
plt.title('Bar Chart: Comparing Quantities')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# %%
# Line chart
time = np.arange(10)
trend = np.sin(time) + 0.5 * time
plt.figure(figsize=(6, 4))
plt.plot(time, trend, marker='o')
plt.title('Line Chart: Trend over Time')
plt.xlabel('Time')
plt.ylabel('Value')
plt.show()

# %%
# Pie chart
segments = ['Segment A', 'Segment B', 'Segment C', 'Segment D']
sizes = [30, 20, 25, 25]
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=segments, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart: Proportions of Segments')
plt.show()

# %%
# Histogram
data = np.random.normal(0, 1, 1000)
plt.figure(figsize=(6, 4))
plt.hist(data, bins=20, edgecolor='black')
plt.title('Histogram: Distribution of Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# %%
# Box plot
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.figure(figsize=(6, 4))
plt.boxplot(data, vert=True, patch_artist=True, tick_labels=['Group 1', 'Group 2', 'Group 3'])
plt.title('Box Plot: Distribution and Outliers')
plt.ylabel('Value')
plt.show()

# %%
# Heatmap
X = np.random.rand(10,1) * 5
Y= np.random.rand(1,10) * 3
matrix = np.dot(X,Y)

plt.figure(figsize=(6, 5))
sns.heatmap(matrix, annot=True, cmap='viridis')
plt.title('Heatmap: Density or Correlation')
plt.show()

# %%
# Bubble chart
x = np.random.rand(30)
y = np.random.rand(30)
size = np.random.rand(30) * 1000
plt.figure(figsize=(6, 4))
plt.scatter(x, y, s=size, alpha=0.5)
plt.title('Bubble Chart: Size represents third variable')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# %%
# Bubble chart (with color for 4th value)
x = np.random.rand(30)
y = np.random.rand(30)
size = np.random.rand(30) * 1000
plt.figure(figsize=(6, 4))
scatter = plt.scatter(x, y, s=size, alpha=0.5, c=size)
plt.title('Bubble Chart: Size represents third variable')

cbar = plt.colorbar(scatter)
cbar.set_label('Color scale')

plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# %%
# Area chart
time = np.arange(10)
series1 = np.random.rand(10)
series2 = np.random.rand(10)
plt.figure(figsize=(6, 4))
plt.fill_between(time, series1, alpha=0.5, label='Series 1')
plt.fill_between(time, series1 + series2, alpha=0.5, label='Series 2')
plt.title('Area Chart: Evolution over time')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()

# %%
# Radar chart
labels = ['Metric 1', 'Metric 2', 'Metric 3', 'Metric 4', 'Metric 5']
values = [4, 3, 2, 5, 4]
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
values += values[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.plot(angles, values, linewidth=2, linestyle='solid')
ax.fill(angles, values, alpha=0.4)
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
plt.title('Radar Chart: Comparing Metrics')
plt.show()

# %%
# Waterfall chart
categories = ['Start', 'Increase', 'Increase 2', 'End']
values = [100, 30, 20, 110]
running_total = np.cumsum(values)
running_total = np.insert(running_total, 0, 0)
print(running_total)
fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(categories, running_total[1:] - running_total[:-1], bottom=running_total[:-1], color=['blue', 'green', 'red', 'grey'])
plt.title('Waterfall Chart: Contribution Analysis')
plt.ylabel('Value')
plt.show()

# %%
# Treemap
import squarify
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [30, 20, 25, 25]
plt.figure(figsize=(6, 4))
squarify.plot(sizes=sizes, label=labels, alpha=0.8)
plt.title('Treemap: Hierarchical Data Visualization')
plt.axis('off')
plt.show()

# %%
