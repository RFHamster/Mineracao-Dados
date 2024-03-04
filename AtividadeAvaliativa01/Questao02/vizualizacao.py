# Histograma

df.hist()
plt.show()

# Gráfico Densidade

df.plot(kind='density',subplots=True,sharex=False)
plt.show()

# Box Plot

df.plot(kind='box',subplots=True,sharex=False,sharey=False)

## Multivalorados

# Gráfico Matriz Correlação

correlations=df.corr()
fig=plt.figure()
ax=fig.add_subplot(111)
cax=ax.matshow(correlations,vmin=-1,vmax=1)
fig.colorbar(cax)
ticks=numpy.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
plt.show()

# Matriz Gráfico Disperção

pandas.plotting.scatter_matrix(df)