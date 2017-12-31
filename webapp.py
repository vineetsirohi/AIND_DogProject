import web
import os


urls = ('/(.*)', 'index')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = web.application(urls, globals())

class index:
	def __init__(self):
		self.render = web.template.render('static')

	def GET(self, name=None):
		user_data = web.input(file="")
		return self.render.webapp("\""+user_data.file+"\"")

	def POST(self, name):
	    x = web.input(myfile={})
	    filedir = os.path.join(APP_ROOT, 'static/uploadedImages')
	    if not os.path.isdir(filedir):
	    	os.mkdir(filedir)

	    if 'myfile' in x: # to check if the file-object is created
	        filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
	        filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)

	        filepath = os.path.join(filedir,filename)
	        fout = open(filepath,'wb') # creates the file where the uploaded file should be stored
	        fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
	        fout.close() # closes the file, upload complete.
	    raise web.seeother('/?file={}'.format(filepath))


if __name__ == '__main__':
	app.run()     







# from flask import Flask, render_template, request
# import os

# app = Flask(__name__)


# APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# @app.route("/")
# def index():
# 	# path = os.path.join(APP_ROOT, "webapp.html")
# 	# print('template path: {}'.format(path))
# 	return render_template("webapp.html")
# 	# return "Hello world"

# # @app.route("/upload", methods=['POST'])
# # def upload():
# #     target = os.path.join(APP_ROOT, '/webapp/uploadImages')
    
# #     if not os.path.isdir(target):
# #         os.mkdir(target)
        
# #     for file in request.files.getlist('myfile'):
# #         print(file)
# #         filname = file.filename
# #         destination = ('/').join(target, filname)
# #         print(destination)
# #         file.save(destination)
    
# #     return render_template("webapp.html")
        
    
# if __name__=='__main__':
# 	app.run(port=4555, debug=True)