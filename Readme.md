HAAR-CASCADE PERSON IDENTIFIER:

This project contains the code to implement a custom Haar-Cascade person identifier. In order to do so, you will first have to download a custom Haar-Cascade trainer located [here](https://amin-ahmadi.com/cascade-trainer-gui/).

Once the Haar-Cascade trainer GUI has been installed, you can run ``` haar_cascade_trainer.py ``` in order to capture your positive and negative images. Whenever you are done collecting your data (the data of the person willing to be recognized), you can run the GUI in order to obtain the ```cascade.xml``` file that will be used as the configuration file for the Haar-Cascade classifier. This file will be stored at ```data_haarcascade/classifier/```

Finally you can run ``` recognizer.py  --name <person to be recognized>``` to check if the training was correctly carried out and you are recognized by the Classifier! 

Enjoy!
