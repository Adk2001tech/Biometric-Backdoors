import tensorflow as tf
import numpy as np



def Euclidean_dist(tensor1, tensor2):
	'''
	 Norm function to calculate euclidean distance between 
	 # Arguments
		Input: (tensor1== return form Generate_sample), (tensor2== Traget image featues)
	''' 
	norm= tf.norm(tf.math.subtract(tensor1, tensor2), ord='euclidean', axis=1) 
	return norm



def Centroid(vector):
	'''
	  After the random initialization, we first optimize the
	glasses using the adversary’s centroid in feature space(Xc)
	 # Arguments
		Input: feature vector(batch_size x feature)
	'''
	return tf.math.reduce_mean(vector, axis=1)



def Generate_sample(tensor1, tensor2, mask):
	'''
	 In order to limit the perturbations
	 into the area of the glasses, we use a binary mask 'Mx' that has the
	 size of the input space and filters out the pixels that do not lie on
	 the glasses frame
	
	 # Arguments
		Input: (tensor1== X), (tensor2== δx, shape(batch, 160, 160, 3)), mask
	'''
	tensor1= tf.math.multiply(tensor1, (1- mask))
	tensor2= tf.math.multiply(tensor2, mask)
	return tf.math.add(tensor1, tensor2)


def Generate_target(feature, batch_size):
	'''
	Template Knowledge: We assume that the adversary has at least one picture of the user’s face.

	 # Arguments
		Input: feature(1x128) for FaceNet Model
			   batch_size	
	'''
	feature_space= feature.shape[-1]
	target= []
	for i in range(batch_size):
	  target.append(feature)
	target = np.array(target)
	return target.reshape(batch_size, feature_space)




def Sample_variance(images):
	'''
	 To account for the glasses smoothness, we look for perturbations
	 that minimize total pixel variation of the ADDED perturbation(δx), computed as a function of each pixel.
	'''
	ndims = images.get_shape().ndims
	#ndims = images.ndim
	if ndims == 3:
	  # [height, width, channels]
	  # The input is a single image with shape [height, width, channels].
	  # Calculate the difference of neighboring pixel-values.
	  # The images are shifted one pixel along the height and width by slicing.
	  pixel_dif1 = images[1:, :, :] - images[:-1, :, :]
	  pixel_dif2 = images[:, 1:, :] - images[:, :-1, :]
	  #Squaring each element.
	  pixel_dif1= tf.math.square(pixel_dif1)
	  pixel_dif2= tf.math.square(pixel_dif2)

	  # Sum for all axis. (None is an alias for all axis.)
	  sum_axis = None
	elif ndims == 4:
	  # [batch, height, width, channels].

	  # Calculate the difference of neighboring pixel-values.
	  # The images are shifted one pixel along the height and width by slicing.
	  pixel_dif1 = images[:, 1:, :, :] - images[:, :-1, :, :]
	  pixel_dif2 = images[:, :, 1:, :] - images[:, :, :-1, :]
	  # Squaring each element.
	  pixel_dif1= tf.math.square(pixel_dif1)
	  pixel_dif2= tf.math.square(pixel_dif2)

	  # Only sum for the last 3 axis.
	  # This results in a 1-D tensor with the total variation for each image.
	  sum_axis = [1, 2, 3]

	# Calculate the total variation by taking the absolute value of the
	# pixel-differences and summing over the appropriate axis.
	tot_var = (
	    tf.math.reduce_sum(tf.math.abs(pixel_dif1), axis=sum_axis) +
	    tf.math.reduce_sum(tf.math.abs(pixel_dif2), axis=sum_axis))
	# Square root.
	tot_var= tf.math.sqrt(tot_var)

	return tot_var