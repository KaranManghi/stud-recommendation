from flask import Flask,jsonify,request
from collections import defaultdict
from flask_sqlalchemy import SQLAlchemy
import psycopg2

#help taken from https://stackoverflow.com/questions/60889087/how-to-fetch-data-from-postgresql-database-using-flask-and-display-html-tables
con=psycopg2.connect(database="test",user="postgres",password="",host="127.0.0.1",port="5432")
cursor=con.cursor()

app=Flask(__name__)

#help taken from https://hackernoon.com/flask-web-programming-from-scratch-9ada8088fde1
app.config['DEBUG']=True
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://localhost/test'
# db=SQLAlchemy(app)


@app.route('/get_recommendations',methods=['GET'])
def mainn():
    
    

    # print(result[0])
    # return jsonify(result)

    




    class Stud:
        def __init__(self,name,friends):
            #here friends is a list of people the person has already studied with
            self.name=name
            self.friends=friends
        
    cursor.execute("select buds, first_name,last_name from profiles")
    result=cursor.fetchall()
    d=dict()

    for i in result:
        d[i[1]]=i[0]
    





    # Stacy=Stud("Stacy",[])
    # Aaron=Stud("Aaron",[])
    # Nancy=Stud("Nancy",[])
    # Alex=Stud("Alex",[Stacy,Nancy])
    # Rory=Stud("Rory",[])
    # Daniel=Stud("Daniel",[Rory,Stacy])
    # Joshua=Stud("Joshua",[])
    # Tony=Stud("Tony",[])
    # Karan=Stud("Karan",[Stacy,Joshua,Aaron])
    # Joshua.friends=[Karan,Tony,Daniel,Alex,Nancy]
    # # Joshua=Stud("Joshua",[Karan,Tony,Daniel,Alex,Nancy])
    # Deion=Stud("Deion",[Tony,Alex,Rory])
    # Tony.friends=[Stacy,Aaron,Deion]
    # Tony=Stud("Tony",[Stacy,Aaron,Deion])


    # connection_dict=dict(list)
    # connection_dict[Tony]=

    #credits for the got_fetch function : Prof. Ivona Bezakova, RIT
    def go_fetch(stud,quant):
        seen=[stud]
        queue=[stud]
        start=0
        end=1

        while(start<end and ( len(list(set(seen) - set(d[stud]) - set([stud]) )) <=quant)):
            start_pointer=queue[start]
            # print(len(list(set(seen) - set(stud.friends) - set([stud]) )))

            for i in d[start_pointer]:
                if i not in seen:
                    queue.append(i)
                    seen.append(i)
                    end+=1
            start+=1
        
        return list(set(seen) - set(d[stud]) - set([stud]))



    stud_to_search=request.args.get("first_name")
    number_of_stud_buds=10
    reccommended_studs=go_fetch(stud_to_search,number_of_stud_buds)

    output=[]
    recommendations=defaultdict()
    for i in reccommended_studs:
        output.append(i)

    recommendations[stud_to_search]=output

    return jsonify(recommendations)

if __name__=='__main__':
    app.run(debug=True)


