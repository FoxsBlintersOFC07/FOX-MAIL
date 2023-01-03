# use python3 ya bro
# Liat apa anjing >:(
try:
	import requests as r, random, json, os
	from time import sleep
except ModuleNotFoundError:
	exit("[!] Module not installed")

list_mail = ["vintomaper.com","tovinit.com","mentonit.net"]
url = "https://cryptogmail.com/"
num = 0

def get_teks(accept, key):
	cek = r.get(url+"api/emails/"+key, headers={"accept": accept}).text
	if "error" in cek:
		return "-"
	else:
		return cek.strip()

def get_random(digit):
	lis = list("abcdefghijklmnopqrstuvwxyz0123456789")
	dig = [random.choice(lis) for _ in range(digit)]
	return "".join(dig), random.choice(list_mail)

def animate(teks):
	lis = list("\|/-")
	for cy in lis:
		print("\r["+cy+"] "+str(teks)+".. ", end="")
		sleep(0.5)

def run(email):
	while True:
		try:
			animate("Aguardando mensagens...")
			raun = r.get(url+"api/emails?inbox="+email).text
			if "404" in raun:
				continue
			elif "data" in raun:
				z = json.loads(raun)
				for data in z["data"]:
					print("\r[•] ID: "+data["id"], end="\n")
					got = json.loads(r.get(url+"api/emails/"+data["id"]).text)
					pengirim = got["data"]["sender"]["display_name"]
					email_pe = got["data"]["sender"]["email"]
					subject  = got["data"]["subject"]
					print("\r[•] Sender Name: "+pengirim, end="\n")
					print("\r[•] Sender mail: "+email_pe, end="\n")
					print("\r[•] Subject    : "+subject, end="\n")
					print("\r[•] Message    : "+get_teks("text/html,text/plain",data["id"]), end="\n")
					atc = got["data"]["attachments"]
					if atc == []:
						print("\r[•] attachments: -", end="\n")
					else:
						print("[•] attachments: ")
						for atch in atc:
							id = atch["id"]
							name = atch["file_name"]
							name = name.split(".")[-1]
							svee = r.get("https://cryptogmail.com/api/emails/"+data["id"]+"/attachments/"+id)
							open(id+"."+name, "wb").write(svee.content)
							print("      ~ "+id+"."+name)
					print("-"*45)
					r.delete(url+"api/emails/"+data["id"])
				continue
			else:
				continue
		except (KeyboardInterrupt,EOFError):
				exit("\n[✓] Pograma terminado, encerrando ...\n")

def cek_update(version):
	check = r.get("https://raw.githubusercontent.com/hekelpro/temp-mail/main/__version__").text.strip()
	if float(version) < float(check):
		print("[✓] Update found ..\n")
		os.system("git pull")
		main()
	else:
		print("[×] Update not found, back menu")
		sleep(2)
		main()

def main():
	os.system('clear')
	global num
	print("""
   
______ _______   __     ___  ___  ___  _____ _     
|  ___|  _  \ \ / /     |  \/  | / _ \|_   _| |    
| |_  | | | |\ V /______| .  . |/ /_\ \ | | | |    
|  _| | | | |/   \______| |\/| ||  _  | | | | |    
| |   \ \_/ / /^\ \     | |  | || | | |_| |_| |____
\_|    \___/\/   \/     \_|  |_/\_| |_/\___/\_____/                                                                                                

    * Author: Fox Waynne
    * Github: https://github.com/FoxsBlintersOFC07
    * Legião : FoxsBlinters
    * YouTube: https://youtube.com/@foxsblintersofc2183

[01] Aleatório 
[02] Customizado 
[00] FECHAR
""")

	pil = input("[?] Choose: ")
	while pil == "" or not pil.isdigit():
		pil = input("[?] Choose: ")
	if pil in ["01","1"]:
		set_name, set_email = get_random(10)
		print("\n[*] Seu Email: "+set_name+"@"+set_email)
		print("[*] CTRL+ C para interromper...")
		print("-"*45)
		run(set_name+"@"+set_email)
	elif pil in ["02","2"]:
		set_name = input("[•] Nome do Email: ")
		print()
		for cy in list_mail:
			num += 1
			print(" "*5,"["+str(num)+"] @"+cy)
		print()
		set_email = input("[?] Select: ")
		while set_email == "" or not set_email.isdigit() or int(set_email) > len(list_mail):
			set_email = input("[?] Select: ")
		mail = list_mail[int(set_email)-1]
		print("\n[*] Your email: "+set_name+"@"+mail)
		print("[*] CTRL+ C para interromper..")
		print("-"*45)
		run(set_name+"@"+mail)
	elif pil in ["03","3"]:
		try:
			versi = open("__version__","r").read().strip()
		except:
			print("[!] No further updates..")
			sleep(2)
			main()
		print("[!] Please wait, check update")
		cek_update(versi)
	elif pil in ["00","0"]:
		exit("[=] Exit program, enjoyy\n")
	else:
		exit("[-] Menu not found, exit..\n")


if __name__ == "__main__":
	main()
