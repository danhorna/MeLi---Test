import requests
import json

def get_data():
    # Aclaración: el site_id siempre será "MLA" dado que el enunciado no indica que éste debe variar.
    api_items = "https://api.mercadolibre.com/sites/MLA/search?seller_id="
    api_categories = "https://api.mercadolibre.com/categories/"
    usersID = input("Ingrese el ID de los vendedores separados por espacio: ")
    separatedUsers = usersID.split()
    fileToSave = open("log.txt","w+")
    for user in separatedUsers:
        request = requests.get(api_items + user)
        jsonTotalItems = json.loads(request.text)
        offset = 0
        comparator = jsonTotalItems['paging']['total']
        while (offset < comparator):
            request = requests.get(api_items + user + "&offset=" + str(offset))
            jsonItems = json.loads(request.text)
            for item in jsonItems['results']:
                request2 = requests.get(api_categories + item['category_id'])
                jsonCategory = json.loads(request2.text)
                fileToSave.write('Item ID: ' + item['id'] + '\n')
                fileToSave.write('Titulo: ' + item['title'] + '\n')
                fileToSave.write('Categoria: ' + item['category_id'] + '\n')
                fileToSave.write('Nombre de la categoria: ' + jsonCategory['name'] + '\n')
                fileToSave.write("-----------------------------------------\n")
            offset += 50
    fileToSave.close()


if __name__ == "__main__":
    get_data()
