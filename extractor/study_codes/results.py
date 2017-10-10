import pandas as pd 


class ExtractorDB:

    def __init__(self):
        self.urls = pd.read_csv('../../classifier/dataframe/urls.csv')

        self.db =[]
        self.zapimoveis = []
        self.expoimovel = []
        self.olx = []
        self.directimoveis = []
        self.imovelavenda = []
        self.imovelweb = []
        self.lugarcerto = []
        self.redeimoveispe = []
        self.teuimovel = []
        self.vivareal = []


        for index, webpage in self.urls.iterrows():
            if webpage['label'] == 1:
                if webpage['site'].find('zapi') != -1:
                    self.zapimoveis.append(webpage['site'])
                elif webpage['site'].find('expoimovel') != -1:
                    self.expoimovel.append(webpage['site'])
                elif webpage['site'].find('olx') != -1:
                    self.olx.append(webpage['site'])
                elif webpage['site'].find('directimoveis') != -1:
                    self.directimoveis.append(webpage['site'])
                elif webpage['site'].find('imovelavenda') != -1:
                    self.imovelavenda.append(webpage['site'])
                elif webpage['site'].find('imovelweb') != -1:
                    self.imovelweb.append(webpage['site'])
                elif webpage['site'].find('lugarcerto') != -1:
                    self.lugarcerto.append(webpage['site'])
                elif webpage['site'].find('redeimoveispe') != -1:
                    self.redeimoveispe.append(webpage['site'])
                elif webpage['site'].find('teuimovel') != -1:
                    self.teuimovel.append(webpage['site'])
                elif webpage['site'].find('vivareal') != -1:
                    self.vivareal.append(webpage['site'])

        self.db.append(self.zapimoveis)
        self.db.append(self.expoimovel)
        self.db.append(self.olx)
        self.db.append(self.directimoveis)
        self.db.append(self.imovelavenda)
        self.db.append(self.imovelweb)
        self.db.append(self.lugarcerto)
        self.db.append(self.redeimoveispe)
        self.db.append(self.teuimovel)
        self.db.append(self.vivareal)

    def get_domain(self, domain):
        if domain.find('zapi') != -1:
            return self.db[0]
        elif domain.find('expoimovel') != -1:
            return self.db[1]
        elif domain.find('olx') != -1:
            return self.db[2]
        elif domain.find('directimoveis') != -1:
            return self.db[3]
        elif domain.find('imovelavenda') != -1:
            return self.db[4]
        elif domain.find('imovelweb') != -1:
            return self.db[5]
        elif domain.find('lugarcerto') != -1:
            return self.db[6]
        elif domain.find('redeimoveispe') != -1:
            return self.db[7]
        elif domain.find('teuimovel') != -1:
            return self.db[8]
        elif domain.find('vivareal') != -1:
            return self.db[9]

    def get_all(self):
        return db
