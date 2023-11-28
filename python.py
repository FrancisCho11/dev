print("hello world!")
#====================
def magician_name(magician):
	print("My favourite magician is" + magician.title() +"!")
magician_name(Todd)
#====================
def describe_pet(animal_type, pet_name):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet("hamster", "harry")
#=================================
#user.py
user_0 = {'username':'efermi','first':'enrico','last':'fermi'}

for key, value in user_0.items(): #使用items()返回一个键值对列表
	print(f"\nKey:{key}") 
	#使用print(f"")来输出格式化的变量，变量不需要在""外单独表示，可以在引号内用{}表示
	print(f"Value:{value}")

#favourite_languages.py
favourite_languages = {'jen':'python','sarah':'c','edward':'ruby','phil':'python'}

for name, language in favourite_languages.item():
	print(f"{name.title()}'s favourite language is {language.title()}.")

#====================================
#使用keys()遍历字典中的所有键
#favourite_languages.py

for name in favourite_languages.keys():
	print(name.title())
#使用name&value还是name&language根据程序代码决定，易读为前提
#keys()使得name指向字典中的键
#使用keys()可以让代码更易懂，但也可以忽略
#===================================
#按特定顺序遍历字典中的所有键
#favourite_languages.py

for name in sorted(favourite_languages.keys()):
	print(f"{name.title()}, tank you for taking the poll.")
#====================================
#使用集合set()来剔除列表中的重复项，集合中的每个元素都是独一无二的
for language in set(favourite_languages.values()):
	print(language.title())

#======================================
#嵌套
#========================================
#在字典中存储列表
pizza = {'crust':'thick','toppings':['mushroom','extra cheese']}
#在字典中存储字典
users = {
	'aeistein' : {
		'first' : 'albert',
		'last' : 'einstein',
		'location' : 'princeton',
		},
	'mcurie' : {
		'first' : 'marie',
		'last' : 'curie',
		'location' : 'paris',
	},
	}
	
	
#======================================
#CH7 用户输入和while循环
#======================================
#用户输入
#parrot.py
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")






	
	
	