import intersight.api.memory_api
import credentials
import csv


header = ["model","serial","dn","location"]
data = []

top = 1000

def get_dimm_modules(apiClient,count):
    api_instance = intersight.api.memory_api.MemoryApi(apiClient)
    #print(dir(api_instance))
    summary = api_instance.get_memory_unit_list(top=top,skip=count)
    #print(dir(summary))
    for i in summary.results:
        if i['model']:
            data.append(i['model'])
            data.append(i['serial'])
            data.append(i['dn'])
            data.append(i['location'])
            #writes the data array into the csv file
            with open('dimm_modules.csv', 'a', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(data)
                data.clear()

def main():
    apiClient = credentials.config_credentials()
    count = 0
    try:
        with open('dimm_modules.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
        while count < 64000:
            print(count)
            count = count + 1000
            get_dimm_modules(apiClient,count)
    except intersight.OpenApiException as e:
        print(e)

if __name__ == "__main__":
    main()
