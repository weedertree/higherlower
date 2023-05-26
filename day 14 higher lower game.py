import random


logo = '''                                                     
                                                    
                                                    
   / __     ( )  ___     / __      ___      __      
  //   ) ) / / //   ) ) //   ) ) //___) ) //  ) )   
 //   / / / / ((___/ / //   / / //       //         
//   / / / /   //__   //   / / ((____   //          
                                                    
                                                    
                                                    
    ___      __                                     
  //   ) ) //  ) )                                  
 //   / / //                                        
((___/ / //                                         
                                                    
                                                    
                                                    
   //  ___                   ___      __            
  // //   ) ) //  / /  / / //___) ) //  ) )         
 // //   / / //  / /  / / //       //               
// ((___/ / ((__( (__/ / ((____   //          



'''



data = [
    {
    'name': 'pratham' ,
    'followercount' : 100,
    'gender' : 'gymboi',
    'college': 'iiithyd'
    },
    
{
    'name': 'sanskar' ,
    'followercount' : 50,
    'gender' : 'coke enjoyer',
    'college': 'mitp'
    },
    
    {
    'name': 'aayush' ,
    'followercount' : 50,
    'gender' : 'bihari',
    'college': 'drop year'
    },
    
    {
    'name': 'alok' ,
    'followercount' : 90,
    'gender' : 'naxali',
    'college': 'drop year'
    },
    
    
    {
    'name': 'rohit' ,
    'followercount' : 30,
    'gender' : 'pahadi',
    'college': 'gehu'
    },
    

    {
    'name': 'sreya' ,
    'followercount' : 1000,
    'gender' : 'bangali',
    'college': 'secret college'
    },
    

    
    {
    'name': 'chirag' ,
    'followercount' : 10,
    'gender' : 'frog',
    'college': 'uietk'
    },
    

    
    {
    'name': 'harshit' ,
    'followercount' : 60,
    'gender' : 'short guy',
    'college': 'iiitj'
    },
    
  
    {
    'name': 'parth' ,
    'followercount' : 20,
    'gender' : 'neet asp',
    'college': ' 2nd drop'
    },
    
 
    
    {
    'name': 'sushruti' ,
    'followercount' : 1009,
    'gender' : 'female',
    'college': 'medc'
    },
    
  
    {
    'name': 'sonu' ,
    'followercount' : 99,
    'gender' : 'marathi',
    'college': 'dosentrevealhiscollege'
    },
   
    {
    'name': 'priyanav' ,
    'followercount' : 79,
    'gender' : 'chess enthusiast',
    'college': 'iiitr'
    },
    
    ]

def check_ans (guess, a_followers, b_followers):
  if a_fc > b_fc:
      return guess == "a"
  else:
      return guess == "b"



#display art
print(logo)
score = 0
game_continue = True 
acc_b = random.choice(data)

#make game repeatable
while game_continue:


    #generate random acc from game
    acc_a = acc_b
    acc_b = random.choice(data)
    if acc_a == acc_b:
       acc_b = random.choice(data)
         
    def format_data(account):
        
        '''format the account data into printable format'''
        acc_name = account["name"]
        acc_gender = account["gender"]
        acc_college = account["college"]
        return f"{acc_name} , a {acc_gender}, from {acc_college}"
    
    
    
    
    print(f"compare A: {format_data(acc_a)}.")
    
    
    print ("               Versus                ")
    
    
    print(f"compare B: {format_data(acc_b)}.")
    
    
    #ask for a guess
    guess =input("Who has more followers on instagram A or B? ").lower()
    
    
    #check if user is correct
    
    ##get follower count of each user
    a_fc = acc_a ["followercount"]
    b_fc = acc_b ["followercount"]
    
    is_crct = check_ans (guess, a_fc, b_fc)
    ##use if statement to check if user is correct
    
    
    #clear screen for bottom rounds
   
    
    #give user feedback on their guess
    if is_crct:
        score += 1
        print(f" You're RIGHT! current score = {score}")
        
    else:
        game_continue = False
        print(f" That's WRONG. final score is: {score}")
        
#scorekeeping

#making account at position b become the next accont at position a

