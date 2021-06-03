#
# Machine learning based compound screening for 3CLPro using quantitative descriptors extracted from compound SMILES
#

# Load compound SMILES
require('rcdk')
mols <- load.molecules( "3clpro_actives_inactives.smi" )

# retrieve categories of descriptors
dc <- get.desc.categories()
d1 = get.desc.names(dc[1])
d2 = get.desc.names(dc[2])
d3 = get.desc.names(dc[3])
d4 = get.desc.names(dc[4])
d5 = get.desc.names(dc[5])

# compute descriptors for training data
d1mat = t(sapply(mols, function(x) eval.desc(x, d1)))
d2mat = t(sapply(mols, function(x) eval.desc(x, d2)))
d3mat = t(sapply(mols, function(x) eval.desc(x, d3)))
d4mat = t(sapply(mols, function(x) eval.desc(x, d4)))
d5mat = t(sapply(mols, function(x) eval.desc(x, d5)))

# remove non-computable descriptors
allna1 = which(apply(d1mat, 2, function(x) all(is.na(x))))
allna2 = which(apply(d2mat, 2, function(x) all(is.na(x))))
allna3 = which(apply(d3mat, 2, function(x) all(is.na(x))))
allna4 = which(apply(d4mat, 2, function(x) all(is.na(x))))
allna5 = which(apply(d5mat, 2, function(x) all(is.na(x))))
dall = cbind(d1mat[,-allna1], d2mat, d3mat[,-allna3], d4mat[,-allna4], d5mat[,1]) 
colnames(dall)[ncol(dall)] = colnames(d5mat)[1]

# convert descriptors to numeric format
dnum = apply(dall, 2, as.numeric)

# get indices of compounds for which no descriptors could be computed
nacmpds = which(apply(dall, 1, function(x) any(is.na(x))))


# Load labels on active and inactive compounds
alldat = read.table('3clpro_actives_inactives_dat.txt', sep="\t", header=T)

#
# Apply Random Forest machine learning analysis
#
require('randomForest')

# set seed to ensure reproducibility
set.seed(1234)
rfmod = randomForest(dnum[-nacmpds,], as.factor(alldat$LABEL)[-nacmpds], ntree=250)

#
# iterate over test compounds, compute descriptors and make predictions using the trained model
#
require('iterators')
i = 1

# outcome variable to save predictions
predvec = numeric(1000000)

# Load 
moliter <- iload.molecules("MolPortAllStockCompounds.smi", type="smi")
while(rcdk:::hasNext(moliter)) {
	
	# extract descriptors
	x <- nextElem(moliter)	
	x1 = eval.desc(x, d1)[-allna1]
	x2 = eval.desc(x, d2)
	x3 = eval.desc(x, d3)[-allna3]
	x4 = eval.desc(x, d4)[-allna4]
	x5 = eval.desc(x, d5)[1]
	vals = c(x1,x2,x3,x4,x5)
	
	# set to 0, if descriptor could not be computed
	naids = which(is.na(vals))
	if(length(naids)){
	  vals[naids] = rep(0, length(naids))
	}
	
	# make prediction
	curpred = tryCatch(predict(rfmod, vals, type="prob")[,which(colnames(predprobs)=="1")], error=function(e){0})
	
	# save current probability prediction and associated compound name
	predvec[i] = curpred
	names(predvec)[i] = x$getTitle()
	
	i = i + 1

	# show current progress
	if(i %% 100 == 0)
		cat(paste("i =",i,"Cur. max:",max(predvec)," - ",names(predvec)[which.max(predvec)],"\n"))
			
}

# show summary
print(summary(predvec))

# show top compounds with highest predicted probability to be active
ord = order(predvec, decreasing=T)
print(head(predvec[ord]))

