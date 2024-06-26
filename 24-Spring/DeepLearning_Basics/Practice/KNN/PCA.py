from sklearn import datasets
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 붓꽃 데이터셋 로드
iris = datasets.load_iris()
X = iris.data
y = iris.target

# PCA를 이용해 4차원 데이터를 2차원으로 변환
pca = PCA(n_components=2)
X_r = pca.fit_transform(X)

# 변환된 데이터 시각화
plt.figure()
colors = ['navy', 'turquoise', 'darkorange']
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], iris.target_names):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=.8, lw=lw,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('PCA of IRIS dataset')
plt.show()
