
class checker:
	def __init__(self, solutions_path, check_file_path, testcases_file_path):
		import os, sys
		self.cwd = os.getcwd()
		sys.path.append(self.cwd)
		self.check_path = '\\'.join(check_file_path.split('\\')[0:-1])
		print(self.check_path)
		sys.path.append(self.check_path)
		self.check = __import__(check_file_path.split('\\')[-1].split('.')[0])
		self.test_cases_path = '\\'.join(testcases_file_path.split('\\')[0:-1])
		sys.path.append(self.test_cases_path)
		self.test_cases = __import__(testcases_file_path.split('\\')[-1].split('.')[0]).cases
		self.files = os.listdir(solutions_path)
		sys.path.append(solutions_path)
		
	def check_files(self):
		results = []
		for file in self.files:
			if '.py' not in file:
				continue
			module = __import__(file.split('.')[0])
			l = [
				module.solution(case) == self.check.solution(case) for case in self.test_cases
			]
			results.append((file.split('.')[0], (l.count(True)/len(l))*100))
		return results

if __name__ == "__main__":

	c = checker(
		"C:\\Users\\Dell\\OneDrive\\Documents\\Code stuff\\Python\\projects\\Coc\\server\\solutions",
		"C:\\Users\\Dell\\OneDrive\\Desktop\\test\\check.py",
		"C:\\Users\\Dell\\OneDrive\\Desktop\\test\\test_cases.py"
	)
	print(
		c.check_files()
	)
	