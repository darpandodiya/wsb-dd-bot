import praw

USER_AGENT = "<>"
CLIENT_ID = "<>"
CLIENT_SECRET = "<>"
USERNAME = "<>"
PASSWORD = "<>"
reddit = None


def main():
    global reddit
    reddit = praw.Reddit(
        user_agent=USER_AGENT,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        username=USERNAME,
        password=PASSWORD,
    )
    stream_wsb()


def stream_wsb():
    subreddit = reddit.subreddit("wallstreetbets")
    for submission in subreddit.stream.submissions():
        process_submission(submission)


def print_dd(submission):
    pretty_print = "Flair >> {0}\n" \
                   "Title >> {1}\n" \
                   "Score >> {2}\n" \
                   "ID >> {3}\n" \
                   "URL >> {4}\n".format(
                    submission.link_flair_text,
                    submission.title,
                    submission.score,
                    submission.id,
                    submission.url)
    print(pretty_print)
    return pretty_print


def send_message(message):
    reddit.redditor("<>").message("Tendies Time", message)
    print("Message sent successfully")


def process_submission(submission):
    allowed_flairs = ["DD", "Stocks", 'Fundamentals', "Options", "YOLO", "Discussion"]
    if submission.link_flair_text in allowed_flairs:
        message = print_dd(submission)
        send_message(message)


if __name__ == "__main__":
    main()
