a <- matrix(c(1,2,3,4,5,2,3,2,5,3,5,5,5,3,2), nrow=3, byrow=1)
mr <- rowMeans(a)
for (i in 1:nrow(a)) a[i,] <- a[i,] - mr[i]
mc <- colMeans(a)
for (i in 1:ncol(a)) a[,i] <- a[,i] - mc[i]