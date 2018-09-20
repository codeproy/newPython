import urllib.request
import shutil
url = 'https://www.ets.org/Media/Tests/GRE/pdf/gre_research_validity_data.pdf'
output_file = r'E:\Python\file_temp.pdf'
with urllib.request.urlopen(url) as response, open(output_file, 'wb') as out_file:
     shutil.copyfileobj(response, out_file)
