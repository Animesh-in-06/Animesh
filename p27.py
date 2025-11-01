# print() with format() function 
ht=5
bs=3

areat= 0.5 * ht *bs

# Unindexed place holder {}
print("height = {} base = {} areat of triangle = {} ".format(ht,bs,areat))

#padding of data in place holder - by default numeric data right alighed 
print("ht = {:20} Base {:20} Area of Triangle ={:20}".format(ht,bs,areat))