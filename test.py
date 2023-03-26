class Test: 
    @staticmethod           
    def rechercherclient(search_string):
        with open("C:/Users/cedri/Desktop/POO/client.txt", "r+") as f:
            #if os.path.exists("C:/Users/cedri/Desktop/POO/client.txt"):
                lines=f.readlines()
                print(lines)
                for line in lines:
                    start = line.find('*')
                    end = line.find('#')
                    if start != -1 and end != -1 and search_string == line[start+1:end]:
                        print("trouvé")
                        return 1
        return 0