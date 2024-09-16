class Employee:
	def __init__(self, id, name, category, contract, prevwage, newwage, warningreason=None):
		self.id = id
		self.name = name
		self.category = category
		self.contract = contract
		self.prevwage = prevwage
		self.newwage = newwage
		self.warningreason = warningreason

	@property
	def warning(self):
		if self.newwage > self.category.range.upper:
			self.warningreason = "New wage is above maximum!"
		elif self.newwage < self.category.range.lower:
			self.warningreason = "New wage is bellow minimum!"
		return self.warningreason
	
class Category:
	def __init__(self, id, name, range):
		self.id = id
		self.name = name
		self.range = range

class SalaryRange:
	def __init__(self, grade, name, lower, upper):
		self.grade = grade
		self.name = name
		self.lower = lower
		self.upper = upper

grades = [
	"Operacional Indiferenciado",
	"Operacional III",
	"Operacional II",
	"Operacional I"
]

ranges = [
	SalaryRange(grades[0], "CARPINTEIRO 3ª", 900.0, 918.0), #0
	SalaryRange(grades[1], "CARPINTEIRO 2ª", 919.0, 934.0), #1
	SalaryRange(grades[2], "CARPINTEIRO 1ª", 935.0, 995.0), #2
	SalaryRange(grades[3], "CARPINTEIRO QUALIFCADO", 996.0, 1070.0), #3
	SalaryRange(grades[0], "PINTOR OFICIAL 3", 900.0, 918.0), #4
	SalaryRange(grades[1], "PINTOR OFICIAL 2", 919.0, 918.0), #5
	SalaryRange(grades[2], "PINTOR OFICIAL 1", 953.0, 1028.0), #6
	SalaryRange(grades[3], "PINTOR QUALIFICADO", 1029.0, 1070.0), #7
	SalaryRange(grades[0], "SERRALHEIRO 3ª", 900.0, 929.0), #8
	SalaryRange(grades[1], "SERRALHEIRO 2ª", 930.0, 940.0), #9
	SalaryRange(grades[2], "SERRALHEIRO CIVIL OFICIAL 1", 941.0, 1075.0), #10
	SalaryRange(grades[3], "SERRALHEIRO QUALIFICADO", 1076.0, 1095.0), #11
	SalaryRange(grades[0], "ESTOFADOR 3ª", 900.0, 918.0), #12
	SalaryRange(grades[1], "ESTOFADOR 2ª", 919.0, 934.0), #13
	SalaryRange(grades[2], "ESTOFADOR 1ª", 935.0, 995.0), #14
	SalaryRange(grades[3], "ESTOFADOR QUALIFICADO", 996.0, 1070.0), #15
	SalaryRange(grades[0], "MECÂNICO AUTO OFICIAL 3", 900.0, 918.0), #16
	SalaryRange(grades[1], "MECÂNICO AUTO OFICIAL 2", 919.0, 952.0), #17
	SalaryRange(grades[2], "MECÂNICO AUTO OFICIAL 1", 953.0, 1040.0), #18
	SalaryRange(grades[3], "MECÂNICO QUALIFICADO", 1041.0, 1550.0), #19
	SalaryRange(grades[0], "MECATRONICO 3ª", 900.0, 953.0), #20
	SalaryRange(grades[1], "MECATRONICO 2ª", 954.0, 1128.0), #21
	SalaryRange(grades[2], "MECATRONICO 1ª", 1129.0, 1169.0), #22
	SalaryRange(grades[3], "MECATRONICO QUALIFICADO", 1170.0, 1550.0), #23
	SalaryRange(grades[0], "CHAPEIRO 3ª", 900.0, 919.0), #24
	SalaryRange(grades[1], "CHAPEIRO 2ª", 920.0, 952.0), #25
	SalaryRange(grades[2], "CHAPEIRO 1ª", 953.0, 1071.0), #26
	SalaryRange(grades[3], "CHAPEIRO QUALIFICADO", 1072.0, 1130.0), #27
	SalaryRange(grades[0], "PRÉ-OFICIAL ELECTRICISTA DO 2º ANO", 900.0, 918.0), #28
	SalaryRange(grades[1], "ELETRICISTA 2ª", 919.0, 952.0), #29
	SalaryRange(grades[2], "ELETRICISTA 1ª", 953.0, 1130.0), #30
	SalaryRange(grades[3], "ELETRICISTA QUALIFICADO", 1131.0, 1370.0), #31
	SalaryRange(grades[0], "SOLDADOR 3ª", 900.0, 920.0), #32
	SalaryRange(grades[1], "SOLDADOR 2ª", 921.0, 952.0), #33
	SalaryRange(grades[2], "SOLDADOR 1ª", 953.0, 1130.0), #34
	SalaryRange(grades[3], "SOLDADOR QUALIFICADO", 1131.0, 1370.0), #35
	SalaryRange(grades[0], "OPERADOR FABRIL 3ª", 900.0, 929.0), #36
	SalaryRange(grades[1], "OPERADOR FABRIL 2ª", 930.0, 939.0), #37
	SalaryRange(grades[2], "OPERADOR FABRIL 1ª", 940.0, 1029.0), #38
	SalaryRange(grades[3], "OPERADOR FABRIL QUALIFICADO", 1030.0, 1090.0) #39
]

