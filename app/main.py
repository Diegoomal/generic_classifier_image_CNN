import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # needed for GPU access

from generic_classifier_image_CNN import GenericClassifierImageCNN


if __name__ == "__main__":

    gci_cnn = GenericClassifierImageCNN(path_dataset='../dataset')

    gci_cnn.verify_gpu()
    gci_cnn.test_dataset()
    
    hist, model = gci_cnn.run_train()

    gci_cnn.predict(model=model, path_test='/tests/', filename='0.jpg')
    gci_cnn.predict(model=model, path_test='/tests/', filename='1.jpg')
    gci_cnn.predict(model=model, path_test='/tests/', filename='2.jpg')
    # gci_cnn.predict(model=model, path_test='/tests/', filename='3.jpg')
    # gci_cnn.predict(model=model, path_test='/tests/', filename='4.jpg')
    # gci_cnn.predict(model=model, path_test='/tests/', filename='5.jpg')
    # gci_cnn.predict(model=model, path_test='/tests/', filename='6.jpg')
    # gci_cnn.predict(model=model, path_test='/tests/', filename='7.jpg')
    # gci_cnn.predict(model=model, path_test='/tests/', filename='8.jpg')
