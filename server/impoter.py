import os, sys


class Checker:
	def __init__(self, solutions_path, check_file_path, testcases_file_path):
		self.cwd = os.getcwd()
		sys.path.append(self.cwd)
		self.solutions_path = solutions_path
		self.check_path = '\\'.join(check_file_path.split('\\')[0:-1])
		sys.path.append(self.check_path)
		self.check = __import__(check_file_path.split('\\')[-1].split('.')[0])
		self.test_cases_path = '\\'.join(testcases_file_path.split('\\')[0:-1])
		sys.path.append(self.test_cases_path)
		self.test_cases = __import__(testcases_file_path.split('\\')[-1].split('.')[0]).cases
		sys.path.append(solutions_path)
		if 'solutions' not in os.listdir():
			os.mkdir('solutions')
		
	def clean_folder(self):
		files = os.listdir(self.solutions_path)
		for file in files:
			if '.py' not in file:
				continue
			os.remove(f'{self.solutions_path}\\{file}')

	def check_files(self):
		files = os.listdir(self.solutions_path)
		results = []
		for file in files:
			if '.py' not in file:
				continue
			module = __import__(file.split('.')[0])
			try:
				l = []
				for case in self.test_cases:
					if type(case) in (list, tuple):
						res = module.solution(*case) == self.check.solution(*case)
					elif type(case) is dict:
						res = module.solution(**case) == self.check.solution(**case)
					else:
						res = module.solution(case) == self.check.solution(case)
					l.append(res)
			except:
				l = [False]
			with open(f'{self.solutions_path}\\{file}', 'r') as f:
				file_length = len(f.read())
			results.append((file.split('.')[0], (l.count(True)/len(l))*100, file_length))
		return results


if __name__ == "__main__":

	c = Checker(
		"C:\\Users\\Dell\\OneDrive\\Documents\\Code stuff\\Python\\projects\\Coc\\server\\solutions",
		"C:\\Users\\Dell\\OneDrive\\Documents\\Code stuff\\Python\\projects\\Coc\\test_files\\check.py",
		"C:\\Users\\Dell\\OneDrive\\Documents\\Code stuff\\Python\\projects\\Coc\\test_files\\test_cases.py"
	)
	print(
		c.check_files()
	)
	# c.clean_folder()
