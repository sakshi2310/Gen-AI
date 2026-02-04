from langchain_community.document_loaders import WebBaseLoader

url = "https://www.flipkart.com/samsung-essential-series-s3-55-88-cm-22-inch-full-hd-led-backlit-ips-panel-d-sub-hdmi-flat-monitor-ls22d300gawxxl/p/itm909c8202e1864?pid=MONH7GHGSGF3AGM9&lid=LSTMONH7GHGSGF3AGM9N3DVIC&marketplace=FLIPKART&store=6bo%2Fg0i%2F9no&srno=b_1_1&otracker=browse&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&fm=organic&iid=en_1qY0QNnH_INrXFS_ZokOqAgX1D4At_yzK0CeKS0_ayHBbjGIosfrQCQI9ZHXp3NRJYP4Hq27WW1jsVUMmNsJyvUFjCTyOHoHZs-Z5_PS_w0%3D&ppt=None&ppn=None&ssid=mqfiu35vz40000001769509959457"
loader = WebBaseLoader(url)
docs = loader.load()


print(len(docs))


