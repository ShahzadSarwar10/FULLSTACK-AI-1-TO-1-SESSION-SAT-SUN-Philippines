import numpy as np

brokered_by,status,price,bed= np.genfromtxt('Week4/RealEstate-USA.csv',delimiter=',',usecols=(0,1,2,3),unpack=True, dtype=None,skip_header=1,invalid_raise=False)
print(brokered_by)
print(status)
print(price)
print(bed)

print("RealEstate-USA status mean: ",np.mean(price))
print("RealEstate-USA status average:",np.average(price))
print("RealEstate-USA status std:",np.std(price))
print("RealEstate-USA status mod:",np.median(price))
print("RealEstate-USA status Percentile-25",np.percentile(price,25))

print("USA Realstate price power",np.power( np.absolute(price),np.absolute(price)))