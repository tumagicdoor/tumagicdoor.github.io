import json

result = []
def get_data(filename, islast):
    cnt = 0
    with open(filename, "r") as infile:
        for data in infile:
            cnt = cnt + 1
            print(data,len(data))
            if not (data == "[\n" or data =="]"):
                result.append(data)

        if not islast:
            result[-1] = result[-1].replace("\n","") + ",\n"
            # if cnt > 10:
            #     break


get_data("data1.json",False)
get_data("data2.json",False)
get_data("data3.json",False)
get_data("data4.json",True)
print(result)
with open("datax.json", "w") as outfile:
    outfile.write("[\n")
    for str in result:
        outfile.write(str)
    outfile.write("]")
