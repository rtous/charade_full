# charade

## 2D keypoints with OpenPose

cd /Users/rtous/DockerVolume/openpose

./build/examples/openpose/openpose.bin --image_dir ../charade/img --display 0 --write_json ../charade/result/2D/keypoints --write_images ../charade/result/2D/images --face --hand

## 3D joints

cd /Users/rtous/DockerVolume/flashback_smplify-x

source venv/bin/activate 

python smplifyx/main.py --config cfg_files/fit_smplx.yaml \
    --data_folder /Users/rtous/DockerVolume/charade/input \
    --use_cuda="False" \
    --output_folder /Users/rtous/DockerVolume/charade/result/3D \
    --visualize="False" \
    --model_folder models \
    --vposer_ckpt models/vposer_v1_0 \
    --part_segm_fn smplx_parts_segm.pkl

## 2D keypoints with HRNet

cd charade

sshpass -p 'so0jyCB&661e' scp -P 2275 -r input/images/* jpoveda@gso.ac.upc.edu:simple-HigherHRNet/input

sshpass -p 'so0jyCB&661e' ssh -p 2275 jpoveda@gso.ac.upc.edu

cd simple-HigherHRNet/

source myvenv/bin/activate 

python python hrnet_test.py

exit

sshpass -p 'so0jyCB&661e' scp -P 2275 -r jpoveda@gso.ac.upc.edu:simple-HigherHRNet/output/* input/keypointsHRNET




## copyright

https://guides.lib.umich.edu/permissions/films