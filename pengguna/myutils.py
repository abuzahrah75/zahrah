#from django.contrib.auth.models import User
def pengurus_pasukan(self, *args, **kwargs):

    try:
        if self.user.profile:
            pengurus_pasukan = True
            id_kelas = self.user.profile.kelas.id
    except:
        pengurus_pasukan = False
        id_kelas = False
    
    return id_kelas
    

def getmykelas(self, pk):
    try:
        if self.user.profile:
            pengurus_pasukan = True
            pk = self.user.profile.kelas.id
    except:
        pass

    return pk