from airium import Airium

page = Airium()

page('<!DOGTYPE html>')

with page.div():
	with page.head():
		with page.title():
			page("Example")

	with page.body():
		with page.center():
			with page.table(width="700", bgcolor="#F5DADF"):
				with page.tr():
					with page.td(coldspan="3"):
						with page.center():
							with page.h1():
								page("page about me")

				with page.tr():
					with page.td():
						with page.center():
							page("<br>menu</b><br>about me<br>cats<br>more cats<br>my work<br>games")
					with page.td():
						page("<br>IB Projects:</b><br>* Extended Essay <br>* Group 4 Project <br>* Math IA <br>* Comp Sci IA")



html_str = str(page)

with open('index.html', 'w') as f:
	f.write(html_str)