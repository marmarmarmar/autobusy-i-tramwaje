# Autobusy-i-tramwaje

First download `yolo-v3` weights from [here](https://www.dropbox.com/s/99mm7olr1ohtjbq/yolov3.weights?dl=0) to `yolo-coco` directory. Be sure that you have `docker` installed. Then run:

    make build 

in order to build a base container. Then:

    make run

In order to run app. Now you can use port `1234` to get cars positions.
