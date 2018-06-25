from bs4 import BeautifulSoup
from requests import get

class GoogleScholar:
    def __init__(self, busc, page=1):
        self.page = page
        self.url_base = 'https://scholar.google.com.br/'
        self.busc = busc
        self.busc = '+'.join([x.lower() for x in self.busc.split()])

    def title(self, bs):
        try:
            return bs.find('h3',{'class':'gs_rt'}).find('a').text
        except:
            return None

    def link_abstract(self, bs):
        return bs.find('h3',{'class':'gs_rt'}).find('a').get('href')

    def infos(self, bs):
        info = bs.find('div',{'class':'gs_a'}).text
        info = info.split('-')
        authors = info[0]
        paper, *year = info[1].split(',')
        return authors, paper, year

    def links(self, bs):
        relacionado, citado_num, citado_link = None, None, None
        for tag in bs.find_all('div',{'class':'gs_fl'}):
            for link in tag.find_all('a'):
                if 'Citado' in link.text.split():
                    citado_num = link.text.split()[-1]
                    citado_link =  self.url_base+link.get('href')
                elif 'relacionados' in link.text.split():
                    relacionado = self.url_base+link.get('href')

        return relacionado, citado_num, citado_link

    def pages(self, pg):
        url = 'https://scholar.google.com.br/scholar?start={}&q={}&hl=pt-BR&as_sdt=0,5'.format(str(pg), self.busc)
        return get(url)

    def run(self, pg_i, pg_f):
        if pg_i:
            if pg_f:
                pgs = list(range(pg_i, pg_f+1))
            else:
                pgs = [pg_i]
        else:
            pgs = list(range(5))

        busca = []
        for p in pgs:
            pagina = self.pages(10*p)
            soup = BeautifulSoup(pagina.content, 'html.parser')
            blocks = soup.find_all('div',{'class':'gs_r gs_or gs_scl'})

            for block in blocks:
                authors, paper, year = self.infos(block)
                related, cited_num, cited_link = self.links(block)
                busca.append({
                    'Title': self.title(block),
                    'Link abstract': self.link_abstract(block),
                    'Authors': authors,
                    'Paper': paper,
                    'Year': ' '.join(year),
                    'Citado por': cited_num,
                    'Link of cited articles': cited_link,
                    'Related articles link': related
                })

        return busca