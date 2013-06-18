#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = Struct({'__allownew': True, 'logfile': 'ipython_log.py'})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
t = TempLatestUrl.objects.get(asdf="")
s = SiteData.objects.get(pk=5000)
s.__dict__
t = TempLatestUrl.objects.get(pk=1000)
t = TempLatestUrl.objects.get(pk=100)
t = TempLatestUrl.objects.get(pk=1)
t = TempLatestUrl.objects.all()[1000]
t.__dict__
s.__dict__
t.__dict__
