# -*- coding: utf-8 -*-
"""C.I.E.1ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GQUpEU_4px0k0YXynzbm3XuhKacixJeI
"""

import matplotlib. pyplot as plt
import seaborn as sns
import pandas as pd
data=pd.read_csv("/content/mtcars.csv")
sns.scatterplot(x='wt',y='mpg',data=data)
plt.xlabel('wt')
plt.ylabel('mpg')
plt.title('scatter plot')
plt.show()

import matplotlib. pyplot as plt
import seaborn as sns
import pandas as pd
data=pd.read_csv("/content/mtcars.csv")
sns.boxplot(x='wt',y='mpg',data=data)
plt.xlabel('wt')
plt.ylabel('mpg')
plt.title('boxplot')
plt.show()

import matplotlib. pyplot as plt
import seaborn as sns
import pandas as pd
data=pd.read_csv("/content/mtcars.csv")
sns.barplot(x='wt',y='mpg',data=data)
plt.xlabel('wt')
plt.ylabel('mpg')
plt.title('barplot')
plt.show()

import matplotlib. pyplot as plt
import seaborn as sns
import pandas as pd
data=pd.read_csv("/content/mtcars.csv")
plt.hist(data['mpg'], bins=10, edgecolor='black', alpha=0.5)
plt.xlabel('miles per gallon (mpg)')
plt.ylabel('frequency')
plt.title('histogram of miles per gallon (mpg)')
plt.grid(True)
plt.show()