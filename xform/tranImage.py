from __future__ import print_function
import sys
sys.path.insert(0, 'src')
import transform
import numpy as np
import os
import scipy.misc
import tensorflow as tf
from utils import save_img, get_img, exists, list_files
from argparse import ArgumentParser
from collections import defaultdict
import time
import json
import subprocess
from storage_utils import StorageUtils


class XForm:
    """TODO not a pretty code -- bad usage of assert in production code, should fix
    """
    BATCH_SIZE = 4
    DEVICE = '/gpu:0'

    # get img_shape
    def ffwd(self, data_in, paths_out, checkpoint_dir, device_t='/gpu:0', batch_size=4):
        assert len(paths_out) > 0
        is_paths = type(data_in[0]) == str
        if is_paths:
            assert len(data_in) == len(paths_out)
            img_shape = get_img(data_in[0]).shape
        else:
            assert data_in.size[0] == len(paths_out)
            img_shape = X[0].shape

        g = tf.Graph()
        batch_size = min(len(paths_out), batch_size)
        curr_num = 0
        soft_config = tf.ConfigProto(allow_soft_placement=True)
        soft_config.gpu_options.allow_growth = True
        with g.as_default(), g.device(device_t), \
                tf.Session(config=soft_config) as sess:
            batch_shape = (batch_size,) + img_shape
            img_placeholder = tf.placeholder(tf.float32, shape=batch_shape,
                                             name='img_placeholder')

            preds = transform.net(img_placeholder)
            saver = tf.train.Saver()
            if os.path.isdir(checkpoint_dir):
                ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
                if ckpt and ckpt.model_checkpoint_path:
                    saver.restore(sess, ckpt.model_checkpoint_path)
                else:
                    raise Exception("No checkpoint found...")
            else:
                saver.restore(sess, checkpoint_dir)

            num_iters = int(len(paths_out)/batch_size)
            for i in range(num_iters):
                pos = i * batch_size
                curr_batch_out = paths_out[pos:pos+batch_size]
                if is_paths:
                    curr_batch_in = data_in[pos:pos+batch_size]
                    X = np.zeros(batch_shape, dtype=np.float32)
                    for j, path_in in enumerate(curr_batch_in):
                        img = get_img(path_in)
                        assert img.shape == img_shape, \
                            'Images have different dimensions. ' +  \
                            'Resize images or use --allow-different-dimensions.'
                        X[j] = img
                else:
                    X = data_in[pos:pos+batch_size]

                _preds = sess.run(preds, feed_dict={img_placeholder:X})
                for j, path_out in enumerate(curr_batch_out):
                    save_img(path_out, _preds[j])

            remaining_in = data_in[num_iters*batch_size:]
            remaining_out = paths_out[num_iters*batch_size:]
        if len(remaining_in) > 0:
            self.ffwd(remaining_in, remaining_out, checkpoint_dir,
                device_t=device_t, batch_size=1)

    def ffwd_to_img(self, in_path, out_path, checkpoint_dir, device='/cpu:0'):
        paths_in, paths_out = [in_path], [out_path]
        self.ffwd(paths_in, paths_out, checkpoint_dir, batch_size=1, device_t=device)

    def ffwd_different_dimensions(self, in_path, out_path, checkpoint_dir,
                device_t=DEVICE, batch_size=4):
        in_path_of_shape = defaultdict(list)
        out_path_of_shape = defaultdict(list)
        for i in range(len(in_path)):
            in_image = in_path[i]
            out_image = out_path[i]
            shape = "%dx%dx%d" % get_img(in_image).shape
            in_path_of_shape[shape].append(in_image)
            out_path_of_shape[shape].append(out_image)
        for shape in in_path_of_shape:
            print('Processing images of shape %s' % shape)
            self.ffwd(in_path_of_shape[shape], out_path_of_shape[shape],
                checkpoint_dir, device_t, batch_size)

    def process_image(self, imageFile, styleID, upload=False):
        """
        From userId -
        get the uploaded photo image from S3
        get the style image from S3

        process Image
        store the out image to S3 and return back status
        ##Deleting the input and output image can be take care of later

        the renderer will decice how to display
        """
        modelRoot = os.environ.get('MODELDIR', False)
        if modelRoot == False:
            return False, "env variable MODELDIR is not set"
        if styleID == 'tony':
            checkpoint_dir = os.path.join(modelRoot,"tonyCheck/")
        elif styleID == 'tigris':
            checkpoint_dir = os.path.join(modelRoot,"tigrisCheck/")
        elif styleID == 'stripes':
            checkpoint_dir = os.path.join(modelRoot,"stripeCheck/")
        else:
            return False, "Style Model not supported"
        outFile = None
        outExt  = '_{}_xform.jpg'.format(styleID)
        if '.photo' in imageFile:
            fileName = imageFile.split('.photo')[0]
        else:
            fileName = imageFile.split('.')[0]
        remoteFile = fileName.rsplit('/')[-1] + outExt
        outFile    = fileName + outExt

        if os.path.exists(outFile):
            os.remove(outFile)

        #TODO add GPU enable from config file later on
        self.ffwd_to_img(imageFile, outFile, checkpoint_dir) #, device=opts.device)
        if os.path.isfile(outFile) and os.path.getsize(outFile) > 1000:
            msg = "outfile generated as: {}".format(outFile)
            if upload == True:
                su = StorageUtils()
                st, uploadMsg = su.fileUpload(outFile, remoteFile)
                msg = msg + "; "+ uploadMsg
            return True, imageFile, msg
        return False, None, "Failed in XFORM"


def main():
    xf = XForm()
    tic = time.time()
    status, msg = xf.process_image('/tmp/group.jpg', 'tony') #, True)
    print("status = {}, Msg = {}".format(status, msg))
    toc = time.time()
    print(toc - tic)

    #multiple file processing - not required
    #files = list_files(opts.in_path)
    #full_in = [os.path.join(opts.in_path,x) for x in files]
    #full_out = [os.path.join(out_path,x) for x in files]
    #if opts.allow_different_dimensions:
    #    xf.ffwd_different_dimensions(full_in, full_out, checkpoint_dir,
    #            device_t=opts.device, batch_size=opts.batch_size)
    #else :
    #    ffwd(full_in, full_out, checkpoint_dir, device_t=opts.device,
    #            batch_size=opts.batch_size)

if __name__ == '__main__':
    main()
