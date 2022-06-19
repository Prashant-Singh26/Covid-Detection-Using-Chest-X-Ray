from cv2 import FileStorage
from django.shortcuts import render
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def predict(request):
    return render(request, 'predict.html')

def predictImage(request):
    print(request)
    print(request.POST.dict())
    fileobj = request.FILES['filePath']
    fs = FileSystemStorage()
    filePathName = fs.save(fileobj.name,fileobj)
    filePathName = fs.url(filePathName)

    model = load_model("models/model.h5")
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    img='.'+filePathName
    test_image = image.load_img(img, target_size=(64, 64)) #Covid
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)
    if result[0][0]==1:
        prediction = "Covid Negative"
    else:
        prediction = "Covid Positive"
    

    context= {'filePathName':filePathName, 'prediction':prediction}
    return render(request, "predict.html", context)

def protect(request):
    return render(request, 'protect.html')