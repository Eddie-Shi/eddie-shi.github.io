from re import sub
import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment function from the madlibs assignment here
madlibs = [
    'Who is running this lame [COLLECTION] of [BOTS] & [TROLLS] anyway? Try harder! I’m an [ENGINEER], knucklehead. Just do [“BUSINESS”] on the side.',
    'Tesla is filing a [LAWSUIT] against [ALAMEDA COUNTY] immediately. The unelected & ignorant [“INTERIM HEALTH OFFICER”] of [ALAMEDA] is acting contrary to the [GOVERNOR], the President, our Constitutional freedoms & just plain common sense!', 
    '(Formerly) [MAINSTREAM MEDIA] has systemic negative & political bias about almost everything. Reading major [NEWSPAPERS] makes you feel sad & [ANGRY]. That’s why they’re being [CRUSH] by [@JOEROGAN]. ',
    '[EXTREMELY] big difference between died because of or died with. Also, did the person actually have [C19] or did they just have [C19] symptoms? It’s almost impossible to [DIE] without feeling [WEAKNESS], shortness of breath or other [C19] symptoms, unless you were crushed by a falling [PIANO].',
    'Another reason reported [MORTALITY] rate is overstated is that dying [*WITH*] [COVID] is not same as dying [*FROM*] covid. [MEDIA] keeps reporting former, not latter.',
    'Well said! Please run for [OFFICE]. The politicians & unelected bureaucrats who stole our [LIBERTY] should be [TARRED], feathered & [THROWN] out of [TOWN]!']

replacements = {
    'COLLECTION' : ['group', 'herd', 'wave', 'kind', 'mass', 'collection'],
    'BOTS' : ['robot', 'losers', 'braindead', 'mentally challenged', 'bots'],
    'TROLLS': ['no-life losers', 'losers', 'no-lifers','edgelords', 'bad jokers'],
    'ENGINEER': ['Gamer', 'Memer', 'Engineer', 'Billionare', 'King'],
    '"BUSINESS"': ['your mom', 'drugs', '"business"', '69', 'gamer moment'],
    'LAWSUIT': ['action', 'trial', 'epic moment', 'gamer moment', 'lawsuit'],
    'ALAMEDA COUNTY': ['the US', 'Mars', 'the Earth', 'the poor people','Alameda County'],
    'ALAMEDA': ['the US', 'Mars', 'the Earth', 'poor people','Alameda County'],
    '“INTERIM HEALTH OFFICER”': ['clown', 'gamer', 'Interim Health Officer', 'tax-paid official', 'Joker'],
    'GOVERNOR': ['citizens', 'rich people', 'me', 'Governor','Alameda'],
    'MAINSTREAM MEDIA':['Fox News', 'CNN', 'Twitter', 'Daily Wire', 'Mainstream Media'],
    'NEWSPAPERS': ['newspapers', 'news outlet', 'news website', 'media', 'news'],
    'ANGRY': ['angry', 'outraged', 'grumpy','not epic', 'not feeling the vibe'],
    'CRUSHED': ['shit on', 'dunked on', 'crushed', 'destroyed', 'bombed'],
    '@JOEROGAN': ['your mom\'s ass','Alex Jones', 'Ben Shapiro', '@joerogan', 'me'],
    'EXTREMELY': ['Very', 'Tremendous', 'Gigantic', 'Enormous', 'Extremely'],
    'C19': ['Ligma', 'Sigma', 'COVID','COVID-19','C19'],
    'DIE': ['die', 'not-living', 'get robloxed', 'not-breathing', 'get oof-ed', 'pass away'],
    'WEAKNESS':['not epic', 'weakness', 'exhaustion', 'fatique','weakness'],
    'PIANO':['piano', 'SpaceX rocket','Tesla', 'your mom', 'ass'],
    'MORTALITY': ['death', 'not-living', 'robloxed', 'not-breathing', 'oof-ed', 'pass away'],
    'COVID': ['Ligma', 'Sigma', 'COVID','COVID-19','C19'],
    '*WITH*': ['*along*', '*besides*','*with*','*accompanied by*', '*in the company of*'],
    '*FROM*': ['*by*', '*from*', '*against*','out of','of'],
    'MEDIA': ['Fox News', 'CNN', 'Twitter', 'Daily Wire', 'Mainstream Media'],
    'OFFICE': ['President', 'Governor', 'Mayor', 'Congress', 'Senate'],
    'LIBERTY':['freedom', 'sovereinty', 'human rights', 'liberty', 'independence'],
    'TARRED': ['terrified', 'ashamed', 'tarred', 'fouled', 'scared'],
    'THROWN': ['thrown', 'kicked', 'yeeted','tossed','hurled'],
    'TOWN': ['town', 'the country', 'the state', 'the planey', 'the universe']
    }

def generate_comment():

    m = random.choice(madlibs)
    for k in replacements.keys():
        m = m.replace('['+k+']', random.choice(replacements[k]))
    return m
# connect to reddit 
reddit = praw.Reddit('bot')


# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://old.reddit.com/r/BotTown/comments/qvlcrc/elonmuskbadtakes_thread/?'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once 
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    submission.comments.replace_more(limit=None, threshold=0)
    all_comments = submission.comments.list()

    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        if str(comment.author) != 'ElonMuskBadTakeBot':
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has not commented = ', has_not_commented)
    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        submission.reply(generate_comment())

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        
        for comment in not_my_comments:
            comment_reply_author = []
            for reply in comment.replies:
                comment_reply_author.append(str(reply.author))
            if 'ElonMuskBadTakeBot' in comment_reply_author:
                pass
            else:
                comments_without_replies.append(comment)
        
                
         
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        comment = random.choice(comments_without_replies)
        try:
            comment.reply(generate_comment())
        except praw.exceptions.APIException:
            print("not replying to a deleted comment.")
            pass

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    submission = random.choice(list(reddit.subreddit("BotTown").hot(limit=5)))
    

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(10*60)


