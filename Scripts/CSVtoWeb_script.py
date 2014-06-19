'''
World Bank Code| Useful scripts
Malte Ahrens, 2014
GPL v2

A quick script that converts Excel (csv) to easu tp read webpage
Done using Kraken.io, a lightweight webframework.

1. Save the Excel file as a csv file in the same directory as this python file (if you run into UTF-8 issues, save the Excel file on Google Docs and download as a csv)
2. Place the printed code into a html file in a <div class="container"></div> tag
'''

import csv

with open('projects_google.csv', newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	for row in csvreader:
		project_name = row[1]
		project_description = row[3]
		project_thoughts = row[2]
		project_imageid = row[0]
		project_documentation = row[4]
		project_stage = row[5]

		print("""<a id='""" + project_imageid + """'><div class="grid-full project-item">
	<a href='#""" + project_imageid + """'><h3>""" + project_name + """</h3></a>
	""" + project_description + """
 	<div class="row text-muted">
		<div style="vertical-align:center" class="grid-fourth"><img src="img/fabprojects/""" + project_imageid + """.jpg"></div>
		<div class="grid-three-fourths">
			<p>
				""" + project_thoughts + """
			</p>
	 		<strong>Documentation?</strong> """ + project_documentation + """
	 		<br/>
	 		<strong>Stage?</strong> """ + project_stage + """
		</div>
	</div>
</div></a>""")