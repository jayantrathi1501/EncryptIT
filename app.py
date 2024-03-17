from flask import Flask, render_template, request, redirect
app=Flask(__name__)


@app.route("/",methods=["GET","POST"])
def table():
    # return render_template("index1.html")
    if request.method=="POST":
        req = request.form
        secret_key =req.get("SK")
        text=req.get("Txt")
        ED=req.get("ED")
        for i in range(len(text)):
            if text[i]==" ":
                text=text[:i]+"-"+text[i+1:]
            
        if ED==1 or ED=="1":
            key=""
            for i in range(len(secret_key)):
                key+=str(ord(secret_key[i]))
                
            #print(key)
            for x in range(len(key)):
                k=int(key[x])
                if k<2:
                    continue
                i=0
                j=k
                
                l=len(text)%k

                encrypted_text=""
                while j<=len(text):
                    for a in range(k-1,-1,-1):
                        encrypted_text+=text[i:j][a]
                    i+=k
                    j+=k
                if l!=0:
                    encrypted_text+=text[-1*l:]
                
                text=encrypted_text
            result=text
        else:
            key1=""
            for i in range(len(secret_key)):
                key1+=str(ord(secret_key[i]))

            key=""
            for i in range(len(key1)-1,-1,-1):
                key+=key1[i]
            #print(key)

            for x in range(len(key)):
                k=int(key[x])
                if k<2:
                    continue
                i=0
                j=k
                
                l=len(text)%k
                
                encrypted_text="" 
                
                while j<=len(text):
                    for a in range(k-1,-1,-1):
                        encrypted_text+=text[i:j][a]
                    i+=k
                    j+=k
                if l!=0:
                    encrypted_text+=text[-1*l:]
                text=encrypted_text
            for i in range(len(text)):
                if text[i]=="-":
                    text=text[:i]+" "+text[i+1:]
            result=text

    else:
        result=""

    return render_template("index1.html",result=result)


if __name__=="__main__":
    app.run(debug=False,host='0.0.0.0')