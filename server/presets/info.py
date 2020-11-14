
card_task = '''
You just bought a public transit card that allows you to ride the Metro for a certain number of days.

Here is how it works: upon first receiving the card, the system allocates you a 31-day pass, which equals the number of days in January. The second time you pay for the card, your pass is extended by 28 days, i.e. the number of days in February (note that leap years are not considered), and so on. The 13th time you extend the pass, you get 31 days again.

You just ran out of days on the card, and unfortunately you've forgotten how many times your pass has been extended so far. However, you do remember the number of days you were able to ride the Metro during this most recent month.

Task
Figure out the number of days by which your pass will now be extended, and return all the options as an array sorted in increasing order.
'''

treasure_task = '''
It's a lovely day, you're once again visiting the Tech With Tim Building. Suddenly, as you walk down the stairs, you find a special treasure chest! There are two items in it!

Task
The first item weighs weight1 and is worth value1, and the second item weighs weight2 and is worth value2. What is the total maximum value of the items you can take with you, assuming that your max weight capacity is maxW and you can't come back for the items later?

Note that there are only two items and you can't bring more than one item of each type, i.e. you can't take two first items or two second items.
'''

INFO = {
    'CardTiming': {
        'TASK': card_task,
        'EXAMPLES': {
            30: [31]
        }
    },
    'Treasure': {
       'TASK': treasure_task,
        'EXAMPLES': {
            'value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 8': 10,
            'value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 9': 16
        }
    }
}
