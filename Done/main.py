from flask import Flask,Response,render_template,request,jsonify,redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
app = Flask(__name__)


# connection 
# client = MongoClient('mongodb://mongoadmin:secret@103.77.155.78:27017/?authMechanism=DEFAULT') 
client = MongoClient('localhost', 27017) 
db = client['My_Products_API'] 
myapis = db['products_apis']

# Dashbord 
@app.route('/',methods=['GET','POST'])
def Dashbord():
    # print(request.form)
    if request.method=="POST":
       myapis.insert_one({
           'product_code':request.form['p_code'],
           'product_name':request.form['p_name']
       })
       return redirect('/')
    return render_template('main.html')

# Update Page 
@app.route('/updatePage/<id>',methods=['GET','POST'])
def UpdatePage(id):
    print("my id ",id)
    findme = myapis.find_one({"_id":ObjectId(id)})
    print(findme)
    return render_template('updatepage.html',data=findme)



@app.route('/get_api',methods=['GET'])
def GET():
    data=[]
    for x in myapis.find():
        data.append({
            'id':str(x['_id']),
            'product_code':x['product_code'],
            'product_name':x['product_name'],
        })
    return jsonify({'data':data})



# UPDATE 
@app.route('/update_api/<id>',methods=['POST','GET'])
def UPDATE(id):
    print("his is my id ",id)

    if request.method == "POST":
        # new_code = request.form['new_code']
        # new_name = request.form['new_name']
        # newvalues = { "$set": { "product_code": new_code,
        #                         "product_name": new_name,
        #                         } }

        myapis.update_one({'_id':ObjectId(id)},{ "$set": { "product_code": request.form['new_code'],
                                "product_name": request.form['new_name'],
                                } })
        return redirect('/')
    

# DELETE 
@app.route('/delete_api/<id>',methods=['GET','POST'])
def DELETE(id):
    print("delete item id",id)
    deleteitem= myapis.delete_one({"_id":ObjectId(id)})
    return redirect('/')





# _______run_________________
if __name__=='__main__':
    app.run(debug=True)