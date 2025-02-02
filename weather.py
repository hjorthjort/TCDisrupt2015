import numpy as np
# Returns a classification of the weather based on point in time and location.
# Resolution is hourly
def getWeather(time, location):
    # At present this class returns randomized weather classification, for proof of concept. For a business implementation,
    # as subscription to Open Weather Map would probably be a good idea, but these are rather expensive.
    return np.random.choice(np.arange(2,10))

# Classifications
# ID	Meaning	Icon
# 200	thunderstorm with light rain	 11d
# 201	thunderstorm with rain	 11d
# 202	thunderstorm with heavy rain	 11d
# 210	light thunderstorm	 11d
# 211	thunderstorm	 11d
# 212	heavy thunderstorm	 11d
# 221	ragged thunderstorm	 11d
# 230	thunderstorm with light drizzle	 11d
# 231	thunderstorm with drizzle	 11d
# 232	thunderstorm with heavy drizzle	 11d
# Group 3xx: Drizzle
# ID	Meaning	Icon
# 300	light intensity drizzle	 09d
# 301	drizzle	 09d
# 302	heavy intensity drizzle	 09d
# 310	light intensity drizzle rain	 09d
# 311	drizzle rain	 09d
# 312	heavy intensity drizzle rain	 09d
# 313	shower rain and drizzle	 09d
# 314	heavy shower rain and drizzle	 09d
# 321	shower drizzle	 09d
# Group 5xx: Rain
# ID	Meaning	Icon
# 500	light rain	 10d
# 501	moderate rain	 10d
# 502	heavy intensity rain	 10d
# 503	very heavy rain	 10d
# 504	extreme rain	 10d
# 511	freezing rain	 13d
# 520	light intensity shower rain	 09d
# 521	shower rain	 09d
# 522	heavy intensity shower rain	 09d
# 531	ragged shower rain	 09d
# Group 6xx: Snow
# ID	Meaning	Icon
# 600	light snow	[[file:13d.png]]
# 601	snow	[[file:13d.png]]
# 602	heavy snow	[[file:13d.png]]
# 611	sleet	[[file:13d.png]]
# 612	shower sleet	[[file:13d.png]]
# 615	light rain and snow	[[file:13d.png]]
# 616	rain and snow	[[file:13d.png]]
# 620	light shower snow	[[file:13d.png]]
# 621	shower snow	[[file:13d.png]]
# 622	heavy shower snow	[[file:13d.png]]
# Group 7xx: Atmosphere
# ID	Meaning	Icon
# 701	mist	[[file:50d.png]]
# 711	smoke	[[file:50d.png]]
# 721	haze	[[file:50d.png]]
# 731	sand, dust whirls	[[file:50d.png]]
# 741	fog	[[file:50d.png]]
# 751	sand	[[file:50d.png]]
# 761	dust	[[file:50d.png]]
# 762	volcanic ash	[[file:50d.png]]
# 771	squalls	[[file:50d.png]]
# 781	tornado	[[file:50d.png]]
# Group 800: Clear
# ID	Meaning	Icon
# 800	clear sky	[[file:01d.png]] [[file:01n.png]]
# Group 80x: Clouds
# ID	Meaning	Icon
# 801	few clouds	[[file:02d.png]] [[file:02n.png]]
# 802	scattered clouds	[[file:03d.png]] [[file:03d.png]]
# 803	broken clouds	[[file:04d.png]] [[file:03d.png]]
# 804	overcast clouds	[[file:04d.png]] [[file:04d.png]]
# Group 90x: Extreme
# ID	Meaning
# 900	tornado
# 901	tropical storm
# 902	hurricane
# 903	cold
# 904	hot
# 905	windy
# 906	hail
# Group 9xx: Additional
# ID	Meaning
# 951	calm
# 952	light breeze
# 953	gentle breeze
# 954	moderate breeze
# 955	fresh breeze
# 956	strong breeze
# 957	high wind, near gale
# 958	gale
# 959	severe gale
# 960	storm
# 961	violent storm
# 962	hurricane   'WarmDry'
