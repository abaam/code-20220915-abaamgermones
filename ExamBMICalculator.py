import json

# Start of Class BMICalculator
class BMICalculator :

	aList =[]
	overwieght = 0

	def	__init__(self, RawData):
		self.aList = json.loads(RawData)

		count = 0
		
		for x in self.aList :
			BMI = self.calculate(x['HeightCm'], x['WeightKg'])
			self.aList[count].update(BMI)
			count +=1

			#count the numner of OverWeight
			if self.checkIfOverWeight(BMI) == "Overweight" :
				overwieght += 1


		print("NO of OverWEight = " + str(self.overwieght))
		print self.aList



	#check if Over Weight 
	def checkIfOverWeight(self, result):
		return result["BMI Category"]
	
	#calculation of BMI
	def calculate(self, Height,Mass) :
		#compute BMI
		BMI = (Mass) / (Height*Height)

		#classify or categorize 
		
		if BMI <= 18.4 :
			return {"BMI Category" : "Underweight", "BMI Range" : "18.4 and below", "Health risk" : "Malnutrition risk"}

		elif BMI >= 18.5 and BMI <= 24.9 :
			return {"BMI Category" : "Normal weight", "BMI Range" : "18.5 - 24.9", "Health risk" : "Low risk"}

		elif BMI >= 25 and BMI <= 29.9 :
			return {"BMI Category" : "Normal weight", "BMI Range" : "25 - 29.9", "Health risk" : "Enhanced risk"}

			
		elif BMI >= 30 and BMI <= 34.9 :
			return {"BMI Category" : "Moderately obese", "BMI Range" : "30 - 34.9", "Health risk" : "Medium risk"}

		elif BMI >= 35 and BMI <= 39.9 :
			return {"BMI Category" : "Severely obese", "BMI Range" : "35 - 39.9", "Health risk" : "High risk"}

		elif BMI >= 40 :
			return {"BMI Category" : "Very severely obese" ,  "BMI Range" : "40 and above", "Health risk" : "Very high risk"}

	

# end of class BMICalculator


#TESTING HERE
rawData = '[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166, "WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]'
testobj = BMICalculator(rawData)