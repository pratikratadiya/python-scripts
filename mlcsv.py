import csv

for ind,val in enumerate(X_train):
  oup = y_train[ind]
  outp = [i for i,e in enumerate(oup) if e!=0][0]
  wet = new_model.predict(val.reshape(1,1,28,28))
  with open('%s.csv' % outp,'a') as fd:
    wr = csv.writer(fd,dialect='excel')
    wr.writerow([wet])             