groups = [
	Category(11018, "OPERADOR SERROTE OFICIAL 1", ranges[36]),
	Category(11027, "MECATRÓNICO AUTO 2ª", ranges[21]),
	Category(11091, "OPERADOR MANUTENÇÃO OFIC. 2", ranges[36]),
	Category(11145, "OPERADOR MÁQUINAS DIVERSAS", ranges[36]),
	Category(11157, "CHEFE EQUIPA", ranges[36]),
	Category(11202, "DIRETOR DEPARTAMENTO", ranges[36]),
	Category(11206, "CHEFE SERVIÇOS", ranges[36]),
	Category(11208, "CHEFE SECÇÃO", ranges[36]),
	Category(11292, "TÉCNICO III", ranges[36]),
	Category(11293, "TÉCNICO II", ranges[36]),
	Category(11294, "TÉCNICO I", ranges[36]),
	Category(11361, "TÉCNICO CONTROLE QUALIDADE", ranges[36]),
	Category(11381, "FIEL ARMAZÉM", ranges[36]),
	Category(11447, "PRÉ OFICIAL ELECTRICISTA DO 2 ANO", ranges[36]),
	Category(11487, "CARPINTEIRO CAR.EST. OF.1", ranges[2]),
	Category(11488, "CARPINTEIRO CAR.EST. OF.2", ranges[1]),
	Category(11489, "CARPINTEIRO CAR.EST. OF.3", ranges[0]),
	Category(11560, "ELECTRICISTA AUTO OFICIAL 1", ranges[30]),
	Category(11562, "ELECTRICISTA AUTO PRÉ-OFIC.", ranges[28]),
	Category(11683, "MECÂNICO AUTO OFICIAL 1", ranges[18]),
	Category(11684, "MECÂNICO AUTO OFICIAL 2", ranges[17]),
	Category(11685, "MECÂNICO AUTO OFICIAL 3", ranges[16]),
	Category(11757, "PINTOR OFICIAL 1", ranges[6]),
	Category(11758, "PINTOR OFICIAL 2", ranges[5]),
	Category(11759, "PINTOR OFICIAL 3", ranges[4]),
	Category(11827, "SERRALHEIRO CIVIL OFICIAL 1", ranges[10]),
	Category(11851, "SERRALHEIRO MECÂNICO OF.1", ranges[36]),
	Category(11873, "SOLDADOR ELECTR. OXIAC. OF.1", ranges[34]),
	Category(11874, "SOLDADOR ELECTR. OXIAC. OF.2", ranges[33]),
	Category(11875, "SOLDADOR ELECTR. OXIAC. OF.3", ranges[32])
]