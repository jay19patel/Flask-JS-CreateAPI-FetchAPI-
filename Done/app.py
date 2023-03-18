from flask import Flask,Response,render_template,request,jsonify,redirect
from pymongo import MongoClient 
import json
app = Flask(__name__)


# connection 
client = MongoClient('localhost', 27017) 
db = client.My_Products_API 
myapis = db.products_apis

# Dashbord 
@app.route('/',methods=['GET','POST'])
def Dashbord():
    if request.method=="POST":
        jsondata ={
        "product_code" :request.form['p_code'],
        "product_name" :request.form['p_name'],
        "product_details" :request.form['p_details'],
        "product_price" :request.form['p_price'],
        "product_purchase_date" :request.form['p_purchase_d'],
        "product_expired_date" :request.form['p_expired_d'],
        }
        mylistdata = list(jsondata)
        database_add =myapis.insert_one(jsondata)
        return redirect('/')
    return render_template('Dashbord.html')


# GET 
@app.route('/api_get',methods=['GET'])
def GET():
    recivedata = list(myapis.find())
    for user in recivedata:
         user["_id"]=str(user["_id"])

    # print(recivedata)
    my_response= jsonify({"Status":200,"Paylod":recivedata,"Messgae":"DATA Recive Successfully"})
    return my_response

# POST 
@app.route('/api_post',methods=['POST'])
def POST():
    if request.method=="POST":

        jsondata={
        "product_code": request.json['product_code'],
        "product_name" :request.json['product_name'],
        "product_details" :request.json['product_details'],
        "product_price" :request.json['product_price'],
        "product_purchase_date" :request.json['product_purchase_date'],
        "product_expired_date" :request.json['product_expired_date'],
        }

        my_response= jsonify({"Status":201,"Paylod":jsondata,"Messgae":"DATA SAVE IN DATABASE"})
        return my_response
    print("data not posted")
    my_response= jsonify({"Status":404,"Paylod":"None","Messgae":"Some Problem in Subuming Form"})
    return my_response 

# UPDATE 
@app.route('/api_update/<id>',methods=['GET','POST'])
def UPDATE(id):
    # recivedata=myapis.find_one({"product_code":id}) 
    # # print(recivedata)
    # print(recivedata['product_purchase_date'])
    # my_response= jsonify({"Status":200,"Paylod":"None","Messgae":"Some Problem in Subuming Form"})
    # return my_response 
    return "UPDATE "

# DELETE 
@app.route('/api_delete')
def DELETE():
    return "DELETE"



# # if URL not found 
# @app.errorhandler(404)
# def error404(error=None):
#     Message = Response(response=json.dumps(
#         {
#         'Status':404,
#         'Message':'Page Not Found '
#         }),
#         status=400)
#     print("******  Error  *******")
#     return Message




# _______run_________________
if __name__=='__main__':
    app.run(debug=True)