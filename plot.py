def plot(self, first_time=True):
    """@brief Plots the results
    """
    import matplotlib.pyplot as plt
    from sklearn.decomposition import PCA

    markerscolor = 'bgrcmybgrcmybgrcmyk'
    if first_time:
        plt.gcf().add_subplot(111, projection='3d')
        plt.ion()
        plt.show()
    if self.X.shape[1]>3:
        if not hasattr(self, 'pca'):
            self.pca = PCA(n_components=3)
            self.pca.fit(self.X)
        Xt = self.pca.transform(self.X)
        Ct = self.pca.transform(self.centroids)
    else:
        Xt=self.X
        Ct=self.centroids
    for k in range(self.K):
        plt.gca().plot(Xt[self.clusters==k,0], Xt[self.clusters==k,1], Xt[self.clusters==k,2], '.'+markerscolor[k])
        plt.gca().plot(Ct[k,0:1], Ct[k,1:2], Ct[k,2:3], 'o'+'k',markersize=12)
    if first_time:
        plt.xlabel('dim 1')
        plt.ylabel('dim 2')
        plt.gca().set_zlabel('dim 3')
    plt.draw()
    plt.pause(0.01)
