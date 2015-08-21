import numpy as np
from PIL import Image
import sys
sys.path.append('../python/')
import caffe
import scipy.misc as misc
from collections import OrderedDict
# load image, switch to BGR, subtract mean, and make dims C x H x W for Caffe
im = Image.open('JPEGImages/2007_000129.jpg')


def visArch():

	def printArch(net, type="params"):
		keyslist = [key for key in net.keys()]
		tmp = OrderedDict()
		for (i, name) in enumerate(keyslist):
			# tmp[name] = net.blobs[name].data[0].shape
			tmp[name] = net[name][0].data.shape
			print name, tmp[name]
		# return tmp

	def compareArchs(net1, net2, type='params'):
		keyslist1 = [key for key in net1.keys()]
		keyslist2 = [key for key in net2.keys()]
		# print '\t', n1[:-9],'\t',n2[:-9]
		for n1,n2 in zip(keyslist1,keyslist2):
			if type=="params": # show params
				print n1,": ", net1.params[n1][0].data.shape, '\t|',n2, net2.params[n2][0].data.shape
			else: # show data
				print n1,": ", net1.params[n1].data.shape, '\t|',n2, net2.params[n2].data.shape



# for example, given a 500*500 image in 32s model
# data (3, 500, 500)
# data_input_0_split_0 (3, 500, 500)
# data_input_0_split_1 (3, 500, 500)
# conv1_1 (64, 698, 698)
# conv1_2 (64, 698, 698)
# pool1 (64, 349, 349)
# conv2_1 (128, 349, 349)
# conv2_2 (128, 349, 349)
# pool2 (128, 175, 175)
# conv3_1 (256, 175, 175)
# conv3_2 (256, 175, 175)
# conv3_3 (256, 175, 175)
# pool3 (256, 88, 88)
# conv4_1 (512, 88, 88)
# conv4_2 (512, 88, 88)
# conv4_3 (512, 88, 88)
# pool4 (512, 44, 44)
# conv5_1 (512, 44, 44)
# conv5_2 (512, 44, 44)
# conv5_3 (512, 44, 44)
# pool5 (512, 22, 22)
# fc6 (4096, 16, 16)
# fc7 (4096, 16, 16)
# score59 (60, 16, 16)
# upscore (60, 544, 544)
# score (60, 500, 500)

# for 8s network
# data (3, 500, 500)
# data_input_0_split_0 (3, 500, 500)
# data_input_0_split_1 (3, 500, 500)
# conv1_1 (64, 698, 698)
# conv1_2 (64, 698, 698)
# pool1 (64, 349, 349)
# conv2_1 (128, 349, 349)
# conv2_2 (128, 349, 349)
# pool2 (128, 175, 175)
# conv3_1 (256, 175, 175)
# conv3_2 (256, 175, 175)
# conv3_3 (256, 175, 175)
# pool3 (256, 88, 88)
# pool3_pool3_0_split_0 (256, 88, 88)
# pool3_pool3_0_split_1 (256, 88, 88)
# conv4_1 (512, 88, 88)
# conv4_2 (512, 88, 88)
# conv4_3 (512, 88, 88)
# pool4 (512, 44, 44)
# pool4_pool4_0_split_0 (512, 44, 44)
# pool4_pool4_0_split_1 (512, 44, 44)
# conv5_1 (512, 44, 44)
# conv5_2 (512, 44, 44)
# conv5_3 (512, 44, 44)
# pool5 (512, 22, 22)
# fc6 (4096, 16, 16)
# fc7 (4096, 16, 16)
# score (21, 16, 16)
# score2 (21, 34, 34)
# score2_score2_0_split_0 (21, 34, 34)
# score2_score2_0_split_1 (21, 34, 34)
# score-pool4 (21, 44, 44)
# score-pool4c (21, 34, 34)
# score-fused (21, 34, 34)
# score4 (21, 70, 70)
# score4_score4_0_split_0 (21, 70, 70)
# score4_score4_0_split_1 (21, 70, 70)
# score-pool3 (21, 88, 88)
# score-pool3c (21, 70, 70)
# score-final (21, 70, 70)
# bigscore (21, 568, 568)
# upscore (21, 500, 500)
		
# vgg 16              			  fcn-32s
# conv1_1 :  (64, 3, 3, 3) 	    | conv1_1 (64, 3, 3, 3)
# conv1_2 :  (64, 64, 3, 3) 	| conv1_2 (64, 64, 3, 3)
# conv2_1 :  (128, 64, 3, 3) 	| conv2_1 (128, 64, 3, 3)
# conv2_2 :  (128, 128, 3, 3) 	| conv2_2 (128, 128, 3, 3)
# conv3_1 :  (256, 128, 3, 3) 	| conv3_1 (256, 128, 3, 3)
# conv3_2 :  (256, 256, 3, 3) 	| conv3_2 (256, 256, 3, 3)
# conv3_3 :  (256, 256, 3, 3) 	| conv3_3 (256, 256, 3, 3)
# conv4_1 :  (512, 256, 3, 3) 	| conv4_1 (512, 256, 3, 3)
# conv4_2 :  (512, 512, 3, 3) 	| conv4_2 (512, 512, 3, 3)
# conv4_3 :  (512, 512, 3, 3) 	| conv4_3 (512, 512, 3, 3)
# conv5_1 :  (512, 512, 3, 3) 	| conv5_1 (512, 512, 3, 3)
# conv5_2 :  (512, 512, 3, 3) 	| conv5_2 (512, 512, 3, 3)
# conv5_3 :  (512, 512, 3, 3) 	| conv5_3 (512, 512, 3, 3)
# fc6 :  (4096, 25088) 	        | fc6 (4096, 512, 7, 7)
# fc7 :  (4096, 4096) 			| fc7 (4096, 4096, 1, 1)
# fc8 :  (1000, 4096) 			| score59 (60, 4096, 1, 1)