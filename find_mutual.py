from flask import Flask,jsonify
from collections import defaultdict

app=Flask(__name__)

@app.route('/get_recommendations',methods=['GET'])
def mainn():
    class Stud:
        def __init__(self,name,friends):
            #here friends is a list of people the person has already studied with
            self.name=name
            self.friends=friends
        

    Stacy=Stud("Stacy",[])
    Aaron=Stud("Aaron",[])
    Nancy=Stud("Nancy",[])
    Alex=Stud("Alex",[Stacy,Nancy])
    Rory=Stud("Rory",[])
    Daniel=Stud("Daniel",[Rory,Stacy])
    Joshua=Stud("Joshua",[])
    Tony=Stud("Tony",[])
    Karan=Stud("Karan",[Stacy,Joshua,Aaron])
    Joshua.friends=[Karan,Tony,Daniel,Alex,Nancy]
    # Joshua=Stud("Joshua",[Karan,Tony,Daniel,Alex,Nancy])
    Deion=Stud("Deion",[Tony,Alex,Rory])
    Tony.friends=[Stacy,Aaron,Deion]
    # Tony=Stud("Tony",[Stacy,Aaron,Deion])


    # connection_dict=dict(list)
    # connection_dict[Tony]=

    #credits for the got_fetch function : Prof. Ivona Bezakova, RIT
    def go_fetch(stud,quant):
        seen=[stud]
        queue=[stud]
        start=0
        end=1

        while(start<end and ( len(list(set(seen) - set(stud.friends) - set([stud]) )) <=quant)):
            start_pointer=queue[start]
            # print(len(list(set(seen) - set(stud.friends) - set([stud]) )))

            for i in start_pointer.friends:
                if i not in seen:
                    queue.append(i)
                    seen.append(i)
                    end+=1
            start+=1
        
        return list(set(seen) - set(stud.friends) - set([stud]))



    stud_to_search=Joshua
    number_of_stud_buds=10
    reccommended_studs=go_fetch(stud_to_search,number_of_stud_buds)

    output=[]
    recommendations=defaultdict()
    for i in reccommended_studs:
        output.append(i.name)

    recommendations[stud_to_search.name]=output

    return jsonify(recommendations)

if __name__=='__main__':
    app.run(debug=True)


