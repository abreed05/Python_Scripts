import mysql.connector
import json
def lambda_handler(event, context):
    mydb = mysql.connector.connect (
        host="",
        user="",
        password="",
        database=""
    )
    mycursor = mydb.cursor()

    try:
        test = event.get('fortune')
        mycursor.execute('INSERT INTO Fortunes (fortune_vc) VALUES ("%s")' % (test) )
        mydb.commit()
        return {
            'statusCode': 200,
            "body": test
        }


    except:
        print("Can't add fortune")