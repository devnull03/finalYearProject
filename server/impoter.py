import os

def importTesting(folderName,inputArgs) :
	for i in os.listdir(folderName) :
		with open(f"imports/{i}","r") as file :
			sol = file.read()
			for arg in inputArgs :
				exec('\n'.join([
					sol,
					f'''with open("temp.txt","w") as tempFile :  \n	tempFile.write(str(solution({arg}))) \n''']))
				with open("temp.txt") as tempFile :
					# condition here
					pass

if __name__ == "__main__" :

	print(os.listdir("imports"))

	args=[1,2,3,4,5,6,7,8]

	importTesting("imports",args)
