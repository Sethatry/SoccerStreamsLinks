"""Soccer Streams Link Retriever 1.0, by u/Madelesi. I'm not associated with r/soccerstreams, the link hosts, or the
commenters in any way, and I'm not responsible for incorrect/harmful links."""
import praw

reddit = praw.Reddit(client_id='cE9bHW5woktIHw',
                     client_secret='vaLr2QVXSG6N3h2tvbvoGiMZkZ0',
                     user_agent='Soccer Streams Links Retriever.Test')
subreddit = reddit.subreddit('soccerstreams')


def choose_stream():
    submission_list = []
    for submission in subreddit.new(limit=10):
        if 'vs' in submission.title or 'GMT' in submission.title:
            print(submission.title)
            submission_list.append(submission)
    team = input('Choose Team: ')                       # You can change the values of  team,quality variables
    quality = input('Choose Quality(720 or 520): ')     # to always use the same team and quality, for example make
    return team, quality, submission_list             # team = 'Barcelona' and quality = '720'


def get_stream_link():
    team, quality, submission_list = choose_stream()

    if not submission_list:
        return 'No Streams Available Right Now'
    for submission in submission_list:
        if team in submission.title:
            print('Team Found')
            for top_level_comment in submission.comments:
                if quality in top_level_comment.body:
                    print('Quality Available')
                    comment = top_level_comment.body[top_level_comment.body.index(quality):]  # we only want the part
                    start_link = comment.index('http')       # after quality because some comments have
                    end_link = comment.find(')',start_link)  # multiple links, the comment variable isn't
                    return comment[start_link:end_link]      # necessary but helps and keeps code cleaner.

            if quality == '720':
                quality = 'HD'                               # Trying to use HD if 720 is not found in comments
                for top_level_comment in submission.comments:
                    if quality in top_level_comment.body:
                        print ('HD Quality Available ')
                        comment = top_level_comment.body[top_level_comment.body.index(quality):]
                        start_link = comment.index('http')
                        end_link = comment.find(')', start_link)
                        return comment[start_link:end_link]
            if quality == '520':
                quality = 'SD'                    # Trying to use SD if 520 isn't found in comments
                for top_level_comment in submission.comments:
                    if quality in top_level_comment.body:
                        print ('SD Quality Available')
                        comment = top_level_comment.body[top_level_comment.body.index(quality):]
                        start_link = comment.index('http')
                        end_link = comment.find(')', start_link)
                        return comment[start_link:end_link]
            print('Quality Not Available, here is full Comment: ')
            for top_level_comment in submission.comments:   # Using the for loop to get back to first comment
                return top_level_comment.body         # had I skipped the for loop line it would return the last comment


print(get_stream_link())
print (input('Press Any Key To Exit:'))