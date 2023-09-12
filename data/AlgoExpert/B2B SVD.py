from sklearn.decomposition import TruncatedSVD

def b2b_svd(avg_trxn_amount, num_monthly_trxn):
    average_monthly_total = avg_trxn_amount.mul(num_monthly_trxn)
    average_monthly_total_T = average_monthly_total.T
    enterprise_svd = TruncatedSVD(n_components=10, n_iter=10)
    enterprise_embeddings = enterprise_svd.fit_transform(average_monthly_total_T)
    return list(average_monthly_total_T.iloc[enterprise_embeddings.argmax(axis=0)].index.values)
