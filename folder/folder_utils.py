from .models import ClientFolder


def get_responden(self,folderID,kategori):
    myresponden=""
    if kategori=="IN":
        myresponden=get_individu(folderID)
    
    elif kategori=="SY":
        myresponden=get_syarikat(folderID)

    elif kategori=="AG":
        myresponden=get_agensi(folderID)
    
    else:
        myresponden=get_ngo(folderID)

    return myresponden


def get_individu(self, individuID=0):
    return "Maklumat Individu"


def get_syarikat(self, syarikatID=0):
    return "Maklumat Syarikat"


def get_agensi(self, agensiID=0):
    return "Maklumat Agensi"


def get_ngo(self,ngoID=0):
    return "Maklumat NGO"


def get_folder(self):
    folder=ClientFolder.objects.all()
    return folder


def get_client(self, pk):
    folder = ClientFolder.objects.get(id=pk)
    return folder
