import json

#json 오픈기능
def json_load(name):
    #json 오픈
    with open(f'./trans/data/{name}.json', encoding='utf-8', ) as f:
        jsons = json.load(f)
        print(f'./trans/data/{name}.json')
    return jsons

# datas : 원문 데이터
#번역기능
def data_compare(datas, name):
    Data = json_load(name)
    for key, value in Data['Data'].items():
        datas = datas.replace(key, value)
    #변경된 데이터를 출력해주기 위해 print문을 넣어둠 마지막엔 datas를 리턴해서 보내주는 형식을 취해야함
    return datas

#데이터 추가기능
def data_add(add_eg_data, add_change_data, name):
    Data = json_load(name)
    Data["Data"][add_eg_data] = add_change_data
    with open(f'./trans/data/{name}.json', 'w', encoding='utf-8') as f:
        #ensure_ascii = False: 한글깨짐 방지
        json.dump(Data, f, indent=4, ensure_ascii=False)
    return Data

def add_f(name):
    print('실행')
    Data = {
        "Data": {

        }
    }
    with open(f'./trans/data/{name}.json', 'w', encoding='utf-8') as f:
        #ensure_ascii = False: 한글깨짐 방지
        json.dump(Data, f, indent=4, ensure_ascii=False)
    return Data
# if __name__ == '__main__':
#     # 데이터 파일 로드
#     Data = json_load()
#     #입력받기, 파일전송 or 데이터 입력중 택1
#     Data_set = open('Ch.txt').read()
#     #Data_set = input('데이터 입력 : ')
#
#     #데이터 비교 후 전송
#     data_compare(Data_set)