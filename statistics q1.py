import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("./Data/Frogs-subsample.csv")
colors= {'HylaMinuta':'red', 'HypsiboasCinerascens':'green'}
fig, ax = plt.subplots()
grouped = df.groupby('Species')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='MFCCs_10', y='MFCCs_17', label=key, color=colors[key])
plt.title('Frogs-subsample scatter figure')
plt.show()


axes=df.hist(column='MFCCs_10', by='Species')
axes[0].set_title('histogram_subsample_MFCCs_10_HylaMinuta', fontsize=8)
axes[1].set_title('histogram_subsample_MFCCs_10_HypsiboasCinerascens', fontsize=8)
plt.show()


axes=df.hist(column='MFCCs_17', by='Species')
axes[0].set_title('histogram_subsample_MFCCs_17_HylaMinuta', fontsize=8)
axes[1].set_title('histogram_subsample_MFCCs_17_HypsiboasCinerascens', fontsize=8)
plt.show()



for key, group in grouped:
    temp=group['MFCCs_10'].sort_values(ascending=True)
    temp=temp.reset_index(drop=True)
    axes=temp.plot.line()
    axes.set_title("line_subsample_MFCCs_10_"+str(key))
    axes.set_xlabel("count")
    axes.set_ylabel("MFCCs_10")
    plt.show()
    temp = group['MFCCs_17'].sort_values(ascending=True)
    temp = temp.reset_index(drop=True)
    axes = temp.plot.line()
    axes.set_title("line_subsample_MFCCs_17_" + str(key))
    axes.set_xlabel("count")
    axes.set_ylabel("MFCCs_17")
    plt.show()


axes=df.boxplot(by="Species", fontsize=8)
plt.suptitle('sample_data_box_graph')
plt.show()


labels=[]
CTEs=[]
error=[]
for key, group in grouped:
    labels.append(str(key)+"_M10")
    labels.append(str(key) + "_M17")
    MF_10=group['MFCCs_10'].to_numpy()
    MF_17=group['MFCCs_17'].to_numpy()
    CTEs.append(np.mean(MF_10))
    CTEs.append(np.mean(MF_17))
    error.append(np.std(MF_10))
    error.append(np.std(MF_17))
x_pos=np.arange(len(labels))
fig, ax = plt.subplots()
ax.bar(x_pos, CTEs,
       yerr=error,
       align='center',
       alpha=0.5,
       capsize=10)
ax.set_ylabel('Coefficient of Thermal Expansion')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels,fontsize=5.5)
ax.set_title('Bar graph with error bars for sample')
plt.show()


result_dict_sample={}
MF_10=df['MFCCs_10'].to_numpy()
MF_17=df['MFCCs_17'].to_numpy()
result_dict_sample["sample_MFCCs_10_mean"]=np.mean(MF_10)
result_dict_sample["sample_MFCCs_17_mean"]=np.mean(MF_17)
result_dict_sample["sample_MFCCs_10_cov"]=np.cov(MF_10)
result_dict_sample["sample_MFCCs_17_cov"]=np.cov(MF_17)
result_dict_sample["sample_MFCCs_10_std"]=np.std(MF_10)
result_dict_sample["sample_MFCCs_17_std"]=np.std(MF_17)


df=pd.read_csv("./Data/Frogs.csv")
colors= {'HylaMinuta':'red', 'HypsiboasCinerascens':'green'}
fig, ax = plt.subplots()
grouped = df.groupby('Species')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='MFCCs_10', y='MFCCs_17', label=key, color=colors[key])
plt.title('Frogs scatter figure')
plt.show()

axes=df.hist(column='MFCCs_10', by='Species')
axes[0].set_title('histogram_Frogs_MFCCs_10_HylaMinuta', fontsize=8)
axes[1].set_title('histogram_Frogs_MFCCs_10_HypsiboasCinerascens', fontsize=8)
plt.show()

axes=df.hist(column='MFCCs_17', by='Species')
axes[0].set_title('histogram_Frogs_MFCCs_17_HylaMinuta', fontsize=8)
axes[1].set_title('histogram_Frogs_MFCCs_17_HypsiboasCinerascens', fontsize=8)
plt.show()

for key, group in grouped:
    temp=group['MFCCs_10'].sort_values(ascending=True)
    temp=temp.reset_index(drop=True)
    axes=temp.plot.line()
    axes.set_title("line_Frogs_MFCCs_10_"+str(key))
    axes.set_xlabel("count")
    axes.set_ylabel("MFCCs_10")
    plt.show()

    temp = group['MFCCs_17'].sort_values(ascending=True)
    temp = temp.reset_index(drop=True)
    axes = temp.plot.line()
    axes.set_title("line_Frogs_MFCCs_17_" + str(key))
    axes.set_xlabel("count")
    axes.set_ylabel("MFCCs_17")
    plt.show()


axes=df.boxplot(by="Species", fontsize=8)
plt.suptitle('Frogs_data_box_graph')
plt.show()

labels=[]
CTEs=[]
error=[]
for key, group in grouped:
    labels.append(str(key)+"_M10")
    labels.append(str(key) + "_M17")
    MF_10=group['MFCCs_10'].to_numpy()
    MF_17=group['MFCCs_17'].to_numpy()
    CTEs.append(np.mean(MF_10))
    CTEs.append(np.mean(MF_17))
    error.append(np.std(MF_10))
    error.append(np.std(MF_17))
x_pos=np.arange(len(labels))
fig, ax = plt.subplots()
ax.bar(x_pos, CTEs,
       yerr=error,
       align='center',
       alpha=0.5,
       capsize=10)
ax.set_ylabel('Coefficient of Thermal Expansion')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels,fontsize=5.5)
ax.set_title('Bar graph with error bars for Frogs')
plt.show()

result_dict_Frogs={}
MF_10=df['MFCCs_10'].to_numpy()
MF_17=df['MFCCs_17'].to_numpy()
result_dict_Frogs["Frogs_MFCCs_10_mean"]=np.mean(MF_10)
result_dict_Frogs["Frogs_MFCCs_17_mean"]=np.mean(MF_17)
result_dict_Frogs["Frogs_MFCCs_10_cov"]=np.cov(MF_10)
result_dict_Frogs["Frogs_MFCCs_17_cov"]=np.cov(MF_17)
result_dict_Frogs["Frogs_MFCCs_10_std"]=np.std(MF_10)
result_dict_Frogs["Frogs_MFCCs_17_std"]=np.std(MF_17)

print(result_dict_sample)
print(result_dict_Frogs)