# -*- coding: utf-8 -*-

from obspy.fdsn import Client
from obspy import UTCDateTime

rede, estacao, b_jday, e_jday = raw_input('Ex: BL AQDB 2015-001 2015-002:\n').split()

fdsn = Client(base_url="http://moho.iag.usp.br")
start = UTCDateTime("%s" %b_jday)
end = UTCDateTime("%s" %e_jday)
   
st = fdsn.get_waveforms("%s" %rede, "%s" %estacao, "", "HHZ", start, end)
st = fdsn.get_waveforms("%s" %rede, "%s" %estacao, "", "HHN", start, end)
st = fdsn.get_waveforms("%s" %rede, "%s" %estacao, "", "HHE", start, end)
st.write("%s.%s..HHZ.D.%s.%s" %(rede, estacao, b_jday[0:4], b_jday[5:] ), "MSEED")
st.write("%s.%s..HHN.D.%s.%s" %(rede, estacao, b_jday[0:4], b_jday[5:] ), "MSEED")
st.write("%s.%s..HHE.D.%s.%s" %(rede, estacao, b_jday[0:4], b_jday[5:] ), "MSEED")
