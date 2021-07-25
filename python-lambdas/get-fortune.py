def lambda_handler(event, context):
    mydb = mysql.connector.connect (
        host="",
        user="",
        password="",
        database=""
    )

    mycursor = mydb.cursor()
    try:
        mycursor.execute("SELECT fortune_vc FROM Fortunes ORDER BY RAND() LIMIT 1;")
        myresult = mycursor.fetchall()
        return {
            'statusCode': 200,
            'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
            "body": myresult
        }

    except:
        print("Could not get fortune")