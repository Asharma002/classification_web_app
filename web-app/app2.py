
# import os
# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# from flask import Flask, render_template, request
# from keras.models import load_model
# from keras.preprocessing import image
# import numpy as np
# import cv2
# app = Flask(__name__)

# dic = {0 : 'wheelchair racing', 1 : 'wheelchair basketball', 2 : 'weightlifting'}

# model_path='C:/Users/KIIT/OneDrive/Desktop/deploy/my_model.h5'
# model=load_model(model_path)
# model.make_predict_function()


# def predict_label(img_path):
# 	i = image.load_img(img_path, target_size=(224,224))
# 	i = image.img_to_array(i)
#     # i = cv2.resize(i,(224,224))
# 	i = i.reshape(1, 224,224,3)
#     p = model.predict(i)

# 	# p = np.argmax(model.predict(i))
    
# 	return dic[p[0]]


# # routes
# @app.route("/", methods=['GET', 'POST'])
# def main():
# 	return render_template("index.html")



# @app.route("/submit", methods = ['GET', 'POST'])
# def get_output():
# 	if request.method == 'POST':
# 		img = request.files['my_image']

# 		img_path = "./images/" + img.filename	
# 		img.save(img_path)

# 		p = predict_label(img_path)

# 	return render_template("index.html", prediction = p, img_path = img_path)


# if __name__ =='__main__':
# 	#app.debug = True
# 	app.run(debug = True)




from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image

app = Flask(__name__)

dic = {0 : 'wheelchair racing', 1 : 'wheelchair basketball', 2 : 'weightlifting'}

model_path='C:/Users/KIIT/OneDrive/Desktop/deploy/my_model.h5'
model=load_model(model_path)
model.make_predict_function()
model.make_predict_function()

def predict_label(img_path):
	i = image.load_img(img_path, target_size=(224,224))
	i = image.img_to_array(i)
	i = i.reshape(1, 224,224,3)
	p = model.predict_classes(i)
	return dic[p[0]]
# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/about")
def about_page():
	return "Please subscribe  Artificial Intelligence Hub..!!!"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "./images/" + img.filename	
		img.save(img_path)

		p = predict_label(img_path)

	return render_template("index.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)