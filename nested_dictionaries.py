ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}


## Exercise 2: Nested Dictionaries

email = (ramit['email'])  ## Gets the email address of Ramit

interests = (ramit['interests'][0])  ## Gets the first of Ramit's interests.

jasmine_email = (ramit['friends'][0]['email']) ## Gets th eemial address of Jasmine.

jan_interest = (ramit['friends'][1]['interests'][1])  ## Gets the second of Jan's two intrerests.
                          

## Excercise 3: Friend Counter

## Function that accepts a dictionary as an agument and returns a new (appended) dictionary with a new key "friends_count".

## Function that accepts the dictionary as an argument:
def countFriends(dictionary):
    new_dictionary = dictionary  ## Creats a new dictionary with the same contents as input dictionary.
    friends_count = len(dictionary['friends'])  ## Checks "friends" key for number of friends.
    new_dictionary['friends_count'] = friends_count  ## Adds new key 'friends_count' and '2' to the new dictionary.
    return new_dictionary  ## Returns the new dictionary.


##  print(countFriends(ramit))   **** Just a test print statment to check dictionary.***



