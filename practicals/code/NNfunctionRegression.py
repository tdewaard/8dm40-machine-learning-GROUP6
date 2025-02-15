def NNfunctionRegression(NN,dataset,features):
    import numpy as np
    """
    Appoint the dataset to a variable value and devide the dataset into a training and testing subdataset.
    """
    Z=dataset.data
    Z_train=Z[:221]
    Z_test=Z[221:]
    """
    Appoint the targets and store this information in the variables : 
    target_train and target_test.
    """
    target_train = dataset.target[:221, np.newaxis]
    target_test= dataset.target[221:, np.newaxis]
    """
    Create a matrix where the normalized dataset can be stored, and after that normalize
    the test and train data.
    """
    norm_z_train=np.zeros(Z_train.shape)
    norm_z_test=np.zeros(Z_test.shape)
    
    for i in range(features):
        min_tr=min(Z_train[:,i])
        max_tr=max(Z_train[:,i])
        normalized=(Z_train[:,i]-min_tr)/(max_tr-min_tr)
        norm_z_train[:,i]=normalized
        
    for i in range(features):
        min_te=min(Z_test[:,i])
        max_te=max(Z_test[:,i])
        normalized=(Z_test[:,i]-min_te)/(max_te-min_te)
        norm_z_test[:,i]=normalized
        
    

    """
    The classification results are stored in the variable Results. In the for loop, the distances between the sample from the 
    test data, and all of the training data is calculated and stored in the the list distance. After sorting this list, the k nearest 
    neighbours ( with minimal distance to the sample) were evaluated and their targets were averaged and the sample was given the average
    value of the nearest neighbours' target values. These averages are stored in the variable Results which is returned by this function.
    """
    Results=np.zeros((len(target_train),1))
    
    for i in range(len(target_test)):
        distance=[]
        originaldist=[]
        targets=[]
        for j in range(len(target_train)):
            verschil=np.linalg.norm(norm_z_test[i,:]-norm_z_train[j,:])
            distance.append(verschil)
            originaldist.append(verschil)
        distance.sort()
        minimaldistance=distance[:NN]
        for k in range(len(minimaldistance)):
            index_min=originaldist.index(minimaldistance[k])
            targets.append(dataset.target[index_min])
        clas=sum(targets)/NN
        Results[i,:]=clas

    return Results
