# coding: utf-8
import csv
import pprint
import json
# print([json.dumps(l) for l in csv.DictReader(open('data2.csv'))])
years = 2000
for year in range(years, 2020):

    json_open = open(
        "../data/{year}/JP_DETAILS_{year}.json".format(year=year), "r", encoding="utf-8")
    json_load = json.load(json_open)
    json_load = json_load["data"]
    json_list = {}
    # print(json_load[0])
    for i in json_load:
        # print(i)
        if "genres" in i:
            for j in i["genres"]:
                # print(j["name"])
                if j["name"] not in json_list:

                    json_list[j["name"]] = 1
                else:
                    json_list[j["name"]] += 1
    json_list = sorted(json_list.items(), key=lambda x: -x[1])
    print(year, json_list)


# json_list = [{}]
# for i in range(2001, 2021):
#     json_list[0][i] = []
# # print(json_list)
# count = 0
# number = 0
# now = -1  # 今どこの番号にいるか
# # CSV ファイルの読み込み
# for year in range(2001, 2021):
#     data = []
#     jugh = False  # 上陸してるかの判定変数
#     number = 0
#     now = -1  # 今どこの番号にいるか
#     with open('table{}.csv'.format(year), 'r', encoding="utf-8_sig") as f:
#         # print(f, )
#         for row in csv.DictReader(f):
#             data.append(row)

#         for k in range(len(data)):
#             count += 1
#             # print(data[k]["上陸"])
#             # print(row["台風番号"])
#             if data[k]["台風番号"] != number:
#                 number = data[k]["台風番号"]
#                 start = k
#                 jugh = False
#             # print("ZXC"
#             if data[k]["上陸"] == "1" and jugh == False:
#                 # print(data[k]["台風番号"])
#                 typhoon = data[k]["台風番号"]
#                 typhoon = typhoon[2:4]

#                 json_list[0][year].append({"台風番号": typhoon, "台風名": data[k]["台風名"], "月": [], "日": [], "時": [],  "階級": [], "緯度": [], "経度": [], "中心気圧": [], "最大風速": [
#                 ], "50KT長径方向": [], "50KT長径": [], "50KT短径": [], "30KT長径方向": [], "30KT長径": [], "30KT短径": [], "上陸": []})
#                 now += 1
#                 jugh = True
#                 for i in range(start, len(data)):
#                     if data[i]["台風番号"] != number:
#                         break
#                     if float(data[i]["経度"]) < 180:

#                         # print(float(data[i]["経度"]))

#                         json_list[0][year][now]["月"].append(data[i]["月"])
#                         json_list[0][year][now]["日"].append(data[i]["日"])
#                         json_list[0][year][now]["時"].append(data[i]["時（UTC）"])
#                         json_list[0][year][now]["階級"].append(data[i]["階級"])
#                         json_list[0][year][now]["緯度"].append(data[i]["緯度"])
#                         json_list[0][year][now]["経度"].append(data[i]["経度"])
#                         json_list[0][year][now]["中心気圧"].append(data[i]["中心気圧"])
#                         json_list[0][year][now]["最大風速"].append(data[i]["最大風速"])
#                         json_list[0][year][now]["50KT長径方向"].append(
#                             data[i]["50KT長径方向"])
#                         json_list[0][year][now]["50KT長径"].append(
#                             data[i]["50KT長径"])
#                         json_list[0][year][now]["50KT短径"].append(
#                             data[i]["50KT短径"])
#                         json_list[0][year][now]["30KT長径方向"].append(
#                             data[i]["30KT長径方向"])
#                         json_list[0][year][now]["30KT長径"].append(
#                             data[i]["30KT長径"])
#                         json_list[0][year][now]["30KT短径"].append(
#                             data[i]["30KT短径"])

#             if count < 3:
#                 print(json_list[0])
#                 count += 1

#     # JSON ファイルへの書き込み
# with open('tyhoon-data-landing.json', 'w',  encoding="utf-8_sig") as f:
#     json.dump(json_list, f, ensure_ascii=False)

# # JSONファイルのロード
# with open('tyhoon-data-landing.json', 'r',  encoding="utf-8_sig") as f:
#     json_output = json.load(f)
